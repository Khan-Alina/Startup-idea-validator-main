import streamlit as st

def show_idea_input():
    st.markdown("<h1 style='text-align:center; color:#ffffff; font-weight:600; letter-spacing:-0.03em;'>💡 Submit Your Startup Idea</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#9a9a9a; font-size:15px; margin-top:-8px;'>Provide key venture details to run automated deep validation & empirical ML feasibility forecasting.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        startup_name = st.text_input("🚀 Startup Name", placeholder="e.g. AI Idea Validator")
        industry = st.selectbox(
            "🏢 Industry",
            ["AI", "FinTech", "Healthcare", "EdTech", "E-Commerce", "Cybersecurity", "SaaS", "Other"]
        )

    with col2:
        target_audience = st.text_input("🎯 Target Audience", placeholder="e.g. Founders, Investors")
        business_model = st.selectbox(
            "💼 Business Model",
            ["B2B", "B2C", "Subscription", "Marketplace", "Freemium"]
        )

    problem = st.text_area(
        "❓ Problem Statement",
        height=110,
        placeholder="What core problem are you solving?"
    )

    solution = st.text_area(
        "🛠️ Proposed Solution",
        height=110,
        placeholder="How does your startup solve this problem?"
    )

    # Optional early-stage parameters for the custom ML feasibility predictor
    with st.expander("⚙️ **Advanced Startup Parameters (ML Model Inputs)**", expanded=False):
        st.caption("These parameters feed directly into our trained Random Forest Feasibility Model (92.3% test accuracy).")
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            market_size = st.selectbox("🌐 Target Market Size", ["Medium", "Large", "Small"], index=0)
            founder_exp = st.slider("🎓 Founder Experience (Years)", min_value=0, max_value=20, value=3, step=1)
        with m_col2:
            team_size = st.slider("👥 Initial Team Size", min_value=1, max_value=25, value=3, step=1)
            funding_k = st.slider("💰 Pre-Seed Funding ($k USD)", min_value=10, max_value=1000, value=150, step=10)
        with m_col3:
            burn_rate_k = st.slider("🔥 Est. Monthly Burn ($k USD)", min_value=1, max_value=100, value=15, step=1)
            est_competitors = st.slider("🥊 Known Direct Competitors", min_value=0, max_value=20, value=4, step=1)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("📊 Analyze Startup Idea", use_container_width=True):
        if not startup_name or not problem or not solution:
            st.warning("Please fill in at least the Startup Name, Problem, and Solution.")
        else:
            st.session_state.idea = {
                "startup_name": startup_name,
                "industry": industry,
                "target_audience": target_audience,
                "business_model": business_model,
                "problem": problem,
                "solution": solution,
                "market_size": locals().get("market_size", "Medium"),
                "founder_experience_years": locals().get("founder_exp", 3),
                "team_size": locals().get("team_size", 3),
                "funding_usd_m": round(locals().get("funding_k", 150) / 1000.0, 3),
                "burn_rate_usd_m": round(locals().get("burn_rate_k", 15) / 1000.0, 3),
                "competitors": locals().get("est_competitors", 4)
            }
            st.session_state.page = "processing"
            st.rerun()