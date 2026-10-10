# Multi-Agent Roles & Operational Specifications

This document outlines the architectural responsibilities, input dependencies, output schemas, and prompt strategies for all specialized agents in the Autonomous Startup Validation pipeline.

---

## 1. Idea Extraction Agent
- **Module**: `agents/idea_extraction_agent.py`
- **Purpose**: Normalizes raw user input into a standardized format.
- **Inputs**: Raw startup idea string (problem, solution, target audience).
- **Outputs**: Structured JSON with `startup_name`, `industry`, `target_audience`, `business_model`, `problem`, `solution`.
- **Reasoning Model**: Evaluates semantic clarity and derives missing attributes based on industry patterns.

---

## 2. Web Search & SERP Agent
- **Module**: `agents/web_search_agent.py`
- **Tooling**: `tools/web_search_tool.py` (DuckDuckGo Search Engine API)
- **Purpose**: Retrieves real-time market data, existing competitors, and industry trends without relying solely on static LLM training cutoff data.
- **Search Strategy**: Constructs targeted boolean queries:
  - `"{industry} market size growth trends 2025 2026"`
  - `"{startup_name} alternatives competitors {industry}"`
  - `"{problem} software solutions startups"`
- **Outputs**: Filtered snippet dictionary with title, snippet, and source URLs.

---

## 3. Market Opportunity & Sizing Agent
- **Module**: `agents/market_analysis_agent.py`
- **Purpose**: Evaluates economic viability and market dynamics.
- **Outputs**:
  - **Market Size (TAM/SAM/SOM)**: Evaluates dollar/growth estimates.
  - **Target Customer Profiles**: Primary buyer personas and demographic traits.
  - **Industry Trends**: Macro adoption tailwinds.
  - **Growth Opportunities**: Untapped niches and customer segments.

---

## 4. Competitor Discovery & Intelligence Agent
- **Module**: `agents/competitor_agent.py`
- **Purpose**: Discovers direct and indirect incumbents to determine market saturation.
- **Outputs**:
  - List of competitor profiles (Name, Website, Product overview).
  - Competitor core strengths.
  - Competitor vulnerabilities & gaps (where the startup can win).

---

## 5. SWOT & Risk Assessment Agent
- **Module**: `agents/swot_risk_agent.py`
- **Purpose**: Performs internal/external situational analysis.
- **Outputs**:
  - **Strengths**: Internal competitive differentiators.
  - **Weaknesses**: Internal operational and capital constraints.
  - **Opportunities**: External market expansion factors.
  - **Threats**: External regulatory, platform, or incumbent threats.
  - **Execution Risk Table**: Specific risk items categorized by Severity (High, Medium, Low) with actionable mitigation protocols.

---

## 6. MVP Feature Recommendation Agent
- **Module**: `agents/mvp_recommendation_agent.py`
- **Purpose**: Applies MoSCoW prioritization to minimize initial development waste.
- **Outputs**:
  - **Must-Have (P1)**: Core features required to validate the primary hypothesis.
  - **Nice-to-Have (P2)**: Features that enhance retention for Phase 2.
  - **Future Features (P3)**: Scalability and enterprise add-ons.
  - **Strategic Rationale**: Justification for feature trade-offs.

---

## 7. Go-To-Market (GTM) Strategy Agent
- **Module**: `agents/gtm_strategy_agent.py`
- **Purpose**: Defines monetization and customer acquisition channels.
- **Outputs**:
  - **Positioning Statement**: Value proposition differentiation.
  - **Pricing Models**: SaaS tiers, usage-based, freemium, or take-rate.
  - **Acquisition Channels**: PLG, community marketing, cold outreach, SEO.
  - **Launch Sequencing**: Step-by-step roadmap from private beta to public launch.

---

## 8. Startup Validation Report Compiler Agent
- **Module**: `agents/report_agent.py`
- **Purpose**: Evaluates all upstream findings and assigns an aggregate Feasibility Score (0-100).
- **Outputs**:
  - Executive Summary.
  - Final Validation Score with weighted criteria (Market Demand 30%, Competitor Space 25%, Feasibility 25%, GTM Viability 20%).
  - References and citations.

---

## 9. Conversational Startup Advisor
- **Module**: `agents/conversational_advisor.py`
- **Purpose**: Interactive conversational AI grounded in the validation report context.
- **Capabilities**: Answers questions regarding competitor risks, MVP scoping, and investor pitch preparation.
