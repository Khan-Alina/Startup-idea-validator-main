# Verification script for ML model and pipeline integration
import sys
from pathlib import Path

# Add project root
root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

print("[1/4] Checking tools.ml_predictor...")
from tools.ml_predictor import get_ml_predictor
predictor = get_ml_predictor()
assert predictor.is_model_ready(), "Model not loaded!"

test_idea = {
    "startup_name": "HealthAI Diagnostics",
    "industry": "Healthcare",
    "business_model": "Subscription",
    "problem": "Manual radiology analysis takes 48 hours and causes clinical delays.",
    "solution": "Real-time AI diagnostic assistant for hospital radiologists.",
    "founder_experience_years": 5,
    "team_size": 4,
    "funding_usd_m": 0.25,
    "burn_rate_usd_m": 0.02,
    "competitors": 3
}

pred = predictor.predict_feasibility(test_idea, competitor_count=3)
print(f"    Feasibility Score: {pred['feasibility_score']}/100")
print(f"    Success Probability: {pred['success_probability']}%")
print(f"    Risk Level: {pred['risk_level']}")
print(f"    Top Drivers: {pred['top_positive_drivers']}")

print("[2/4] Checking pipeline graph imports and state structure...")
from pipeline.graph import GraphState
state_keys = GraphState.__annotations__.keys()
assert "ml_prediction" in state_keys, "ml_prediction missing in GraphState!"

print("[3/4] Checking UI components imports...")
import ui.components.report_viewer
import ui.components.idea_input
import ui.components.processing_page

print("[4/4] Checking visual plot artifacts exist on disk...")
assert (root / "ml_models" / "feature_importance.png").exists()
assert (root / "ml_models" / "confusion_matrix.png").exists()
assert (root / "ml_models" / "roc_curve.png").exists()
assert (root / "ml_models" / "model_metrics.json").exists()

print("\nSUCCESS: All components and ML integration verified successfully!")
