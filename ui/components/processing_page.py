import os
import time
import streamlit as st
from pipeline.graph import graph

def show_processing_page():
    idea_data = st.session_state.get("idea", {})
    startup_name = idea_data.get("startup_name", "Startup Idea")
    industry = idea_data.get("industry", "Technology")
    target_audience = idea_data.get("target_audience", "General Public")
    business_model = idea_data.get("business_model", "Freemium")
    problem = idea_data.get("problem", "")
    solution = idea_data.get("solution", "")

    st.markdown("<h1 style='text-align:center; color:#ffffff; font-weight:600; letter-spacing:-0.03em;'>🤖 AI Multi-Agent Processing</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#9a9a9a; font-size:15px; margin-top:-8px;'>Synthesizing real-time market data, competitive intelligence, and empirical ML feasibility...</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    startup_idea_full = (
        f"Startup Name: {startup_name}\n"
        f"Industry: {industry}\n"
        f"Target Audience: {target_audience}\n"
        f"Business Model: {business_model}\n"
        f"Problem Statement: {problem}\n"
        f"Proposed Solution: {solution}"
    )

    api_key = st.session_state.get("gemini_api_key") or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")

    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key
        os.environ["GOOGLE_API_KEY"] = api_key

    progress_bar = st.progress(0)
    status_box = st.empty()

    agents_list = [
        ("Web Search Agent", 15),
        ("Market Opportunity Agent", 30),
        ("Competitor Discovery Agent", 45),
        ("SWOT & Risk Analysis Agent", 60),
        ("MVP Recommendation Agent", 75),
        ("Go-To-Market Strategy Agent", 90),
        ("Validation Report Agent", 100),
    ]

    initial_state = {
        "startup_idea": startup_idea_full,
        "idea_extraction": {
            "startup_name": startup_name,
            "industry": industry,
            "target_audience": target_audience,
            "business_model": business_model,
            "problem": problem,
            "solution": solution,
        },
        "web_search_results": {},
        "market_analysis": {},
        "competitor_analysis": {},
        "swot_analysis": {},
        "mvp_recommendation": {},
        "gtm_strategy": {},
        "report": {},
    }

    if not api_key:
        status_box.warning("⚠️ No Gemini API Key provided. Running in Demonstration Mode with simulated deep analysis.")
        time.sleep(1.0)
        for agent_name, pct in agents_list:
            status_box.info(f"⏳ **Running Agent:** {agent_name}...")
            progress_bar.progress(pct)
        # Compute live ML prediction from custom trained model
        from tools.ml_predictor import get_ml_predictor
        ml_res = get_ml_predictor().predict_feasibility(idea_data, competitor_count=2)

        # Generate realistic demo output structure aligned with GraphState
        mock_report = {
            "executive_summary": f"{startup_name} addresses a significant pain point in the {industry} sector. The proposed solution has strong value proposition potential for {target_audience}.",
            "final_validation_score": ml_res["feasibility_score"],
            "ml_prediction": ml_res,
            "market_analysis": {
                "market_size": "Estimated $14.2 Billion TAM with 18.5% YoY Growth",
                "target_audience": target_audience,
                "industry_trends": f"Accelerating digital transformation and AI adoption in {industry}.",
                "opportunities": f"High demand for automated solutions tailored to {target_audience}."
            },
            "competitor_analysis": [
                {
                    "name": "Industry Leader Alpha",
                    "website": "https://example.com/alpha",
                    "description": "Established enterprise provider with legacy software footprint.",
                    "strengths": ["Strong brand equity", "Broad distribution network"],
                    "weaknesses": ["Slow feature updates", "Higher pricing tier"]
                },
                {
                    "name": "NextGen Solution Beta",
                    "website": "https://example.com/beta",
                    "description": "Modern cloud-native alternative targeting SMBs.",
                    "strengths": ["User-friendly UI", "Low onboarding barrier"],
                    "weaknesses": ["Limited customer support", "Lacks advanced analytics"]
                }
            ],
            "swot_analysis": {
                "strengths": ["First-mover advantage in niche segment", "AI-first core architecture", "Scalable cloud design"],
                "weaknesses": ["Initial brand awareness gap", "Requires high-quality training/domain data"],
                "opportunities": ["Rapid enterprise adoption", "Integration with existing ecosystem tools"],
                "threats": ["Potential entry by incumbents", "Evolving regulatory standards"],
                "risks": [
                    {
                        "risk": "Customer Acquisition Friction",
                        "severity": "Medium",
                        "mitigation": "Offer freemium trial and self-service onboarding."
                    },
                    {
                        "risk": "Data Privacy & Compliance",
                        "severity": "High",
                        "mitigation": "Implement end-to-end encryption and SOC2 compliance early."
                    }
                ]
            },
            "mvp_recommendation": {
                "must_have": [
                    {"feature": "Core AI Engine & Workflow Tool", "reason": "Validates essential problem-solution fit", "validation_goal": "User satisfaction & retention"},
                    {"feature": "Automated Report & Dashboard", "reason": "Delivers immediate quantifiable value", "validation_goal": "Demonstrates ROI to decision makers"}
                ],
                "nice_to_have": [
                    {"feature": "Third-Party API Integrations", "reason": "Enhances workflow efficiency", "validation_goal": "Increases user stickiness"}
                ],
                "future_features": [
                    {"feature": "Custom Enterprise SLA & Multi-tenancy", "reason": "Required for large enterprise contracts", "validation_goal": "Enterprise scale readiness"}
                ],
                "prioritization_rationale": "Focus first on core AI processing to prove user demand before building enterprise governance features."
            },
            "gtm_strategy": {
                "positioning_strategy": f"Position {startup_name} as the most intelligent and easy-to-use platform for {target_audience} in the {industry} domain.",
                "pricing_ideas": [
                    {"model": "Freemium / Tiered SaaS", "reason": "Lowers friction for initial user adoption while enabling monetization at scale."}
                ],
                "customer_acquisition_channels": [
                    {"channel": "Product-Led Growth (PLG)", "reason": "Allows founders to test value immediately with minimal sales friction."},
                    {"channel": "Targeted Community & Content Marketing", "reason": "Establishes authority in niche communities where target users hangout."}
                ],
                "launch_strategy": [
                    "1. Private Beta launch to 50 select design partners.",
                    "2. Collect qualitative feedback and iterate on core workflow.",
                    "3. Public Product Hunt & Hacker News launch with freemium tier.",
                    "4. Scale inbound content marketing and strategic partnerships."
                ]
            },
            "references": [
                "https://duckduckgo.com/?q=" + startup_name.replace(" ", "+")
            ]
        }

        st.session_state.results = {
            "startup_idea": startup_idea_full,
            "market_analysis": mock_report["market_analysis"],
            "competitor_analysis": {"competitors": mock_report["competitor_analysis"]},
            "swot_analysis": mock_report["swot_analysis"],
            "mvp_recommendation": mock_report["mvp_recommendation"],
            "gtm_strategy": mock_report["gtm_strategy"],
            "report": mock_report
        }
        st.session_state.report = mock_report
    else:
        try:
            status_box.info("🚀 **Initializing Multi-Agent Pipeline...**")
            progress_bar.progress(10)
            
            # Execute real LangGraph multi-agent pipeline
            final_state = graph.invoke(initial_state)
            
            progress_bar.progress(100)
            status_box.success("✅ Multi-Agent Validation Pipeline execution complete!")
            
            st.session_state.results = final_state
            
            # Extract final report or construct structured view
            if final_state.get("report") and isinstance(final_state["report"], dict):
                report_data = final_state["report"].get("validation_report", final_state["report"])
            else:
                report_data = final_state

            if "ml_prediction" not in report_data and "ml_prediction" in final_state:
                report_data["ml_prediction"] = final_state["ml_prediction"]
                
            st.session_state.report = report_data
            
        except Exception as e:
            status_box.error(f"❌ Error during multi-agent pipeline execution: {str(e)}")
            st.warning("Please verify your Gemini API key in the sidebar or try again.")
            if st.button("⬅️ Return to Submission"):
                st.session_state.page = "submit"
                st.rerun()
            return

    time.sleep(0.8)
    st.session_state.page = "report"
    st.rerun()