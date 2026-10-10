# Autonomous Multi-Agent AI Startup Idea Validator

> **An End-to-End Autonomous Multi-Agent Intelligence System for Real-Time Market Demand Analysis, Competitor Benchmarking, SWOT & Execution Risk Modeling, and Go-To-Market Synthesis.**

---

## 📌 Project Overview & Abstract

Early-stage startup failure rates exceed 90%, predominantly due to building products without verified market need, misjudging existing competition, or underestimating execution risks. Traditional manual market validation is fragmented, expensive, and takes weeks of manual research.

The **Autonomous Multi-Agent AI Startup Idea Validator** addresses this problem by automating the entire research and feasibility assessment pipeline. Utilizing a stateful cyclic multi-agent graph powered by **LangGraph**, **Google Gemini Large Language Models**, and **DuckDuckGo Live Web Search**, the system decomposes an initial startup hypothesis into structured validation dimensions in under 60 seconds.

---

## 🎯 Key Objectives

1. **Autonomous Web Retrieval**: Execute live search queries against DuckDuckGo to extract up-to-date market signals and existing competitor products.
2. **Market Sizing & Customer Segmentation**: Estimate Total Addressable Market (TAM), Serviceable Available Market (SAM), and segment Ideal Customer Profiles (ICPs).
3. **Competitive Moat Assessment**: Discover direct and indirect market incumbents and extract vulnerability gaps.
4. **SWOT & Execution Risk Matrix**: Identify internal strengths/weaknesses and external opportunities/threats with prioritized mitigation protocols.
5. **MoSCoW MVP Feature Scoping**: Synthesize prioritized Must-Have, Nice-to-Have, and Future Scale features to reduce time-to-market.
6. **Go-To-Market (GTM) Strategy**: Outline pricing models, customer acquisition channels, and phased launch milestones.
7. **Interactive AI Startup Advisor**: Provide a conversational chatbot for founders to interrogate the validation report and explore strategic options.
8. **Exportable PDF & Pitch Deck**: Generate instant downloadable executive PDF validation dossiers and 8-slide investor pitch decks.

---

## 🏗️ System Architecture & Workflow

The platform implements a sequential and cyclic state-machine architecture using **LangGraph**:

```
                  ┌───────────────────────────────┐
                  │    Startup Idea Submission    │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │   Idea Extraction Sub-Agent   │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │   Live Web Research Agent     │
                  │     (DuckDuckGo SERP API)     │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │ Market Analysis & TAM Agent   │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │  Competitor Discovery Agent   │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │  SWOT & Risk Modeling Agent   │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │    MVP Recommendation Agent   │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │    GTM Strategy Generation    │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │   Validation Report Compiler  │
                  └───────────────┬───────────────┘
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
┌──────────────────┐                              ┌──────────────────┐
│ PDF Report Export│                              │ AI Advisor Chat  │
└──────────────────┘                              └──────────────────┘
```

---

## 🤖 Multi-Agent Specifications

| # | Specialized Agent | Primary Role & Intelligence Output |
|---|---|---|
| **01** | **Idea Extraction Agent** | Parses freeform user ideas into structured attributes: problem, solution, target persona, and business model. |
| **02** | **Web Search Agent** | Dynamically synthesizes search queries, queries DuckDuckGo, and filters live SERP data. |
| **03** | **Market Opportunity Agent** | Evaluates market trends, macro growth trajectory, and customer segmentation. |
| **04** | **Competitor Intelligence Agent** | Uncovers market players, analyzes incumbent strengths, and maps vulnerability gaps. |
| **05** | **SWOT & Risk Agent** | Compiles 4-quadrant SWOT matrix and models execution risks with severity ratings and mitigations. |
| **06** | **MVP Scoping Agent** | Applies MoSCoW prioritization to identify minimum viable feature sets to test product-market fit. |
| **07** | **GTM Strategy Agent** | Recommends customer acquisition channels (PLG, outbound, SEO), pricing strategy, and launch sequence. |
| **08** | **Report Compiler Agent** | Computes the overall feasibility score (0–100) and compiles executive summary dossiers. |
| **09** | **Conversational Advisor** | RAG-grounded conversational agent answering dynamic follow-up questions regarding the report. |

---

## 🛠️ Technology Stack

- **Primary Language**: Python 3.11+
- **Multi-Agent Orchestration**: LangGraph, LangChain Core
- **LLM Reasoning**: Google Gemini API (`gemini-2.5-flash`, `gemini-1.5-flash`)
- **Live Search Tooling**: DuckDuckGo Search API (`duckduckgo-search`)
- **User Interface**: Streamlit (Reactive Python Web Framework)
- **Data Modeling**: Pydantic v2 schemas
- **Document Exporting**: FPDF2 (PDF Report Generator)
- **Data Visualization**: Altair, Pandas

---

## 📁 Repository Structure

```text
ai-startup-validator/
├── app/                      # Application entrypoints & configuration
│   ├── config.py             # System configuration & environment loaders
│   └── orchestrator.py       # High-level pipeline wrappers
│
├── agents/                   # Autonomous agent implementations
│   ├── idea_extraction_agent.py
│   ├── web_search_agent.py
│   ├── market_analysis_agent.py
│   ├── competitor_agent.py
│   ├── swot_risk_agent.py
│   ├── mvp_recommendation_agent.py
│   ├── gtm_strategy_agent.py
│   ├── report_agent.py
│   └── conversational_advisor.py
│
├── pipeline/                 # LangGraph state machine definition
│   ├── graph.py              # Node bindings, edge routing & graph compilation
│   └── context_passer.py     # State context transfer utilities
│
├── state/                    # Typed Pydantic data schemas
│   ├── schema.py             # GraphState and agent input/output models
│   └── memory.py             # In-memory session tracking
│
├── tools/                    # Tool definitions for LLM invocation
│   ├── web_search_tool.py    # DuckDuckGo live search wrapper
│   ├── pdf_exporter.py       # PDF & Markdown document generation
│   └── retrieval_utils.py    # Text parsing & normalization helpers
│
├── ui/                       # Streamlit web frontend
│   ├── streamlit_app.py      # Main application page & sidebar
│   └── components/
│       ├── idea_input.py     # Startup parameters submission form
│       ├── processing_page.py# Live execution progress visualizer
│       └── report_viewer.py  # Structured report tabs, charts & chat
│
├── docs/                     # Technical documentation & viva prep
│   ├── architecture.md       # High-level & low-level design
│   ├── agent_roles.md        # Detailed prompt & role breakdown
│   ├── final_report.md       # Project report reference
│   └── VIVA_PREPARATION.md   # Complete Viva Q&A Guide
│
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variable template
└── LICENSE                   # MIT Open Source License
```

---

## ⚡ Setup & Execution Guide

### 1. Prerequisites
- Python 3.11, 3.12, or 3.13 installed
- Google Gemini API Key (obtainable free from [Google AI Studio](https://aistudio.google.com/))

### 2. Virtual Environment Setup
```bash
# Clone or navigate to the project directory
cd ai-startup-validator

# Create and activate virtual environment
python -m venv .venv

# On Windows:
.\.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create a `.env` file in the root directory (or enter the key directly in the UI sidebar):
```env
GEMINI_API_KEY=your_gemini_api_key_here
SEARCH_ENGINE=duckduckgo
MAX_RESULTS=5
LOG_LEVEL=INFO
```

### 5. Run the Application
```bash
streamlit run ui/streamlit_app.py
```
Open your browser at `http://localhost:8501` to access the validator.

---

## 🎓 Academic Submission Details

- **Project Title**: Autonomous Multi-Agent AI Startup Idea Validator
- **Domain**: Artificial Intelligence / Multi-Agent Systems / NLP
- **Project Type**: Final Year Capstone Project

