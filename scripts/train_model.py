# Startup Feasibility & Success Prediction - ML Training Pipeline
import os
import json
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, roc_curve
)

def train_and_evaluate():
    base_dir = Path(__file__).resolve().parent.parent
    data_path = base_dir / 'data' / 'startup_ai_dataset_5000.csv'
    models_dir = base_dir / 'ml_models'
    models_dir.mkdir(exist_ok=True)

    print(f'[*] Loading dataset: {data_path}')
    df = pd.read_csv(data_path)
    print(f'[*] Loaded {len(df):,} startup records.')

    # Target: Successful = 1, Failed = 0
    df['target'] = (df['Status'].astype(str).str.strip() == 'Successful').astype(int)

    # Early-Stage features without post-hoc data leakage (no PMF or future revenue)
    categorical_features = ['Industry', 'Market_Size', 'Business_Model']
    numerical_features = [
        'Founder_Experience_Years',
        'Team_Size',
        'Funding_USD_M',
        'Burn_Rate_USD_M',
        'Competitors',
        'Innovation_Score'
    ]

    X = df[categorical_features + numerical_features]
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f'[*] Training samples: {len(X_train):,}, Testing samples: {len(X_test):,}')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
        ]
    )

    # 1. Baseline Model Comparison (Logistic Regression)
    baseline_pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))
    ])
    baseline_pipe.fit(X_train, y_train)
    y_base_pred = baseline_pipe.predict(X_test)
    base_acc = accuracy_score(y_test, y_base_pred)
    base_f1 = f1_score(y_test, y_base_pred)
    print(f'[+] Baseline Logistic Regression Accuracy: {base_acc * 100:.2f}%, F1: {base_f1 * 100:.2f}%')

    # 2. Production Model (Random Forest Classifier)
    rf_pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(
            n_estimators=180,
            max_depth=12,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        ))
    ])

    print('[*] Performing 5-Fold Stratified Cross-Validation...')
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(rf_pipe, X_train, y_train, cv=cv, scoring='accuracy', n_jobs=-1)
    print(f'[+] 5-Fold CV Mean Accuracy: {cv_scores.mean() * 100:.2f}% (std: {cv_scores.std() * 100:.2f}%)')

    print('[*] Training Production Random Forest Model...')
    rf_pipe.fit(X_train, y_train)

    y_pred = rf_pipe.predict(X_test)
    y_proba = rf_pipe.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)
    cm = confusion_matrix(y_test, y_pred)

    print('\n' + '=' * 60)
    print('       COLLEGE VIVA DEFENSE - ML VALIDATION REPORT')
    print('=' * 60)
    print(f'Test Accuracy:            {acc * 100:.2f}%')
    print(f'Baseline (LogReg) Acc:    {base_acc * 100:.2f}%')
    print(f'Model Accuracy Gain:     +{(acc - base_acc) * 100:.2f}%')
    print(f'Precision:                {prec * 100:.2f}%')
    print(f'Recall:                   {rec * 100:.2f}%')
    print(f'F1-Score:                 {f1 * 100:.2f}%')
    print(f'ROC-AUC Score:            {auc * 100:.2f}%')
    print(f'5-Fold CV Accuracy:       {cv_scores.mean() * 100:.2f}% ± {cv_scores.std() * 100:.2f}%')
    print(f'Confusion Matrix:\n{cm}')
    print('=' * 60)

    # Save Model Artifact
    model_path = models_dir / 'startup_feasibility_model.joblib'
    joblib.dump(rf_pipe, model_path)
    print(f'[OK] Serialized production model to: {model_path}')

    # Save Detailed Metrics JSON
    metrics = {
        'model_name': 'RandomForestClassifier (Ensemble)',
        'baseline_model': 'LogisticRegression',
        'n_estimators': 180,
        'max_depth': 12,
        'dataset_records': len(df),
        'train_samples': len(X_train),
        'test_samples': len(X_test),
        'accuracy_pct': round(float(acc) * 100, 2),
        'baseline_accuracy_pct': round(float(base_acc) * 100, 2),
        'precision_pct': round(float(prec) * 100, 2),
        'recall_pct': round(float(rec) * 100, 2),
        'f1_score_pct': round(float(f1) * 100, 2),
        'roc_auc_pct': round(float(auc) * 100, 2),
        'cv_mean_pct': round(float(cv_scores.mean()) * 100, 2),
        'cv_std_pct': round(float(cv_scores.std()) * 100, 2),
        'confusion_matrix': cm.tolist(),
        'features': {
            'categorical': categorical_features,
            'numerical': numerical_features
        }
    }
    with open(models_dir / 'model_metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)
    print('[OK] Saved model_metrics.json')

    # Set dark aesthetic for all plots to match Vesper.ai pure black UI
    plt.style.use('dark_background')
    plt.rcParams['font.family'] = 'sans-serif'

    # Visual 1: Feature Importance Chart (Dark Liquid Metal)
    fitted_pre = rf_pipe.named_steps['preprocessor']
    cat_out = fitted_pre.named_transformers_['cat'].get_feature_names_out(categorical_features).tolist()
    all_feats = numerical_features + cat_out
    importances = rf_pipe.named_steps['classifier'].feature_importances_

    feat_df = pd.DataFrame({'feature': all_feats, 'importance': importances})
    feat_df = feat_df.sort_values(by='importance', ascending=True).tail(12)

    display_names = [f.replace('cat__', '').replace('num__', '').replace('_', ' ') for f in feat_df['feature']]

    fig, ax = plt.subplots(figsize=(9.5, 6), facecolor='#09090b')
    ax.set_facecolor('#09090b')
    bars = ax.barh(display_names, feat_df['importance'], color='#f4f4f5', edgecolor='#a1a1aa', height=0.65)
    ax.set_title('Top Predictors of Startup Feasibility (Random Forest Gini Importance)', fontsize=13, fontweight='bold', color='#ffffff', pad=15)
    ax.set_xlabel('Importance Weight', fontsize=11, fontweight='bold', color='#a1a1aa')
    ax.grid(axis='x', linestyle=':', color='#27272a', alpha=0.8)
    ax.tick_params(colors='#d4d4d8', labelsize=10)
    for spine in ax.spines.values():
        spine.set_color('#27272a')
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.005, bar.get_y() + bar.get_height() / 2, f'{w:.3f}', va='center', ha='left', fontsize=9.5, fontweight='bold', color='#ffffff')
    plt.tight_layout()
    plt.savefig(models_dir / 'feature_importance.png', dpi=250, facecolor='#09090b', edgecolor='none')
    plt.close()
    print('[OK] Saved feature_importance.png (Dark Mode)')

    # Visual 2: Confusion Matrix Plot (Dark Monochrome)
    fig, ax = plt.subplots(figsize=(5.5, 5), facecolor='#09090b')
    ax.set_facecolor('#09090b')
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.bone)
    ax.set_title('Confusion Matrix - Startup Prediction (Test Set)', fontsize=12, fontweight='bold', color='#ffffff', pad=12)
    cbar = fig.colorbar(im, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(colors='#a1a1aa')
    ticks = [0, 1]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(['Failed', 'Successful'], fontsize=10, fontweight='bold', color='#d4d4d8')
    ax.set_yticklabels(['Failed', 'Successful'], fontsize=10, fontweight='bold', color='#d4d4d8')
    for i in range(2):
        for j in range(2):
            val = cm[i, j]
            color = '#09090b' if val > cm.max() / 2 else '#ffffff'
            ax.text(j, i, f'{val:,}', ha='center', va='center', color=color, fontsize=14, fontweight='bold')
    ax.set_ylabel('Ground Truth (Actual)', fontsize=11, fontweight='bold', color='#a1a1aa')
    ax.set_xlabel('Model Prediction', fontsize=11, fontweight='bold', color='#a1a1aa')
    for spine in ax.spines.values():
        spine.set_color('#27272a')
    plt.tight_layout()
    plt.savefig(models_dir / 'confusion_matrix.png', dpi=250, facecolor='#09090b', edgecolor='none')
    plt.close()
    print('[OK] Saved confusion_matrix.png (Dark Mode)')

    # Visual 3: ROC Curve Plot (Dark Silver)
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    fig, ax = plt.subplots(figsize=(6, 5), facecolor='#09090b')
    ax.set_facecolor('#09090b')
    ax.plot(fpr, tpr, color='#ffffff', lw=2.5, label=f'Random Forest (AUC = {auc:.3f})')
    ax.plot([0, 1], [0, 1], color='#52525b', lw=1.5, linestyle='--', label='Random Chance (AUC = 0.50)')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate (1 - Specificity)', fontsize=10, fontweight='bold', color='#a1a1aa')
    ax.set_ylabel('True Positive Rate (Sensitivity)', fontsize=10, fontweight='bold', color='#a1a1aa')
    ax.set_title('Receiver Operating Characteristic (ROC) Curve', fontsize=12, fontweight='bold', color='#ffffff')
    ax.legend(loc='lower right', fontsize=10, facecolor='#18181b', edgecolor='#27272a')
    ax.grid(color='#27272a', linestyle=':', alpha=0.8)
    ax.tick_params(colors='#d4d4d8')
    for spine in ax.spines.values():
        spine.set_color('#27272a')
    plt.tight_layout()
    plt.savefig(models_dir / 'roc_curve.png', dpi=250, facecolor='#09090b', edgecolor='none')
    plt.close()
    print('[OK] Saved roc_curve.png (Dark Mode)')

if __name__ == '__main__':
    train_and_evaluate()
