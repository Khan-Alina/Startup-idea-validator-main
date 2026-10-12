import os
import sys
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

# Lazy-loaded page components below for ultra-fast instant startup

st.set_page_config(
    page_title="IdeaValidator.ai — Autonomous Startup Idea Validation & ML Feasibility",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject exact Vesper.ai typography, fluid video background, liquid metal pills, and layout
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Instrument+Serif:ital@1&display=swap');

/* 1. Force Pure Pitch Black Immediately */
html {
    scroll-behavior: smooth !important;
}
html, body {
    background: #000000 !important;
    background-color: #000000 !important;
    color: #ffffff !important;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
    background-color: transparent !important;
}

.stApp {
    background: transparent !important;
    color: #ffffff !important;
    font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

/* 2. Fluid Video Background (The luminous white particle ribbon) */
.vesper-video-bg {
    position: fixed;
    top: 50%;
    left: 50%;
    min-width: 100vw;
    min-height: 100vh;
    width: 100vw;
    height: 100vh;
    transform: translate(-50%, -50%);
    object-fit: cover;
    z-index: -1 !important;
    pointer-events: none !important;
    opacity: 0.88 !important;
}

/* Ensure content sits cleanly above video */
[data-testid="stMainBlockContainer"], .block-container {
    position: relative !important;
    z-index: 5 !important;
    max-width: 1200px !important;
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
}

/* Remove header layer completely - pure transparent & seamless */
header[data-testid="stHeader"] {
    background: transparent !important;
    background-color: transparent !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    border: none !important;
    border-bottom: none !important;
    box-shadow: none !important;
    pointer-events: none !important; /* CRITICAL: Header won't intercept clicks to sidebar */
    z-index: 99 !important;
}

/* Completely remove Deploy button & Streamlit header decoration */
[data-testid="stDeployButton"],
div[data-testid="stDeployButton"],
button[data-testid="stDeployButton"],
.stDeployButton,
[data-testid="stAppDeployButton"],
[data-testid="stToolbarActions"],
[data-testid="stHeaderActionElements"],
[data-testid="stDecoration"],
[data-testid="manage-app-button"],
div[class*="viewerBadge"],
div[data-testid="stStatusWidget"],
footer,
#MainMenu {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

/* Replace double chevron (>>) with a simple crisp hamburger icon */
[data-testid="stExpandSidebarButton"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    background: transparent !important;
    top: 12px !important;
    left: 14px !important;
    z-index: 100 !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    pointer-events: auto !important;
}

[data-testid="stExpandSidebarButton"] button,
[data-testid="stSidebarCollapsedControl"] button,
[data-testid="collapsedControl"] button {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: #ffffff !important;
    width: 36px !important;
    height: 36px !important;
    padding: 6px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    position: relative !important;
    pointer-events: auto !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 101 !important;
}

[data-testid="stExpandSidebarButton"] button:focus,
[data-testid="stSidebarCollapsedControl"] button:focus,
[data-testid="collapsedControl"] button:focus {
    outline: none !important;
    box-shadow: none !important;
}

/* Hide ONLY children inside the expand button */
[data-testid="stExpandSidebarButton"] button > *,
[data-testid="stSidebarCollapsedControl"] button > *,
[data-testid="collapsedControl"] button > * {
    visibility: hidden !important;
    font-size: 0 !important;
    opacity: 0 !important;
    width: 0 !important;
    height: 0 !important;
    pointer-events: none !important;
}

/* Render clean simple hamburger icon (3 horizontal lines) */
[data-testid="stExpandSidebarButton"] button::before,
[data-testid="stSidebarCollapsedControl"] button::before,
[data-testid="collapsedControl"] button::before {
    content: "" !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    width: 22px !important;
    height: 16px !important;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23ffffff' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='3' y1='5' x2='21' y2='5'%3E%3C/line%3E%3Cline x1='3' y1='12' x2='21' y2='12'%3E%3C/line%3E%3Cline x1='3' y1='19' x2='21' y2='19'%3E%3C/line%3E%3C/svg%3E") !important;
    background-repeat: no-repeat !important;
    background-position: center !important;
    background-size: contain !important;
    visibility: visible !important;
    opacity: 1 !important;
    transition: opacity 0.2s ease, transform 0.2s ease !important;
    pointer-events: none !important;
}

[data-testid="stExpandSidebarButton"] button:hover::before,
[data-testid="stSidebarCollapsedControl"] button:hover::before,
[data-testid="collapsedControl"] button:hover::before {
    opacity: 0.75 !important;
    transform: translate(-50%, -50%) scale(1.08) !important;
}

/* Sidebar Header and Collapse Button (replaces << with a sleek Cross / Close ✕ icon) */
[data-testid="stSidebarHeader"] {
    background: transparent !important;
    position: relative !important;
    z-index: 1001 !important;
    pointer-events: auto !important;
}

[data-testid="stSidebarCollapseButton"] {
    background: transparent !important;
    position: relative !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    z-index: 1002 !important;
    pointer-events: auto !important;
    width: 38px !important;
    height: 38px !important;
}

[data-testid="stSidebarCollapseButton"] button {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: #ffffff !important;
    width: 38px !important;
    height: 38px !important;
    padding: 6px !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    position: relative !important;
    pointer-events: auto !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 1003 !important;
}

/* Hide ONLY children inside the collapse button */
[data-testid="stSidebarCollapseButton"] button > * {
    visibility: hidden !important;
    font-size: 0 !important;
    opacity: 0 !important;
    width: 0 !important;
    height: 0 !important;
    pointer-events: none !important;
}

/* Inject sleek Cross ✕ SVG icon */
[data-testid="stSidebarCollapseButton"] button::before {
    content: "" !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    width: 18px !important;
    height: 18px !important;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23ffffff' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E") !important;
    background-repeat: no-repeat !important;
    background-position: center !important;
    background-size: contain !important;
    visibility: visible !important;
    opacity: 0.9 !important;
    transition: opacity 0.2s ease, transform 0.2s ease !important;
    pointer-events: none !important;
}

[data-testid="stSidebarCollapseButton"] button:hover::before {
    opacity: 1 !important;
    transform: translate(-50%, -50%) rotate(90deg) scale(1.1) !important;
}

/* 3. Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: rgba(5, 5, 5, 0.92) !important;
    backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.12) !important;
    z-index: 1000 !important;
    pointer-events: auto !important;
}
section[data-testid="stSidebar"] * {
    color: #d8d8d8 !important;
    font-family: "Inter", sans-serif !important;
}
section[data-testid="stSidebar"] h1, 
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] h3, 
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] strong {
    color: #ffffff !important;
}

/* 4. Top Header Bar Navigation */
div[data-testid="stHorizontalBlock"]:has(button[data-testid="stBaseButton-secondary"]) {
    align-items: center !important;
    padding: 6px 0 16px 0 !important;
    margin-bottom: 25px !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
}
div[data-testid="stHorizontalBlock"]:has(button[data-testid="stBaseButton-secondary"]) div[data-testid="column"] {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
div[data-testid="stHorizontalBlock"]:has(button[data-testid="stBaseButton-secondary"]) div[data-testid="column"]:first-child {
    justify-content: flex-start !important;
}

.vesper-nav-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 0 25px 0;
    margin-bottom: 20px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.vesper-logo {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    font-size: 16px;
    font-weight: 600;
    letter-spacing: -0.03em;
    color: #ffffff;
}
.vesper-pills {
    display: flex;
    align-items: center;
    gap: 8px;
}
.liquid-pill {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 38px;
    padding: 0 18px;
    border-radius: 7px;
    border: 1px solid rgba(198, 198, 198, 0.55);
    background: linear-gradient(105deg, #050505 0%, #2a2a2a 48%, #4a4a4a 100%);
    color: #f3f3f3;
    font-size: 13.5px;
    font-weight: 400;
    letter-spacing: -0.01em;
    text-decoration: none;
    box-shadow: 0 0 14px rgba(0, 0, 0, 0.5);
    transition: all 0.35s ease;
}
.liquid-pill:hover {
    border-color: rgba(235, 235, 235, 0.9);
    background: linear-gradient(105deg, #111 0%, #3a3a3a 45%, #6a6a6a 100%);
    box-shadow: 0 0 18px rgba(200, 210, 230, 0.25);
    color: #ffffff;
    transform: translateY(-1px);
}

/* 5. Vesper Hero Elements */
.vesper-badge-wrapper {
    display: flex;
    justify-content: center;
    margin-top: 35px;
    margin-bottom: 18px;
    position: relative !important;
    z-index: 10 !important;
}
.vesper-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 7px 16px;
    border-radius: 9999px;
    background: linear-gradient(90deg, #7d7d7d 0%, #2a2a2a 52%, #0a0a0a 100%);
    border: 1px solid rgba(255, 255, 255, 0.18);
    color: #f2f2f2;
    font-size: 12.5px;
    letter-spacing: -0.01em;
    box-shadow: 0 0 16px rgba(255, 255, 255, 0.08);
}
.vesper-headline {
    text-align: center;
    font-size: 54px;
    font-weight: 500;
    line-height: 1.12;
    letter-spacing: -0.045em;
    color: #ffffff;
    margin: 8px 0 16px 0;
    position: relative !important;
    z-index: 10 !important;
}
.vesper-headline em {
    font-family: "Instrument Serif", "Times New Roman", Times, serif;
    font-style: italic;
    font-weight: 400;
    font-size: 1.15em;
    color: #9a9a9a;
    letter-spacing: -0.025em;
}
.vesper-lede {
    text-align: center;
    font-size: 16px;
    line-height: 1.6;
    color: #9a9a9a;
    max-width: 560px;
    margin: 0 auto 30px auto;
    letter-spacing: -0.015em;
    position: relative !important;
    z-index: 10 !important;
}

/* 6. Buttons & Pills */
/* Primary Action Buttons (Hero: Start for Free, See it in action) */
button[data-testid="stBaseButton-primary"],
.stButton > button:not([data-testid="stBaseButton-secondary"]) {
    background: linear-gradient(180deg, #ffffff 0%, #e7e7e7 48%, #cfcfcf 100%) !important;
    color: #111111 !important;
    border: 1px solid #ffffff !important;
    border-radius: 6px !important;
    font-family: "Inter", sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    letter-spacing: -0.02em !important;
    padding: 12px 26px !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.95), 0 0 20px rgba(255, 255, 255, 0.15) !important;
    transition: all 0.35s ease !important;
    cursor: pointer !important;
}
button[data-testid="stBaseButton-primary"]:hover,
.stButton > button:not([data-testid="stBaseButton-secondary"]):hover {
    background: linear-gradient(180deg, #ffffff 0%, #f3f6ff 42%, #d5def2 100%) !important;
    border-color: #f2f6ff !important;
    box-shadow: inset 0 1px 0 #fff, 0 0 28px rgba(186,208,255,0.45), 0 8px 18px rgba(255,255,255,0.16) !important;
    color: #000000 !important;
    transform: translateY(-1px);
}

/* Secondary Buttons & Navbar Liquid-Metal Pills (Benefits, How It Works, FAQs, Pricing) */
button[data-testid="stBaseButton-secondary"],
.liquid-pill {
    height: 38px !important;
    padding: 0 16px !important;
    border-radius: 7px !important;
    border: 1px solid rgba(198, 198, 198, 0.55) !important;
    background: linear-gradient(105deg, #050505 0%, #2a2a2a 48%, #4a4a4a 100%) !important;
    color: #f3f3f3 !important;
    font-family: "Inter", sans-serif !important;
    font-size: 13.5px !important;
    font-weight: 400 !important;
    letter-spacing: -0.01em !important;
    box-shadow: 0 0 14px rgba(0, 0, 0, 0.5) !important;
    transition: all 0.35s ease !important;
    cursor: pointer !important;
    white-space: nowrap !important;
}
button[data-testid="stBaseButton-secondary"]:hover,
.liquid-pill:hover {
    border-color: rgba(235, 235, 235, 0.9) !important;
    background: linear-gradient(105deg, #111 0%, #3a3a3a 45%, #6a6a6a 100%) !important;
    box-shadow: 0 0 18px rgba(200, 210, 230, 0.25) !important;
    color: #ffffff !important;
    transform: translateY(-1px);
}

.stDownloadButton > button {
    background: linear-gradient(105deg, #050505 0%, #2a2a2a 48%, #4a4a4a 100%) !important;
    color: #f3f3f3 !important;
    border: 1px solid rgba(198, 198, 198, 0.55) !important;
    border-radius: 7px !important;
    font-family: "Inter", sans-serif !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    padding: 10px 20px !important;
    box-shadow: 0 0 14px rgba(0, 0, 0, 0.5) !important;
    transition: all 0.3s ease !important;
}
.stDownloadButton > button:hover {
    border-color: rgba(235, 235, 235, 0.9) !important;
    background: linear-gradient(105deg, #111 0%, #3a3a3a 45%, #6a6a6a 100%) !important;
    box-shadow: 0 0 18px rgba(200, 210, 230, 0.25) !important;
    color: #ffffff !important;
    transform: translateY(-1px) !important;
}

/* Dialog / Modal Styling (Benefits, How It Works, FAQs, Pricing) */
div[data-testid="stDialog"] > div {
    background: rgba(12, 12, 16, 0.96) !important;
    backdrop-filter: blur(28px) !important;
    -webkit-backdrop-filter: blur(28px) !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    border-radius: 14px !important;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8) !important;
    color: #ffffff !important;
}
div[data-testid="stDialog"] h1, 
div[data-testid="stDialog"] h2, 
div[data-testid="stDialog"] h3, 
div[data-testid="stDialog"] h4 {
    color: #ffffff !important;
}
div[data-testid="stDialog"] button[aria-label="Close"] {
    color: #ffffff !important;
}

/* 7. Input Fields & Sliders */
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div {
    background-color: rgba(9, 9, 11, 0.88) !important;
    backdrop-filter: blur(16px) !important;
    color: #f3f3f3 !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    border-radius: 6px !important;
    font-family: "Inter", sans-serif !important;
}
.stTextInput input:focus, .stTextArea textarea:focus, div[data-baseweb="select"] > div:focus-within {
    border-color: rgba(255, 255, 255, 0.7) !important;
    box-shadow: 0 0 16px rgba(255, 255, 255, 0.18) !important;
}

/* 8. Frosted Glass Panels & Content Cards */
.vesper-glass-panel {
    background: rgba(10, 10, 14, 0.85) !important;
    backdrop-filter: blur(28px) !important;
    -webkit-backdrop-filter: blur(28px) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 12px !important;
    padding: 24px !important;
    margin-bottom: 20px !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6) !important;
}

.vesper-glass-card {
    background: rgba(12, 12, 16, 0.85) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.11) !important;
    border-radius: 10px !important;
    padding: 18px !important;
    margin-bottom: 14px !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4) !important;
}

/* 9. Tabs Styling - Monochrome Silver Liquid Metal */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(10, 10, 14, 0.85) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 10px !important;
    padding: 6px 8px !important;
    gap: 6px !important;
}
.stTabs [data-baseweb="tab"] {
    color: #a1a1aa !important;
    font-family: "Inter", sans-serif !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    border-radius: 7px !important;
    padding: 8px 16px !important;
    border: 1px solid transparent !important;
    background: transparent !important;
    transition: all 0.25s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #ffffff !important;
    background: rgba(255, 255, 255, 0.06) !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.05) 100%) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.24) !important;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.5) !important;
}
.stTabs [data-baseweb="tab-highlight"] {
    background-color: transparent !important;
}
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* 10. Expanders & Callouts */
div[data-testid="stExpander"] {
    background: rgba(10, 10, 14, 0.85) !important;
    backdrop-filter: blur(18px) !important;
    -webkit-backdrop-filter: blur(18px) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 10px !important;
    margin-bottom: 14px !important;
}
div[data-testid="stExpander"] summary {
    color: #f4f4f5 !important;
    font-weight: 500 !important;
    font-size: 14px !important;
}
div[data-testid="stExpander"] summary:hover {
    color: #ffffff !important;
}

div[data-testid="stAlert"] {
    background: rgba(12, 12, 16, 0.88) !important;
    backdrop-filter: blur(18px) !important;
    -webkit-backdrop-filter: blur(18px) !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    border-radius: 8px !important;
    color: #e4e4e7 !important;
}
div[data-testid="stAlert"] * {
    color: #e4e4e7 !important;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #71717a 0%, #d4d4d8 50%, #ffffff 100%) !important;
}
.stProgress > div > div > div {
    background-color: rgba(255, 255, 255, 0.1) !important;
}

/* Chat Messages */
div[data-testid="stChatMessage"] {
    background: rgba(10, 10, 14, 0.85) !important;
    backdrop-filter: blur(18px) !important;
    -webkit-backdrop-filter: blur(18px) !important;
    border: 1px solid rgba(255, 255, 255, 0.11) !important;
    border-radius: 10px !important;
    margin-bottom: 12px !important;
    color: #f4f4f5 !important;
}

/* 11. Bottom Stats Row */
.vesper-stats-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    margin-top: 60px;
    padding: 20px 30px;
    background: rgba(8, 8, 10, 0.7);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    position: relative !important;
    z-index: 10 !important;
}
.vesper-stat-item {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    font-size: 13.5px;
    color: #d8d8d8;
    letter-spacing: -0.015em;
    white-space: nowrap;
}
/* 12. Benefits Grid */
.benefits-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin: 24px 0 50px 0;
    position: relative !important;
    z-index: 10 !important;
}
.benefit-card {
    background: rgba(12, 12, 16, 0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;
    padding: 24px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
}
.benefit-card:hover {
    border-color: rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6);
}
.benefit-icon-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 44px;
    height: 44px;
    border-radius: 10px;
    background: linear-gradient(135deg, #27272a 0%, #121215 100%);
    border: 1px solid rgba(255, 255, 255, 0.16);
    margin-bottom: 14px;
    font-size: 20px;
}
.benefit-title {
    font-size: 17px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 8px;
    letter-spacing: -0.02em;
}
.benefit-desc {
    font-size: 14px;
    color: #a1a1aa;
    line-height: 1.6;
}

/* 13. How It Works - OpenAI Architecture Diagram */
.how-container {
    margin: 24px 0 60px 0;
    padding: 32px 28px;
    background: rgba(8, 8, 12, 0.85);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 16px;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.7);
    position: relative !important;
    z-index: 10 !important;
}
.how-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 28px;
}
.how-col {
    display: flex;
    flex-direction: column;
}
.how-step-num {
    font-size: 11.5px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #71717a;
    margin-bottom: 4px;
}
.how-step-title {
    font-size: 16px;
    font-weight: 600;
    color: #ffffff;
    line-height: 1.35;
    margin-bottom: 16px;
    letter-spacing: -0.015em;
    min-height: 44px;
}
.how-step-desc {
    font-size: 13px;
    color: #9ca3af;
    line-height: 1.55;
    margin-bottom: 20px;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 8px;
    padding: 12px;
}
.how-flow-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}
.how-node {
    width: 100%;
    border-radius: 8px;
    padding: 12px 14px;
    font-size: 12.5px;
    text-align: center;
    box-sizing: border-box;
    transition: all 0.25s ease;
}
.how-node-prompt {
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.35);
    color: #34d399;
    font-size: 12px;
    font-style: italic;
    font-family: monospace;
}
.how-node-neutral {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.14);
    color: #f4f4f5;
    font-weight: 500;
}
.how-node-highlight {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.04) 100%);
    border: 1px solid rgba(255, 255, 255, 0.28);
    color: #ffffff;
    font-weight: 600;
    box-shadow: 0 0 16px rgba(255, 255, 255, 0.06);
}
.how-arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 24px;
    color: rgba(255, 255, 255, 0.4);
}
.how-subgrid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    width: 100%;
}
.how-subnode {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 6px;
    padding: 8px 10px;
    font-size: 11.5px;
    color: #e4e4e7;
    text-align: center;
}
.how-loop-back {
    margin-top: 12px;
    font-size: 11.5px;
    color: #a1a1aa;
    text-align: center;
    padding: 8px;
    border-radius: 6px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px dashed rgba(255, 255, 255, 0.18);
    width: 100%;
    box-sizing: border-box;
}

/* 14. FAQs Section - Inspired by Image 1 */
.faq-section {
    margin: 24px 0 80px 0;
    position: relative !important;
    z-index: 10 !important;
}
.faq-pair {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 24px;
}
.faq-user-card {
    background: #18181b;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 10px;
    padding: 16px 20px;
}
.faq-ai-card {
    background: #0e0e12;
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 10px;
    padding: 20px 22px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
}
.faq-role {
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #71717a;
    margin-bottom: 6px;
    display: block;
}
.faq-ai-card .faq-role {
    color: #a1a1aa;
}
.faq-user-card p {
    margin: 0;
    color: #f4f4f5;
    font-size: 15px;
    font-weight: 500;
}
.faq-ai-card p {
    margin: 0;
    color: #d4d4d8;
    font-size: 14.5px;
    line-height: 1.65;
}
</style>

<!-- Live Undulating White Particle Wave Video Background (Cached locally for instant 0ms load) -->
<video autoplay loop muted playsinline preload="auto" class="vesper-video-bg">
    <source src="/app/static/background_wave.mp4" type="video/mp4">
    <source src="/static/background_wave.mp4" type="video/mp4">
    <source src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260818_072341_50851634-bbc3-4c33-9acc-7647d4db44aa.mp4" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# SIDEBAR CONFIGURATION
with st.sidebar:
    st.markdown("### ⚙️ IdeaValidator Console")
    st.markdown("""
    <div style="display:inline-flex; align-items:center; justify-content:center; width:52px; height:52px; border-radius:12px; background:linear-gradient(135deg, #27272a 0%, #121215 100%); border:1px solid rgba(255,255,255,0.18); box-shadow:0 0 20px rgba(255,255,255,0.08); margin: 6px 0 12px 0;">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 4.44-2.04"/>
            <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-4.44-2.04"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**IdeaValidator.ai**")
    st.caption("AI Startup Feasibility & Market Intelligence")

    st.divider()

    # Gemini API Key Entry
    existing_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
    user_api_key = st.text_input("🔑 Gemini API Key", value=existing_key, type="password", help="Enter your Gemini API key to run live DeepAgent web research & LLM analysis.")
    if user_api_key:
        os.environ["GEMINI_API_KEY"] = user_api_key
        os.environ["GOOGLE_API_KEY"] = user_api_key
        st.session_state.gemini_api_key = user_api_key
        st.success("API Key Active ✅")
    else:
        st.info("💡 Running with In-House Random Forest ML Model (Demo Mode ready).")

    st.divider()

    # AI Model Selector
    model_choice = st.selectbox("🧠 Select AI Engine", ["gemini-2.5-flash", "gemini-1.5-flash"], index=0)
    os.environ["STARTUP_VALIDATOR_MODEL"] = model_choice

    st.divider()
    st.markdown("#### ⚡ Active Autonomous Agents")
    st.markdown("""
    - 🔍 Web Search Agent
    - 📊 Market Analysis Agent
    - 🥊 Competitor Intelligence
    - 🛡️ SWOT & Risk Agent
    - ⚡ MVP Feature Agent
    - 🚀 GTM Strategy Agent
    - 📈 Report Generator
    - 💬 Conversational Advisor
    """)

    st.divider()
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


if "page" not in st.session_state:
    st.session_state.page = "home"

# HOME PAGE
if st.session_state.page == "home":
    # Top Header Navigation (No Pricing, Instant Smooth Scroll Links)
    st.html("""
<div class="vesper-nav-container">
    <div class="vesper-logo">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="#ffffff">
            <g transform="rotate(-30 12 12)">
                <circle cx="7.3" cy="3.2" r="1.45"/>
                <rect x="5.5" y="4.7" width="3.6" height="14.6" rx="1.8"/>
                <rect x="14.9" y="4.7" width="3.6" height="14.6" rx="1.8"/>
                <circle cx="16.7" cy="20.8" r="1.45"/>
            </g>
        </svg>
        <span>IdeaValidator<span style="font-weight:400; color:#9a9a9a;">.ai</span></span>
    </div>
    <div class="vesper-pills">
        <a href="#benefits" class="liquid-pill">Benefits</a>
        <a href="#how-it-works" class="liquid-pill">How It Works</a>
        <a href="#faqs" class="liquid-pill">FAQs</a>
    </div>
</div>
""")

    # IdeaValidator Metallic Sparkle Badge
    st.html("""
<div class="vesper-badge-wrapper">
    <div class="vesper-badge">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="#ffffff" style="filter: drop-shadow(0 0 3px rgba(255,255,255,0.45));">
            <path d="M12 2.6C12.55 2.6 12.88 3.15 13.08 4.7c.62 4.7 1.52 5.6 6.22 6.22 1.55.2 2.1.53 2.1 1.08s-.55.88-2.1 1.08c-4.7.62-5.6 1.52-6.22 6.22-.2 1.55-.53 2.1-1.08 2.1s-.88-.55-1.08-2.1c-.62-4.7-1.52-5.6-6.22-6.22C3.15 12.88 2.6 12.55 2.6 12s.55-.88 2.1-1.08c4.7-.62 5.6-1.52 6.22-6.22C11.12 3.15 11.45 2.6 12 2.6Z"/>
        </svg>
        <span>Autonomous Startup Idea Validation & ML Feasibility</span>
    </div>
</div>
""")

    # Dual-Line Headline with Instrument Serif Italic
    st.html("""
<h1 class="vesper-headline">
    Validate your <em>startup idea</em><br>
    before you build.
</h1>
<p class="vesper-lede">
    Autonomous AI agents research competitors, analyze market sizing, and predict startup success probability with an in-house Random Forest ML model.
</p>
""")

    # Action Buttons (Side by Side in Center)
    c_btn1, c_btn2, c_btn3, c_btn4 = st.columns([1.5, 1.2, 1.2, 1.5])
    with c_btn2:
        if st.button("Start for Free", use_container_width=True):
            st.session_state.page = "submit"
            st.rerun()
    with c_btn3:
        if st.button("See it in action", use_container_width=True):
            st.session_state.idea = {
                "startup_name": "MediScan AI",
                "industry": "Healthcare",
                "target_audience": "Diagnostic Labs, Clinics, and Radiologists",
                "business_model": "B2B",
                "problem": "Diagnostic clinics face severe radiologist shortages, delaying X-ray triage by 48-72 hours.",
                "solution": "Automated AI assistant analyzing medical radiology scans in real-time under 60 seconds."
            }
            st.session_state.page = "processing"
            st.rerun()

    # Project 3-Stat Bottom Row
    st.html("""
<div class="vesper-stats-footer">
    <div class="vesper-stat-item">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
            <rect x="3.4" y="2.6" width="7.2" height="18.8" rx="3.6" fill="rgba(255,255,255,0.4)"/>
            <rect x="13.4" y="2.6" width="7.2" height="18.8" rx="3.6" fill="rgba(255,255,255,0.85)"/>
            <rect x="9.2" y="10.9" width="5.6" height="2.2" rx="1.1" fill="#4a4a4a"/>
        </svg>
        <span>5,000+ Startups Trained</span>
    </div>
    <div class="vesper-stat-item">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
            <rect x="2.4" y="2.4" width="19.2" height="19.2" rx="6.2" fill="#ffffff"/>
            <path d="M12 7.1v7.4M8.15 12.35L12 16.2l3.85-3.85" stroke="#111111" stroke-width="1.85" stroke-linecap="round"/>
        </svg>
        <span>92.3% Empirical Prediction Accuracy</span>
    </div>
    <div class="vesper-stat-item">
        <svg width="36" height="20" viewBox="0 0 40 22" fill="none">
            <circle cx="10.2" cy="11" r="8" fill="#2b2b2b"/>
            <ellipse cx="10.2" cy="12.1" rx="4.15" ry="3.7" fill="#f4f4f4"/>
            <circle cx="20.2" cy="11" r="8" fill="#ffffff"/>
            <circle cx="30.2" cy="11" r="8" fill="#71717a"/>
            <text x="30.2" y="15.1" fill="#ffffff" font-family="Inter, sans-serif" font-weight="700" font-size="12" text-anchor="middle">7</text>
        </svg>
        <span>7 Autonomous Intelligence Agents</span>
    </div>
</div>
""")

    # =========================================================================
    # 1. PLATFORM BENEFITS SECTION (Directly in UI Column)
    # =========================================================================
    st.html("""
<div id="benefits" style="padding-top: 70px; text-align: center; position: relative; z-index: 10;">
    <span style="font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: #71717a;">Platform Advantages</span>
    <h2 style="font-size: 38px; font-weight: 600; color: #ffffff; letter-spacing: -0.035em; margin: 8px 0 14px 0;">Platform Benefits</h2>
    <p style="color: #9a9a9a; font-size: 16px; max-width: 640px; margin: 0 auto; line-height: 1.6;">
        IdeaValidator.ai combines autonomous multi-agent intelligence with an empirical scikit-learn machine learning model to stress-test your startup concept before you build.
    </p>
</div>

<div class="benefits-grid">
    <div class="benefit-card">
        <div class="benefit-icon-badge">⚡</div>
        <div class="benefit-title">Zero-Hallucination Scoring</div>
        <div class="benefit-desc">Dual-layer validation: LLM qualitative reasoning cross-referenced with an offline Random Forest model trained on 5,000+ real-world startups to eliminate optimistic bias.</div>
    </div>
    <div class="benefit-card">
        <div class="benefit-icon-badge">🔍</div>
        <div class="benefit-title">Autonomous Web Recon Swarm</div>
        <div class="benefit-desc">Deep web search agents discover stealth rivals, real-time pricing benchmarks, and trademark/patent pitfalls across global registries before you launch.</div>
    </div>
    <div class="benefit-card">
        <div class="benefit-icon-badge">🛡️</div>
        <div class="benefit-title">Predictive SWOT & Risk Engine</div>
        <div class="benefit-desc">Proactively highlights regulatory barriers, customer acquisition bottlenecks, unit economics flaws, and technical hurdles before spending capital.</div>
    </div>
    <div class="benefit-card">
        <div class="benefit-icon-badge">📈</div>
        <div class="benefit-title">Investor-Grade Deliverables</div>
        <div class="benefit-desc">Automatically synthesizes TAM/SAM/SOM market models, a 3-phase agile MVP roadmap, and exportable Markdown, JSON, and PDF executive dossiers.</div>
    </div>
</div>
""")

    # =========================================================================
    # 2. HOW IT WORKS - ARCHITECTURE DIAGRAM (Inspired by OpenAI RLHF)
    # =========================================================================
    st.html("""
<div id="how-it-works" style="padding-top: 70px; text-align: center; position: relative; z-index: 10;">
    <span style="font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: #71717a;">End-to-End Orchestration</span>
    <h2 style="font-size: 38px; font-weight: 600; color: #ffffff; letter-spacing: -0.035em; margin: 8px 0 14px 0;">How It Works</h2>
    <p style="color: #9a9a9a; font-size: 16px; max-width: 660px; margin: 0 auto; line-height: 1.6;">
        Architecture pipeline inspired by state-of-the-art multi-agent research and empirical machine learning models.
    </p>
</div>

<div class="how-container">
    <div class="how-grid">
        <!-- Column 1: Step 1 -->
        <div class="how-col">
            <span class="how-step-num">Step 1</span>
            <div class="how-step-title">Ingest demonstration data & parse hypothesis</div>
            <div class="how-step-desc">
                A founder's raw concept is parsed and normalized into structured problem, target audience, and business model entities.
            </div>
            <div class="how-flow-box">
                <div class="how-node how-node-prompt">
                    "AI co-pilot analyzing medical radiology scans in 60s for diagnostic clinics"
                </div>
                <div class="how-arrow">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none"><path d="M7 2v14m0 0l-4-4m4 4l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="how-node how-node-neutral">
                    <div style="font-size: 18px; margin-bottom: 4px;">👤</div>
                    Founder Hypothesis Input
                </div>
                <div class="how-arrow">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none"><path d="M7 2v14m0 0l-4-4m4 4l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="how-node how-node-neutral">
                    <div style="font-size: 18px; margin-bottom: 4px;">⚙️</div>
                    Parameter Normalization Engine
                </div>
                <div class="how-arrow">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none"><path d="M7 2v14m0 0l-4-4m4 4l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="how-node how-node-highlight">
                    <div style="font-size: 18px; margin-bottom: 4px;">📄</div>
                    Standardized Hypothesis Vector
                </div>
            </div>
        </div>

        <!-- Column 2: Step 2 -->
        <div class="how-col">
            <span class="how-step-num">Step 2</span>
            <div class="how-step-title">Collect market recon & run multi-agent swarm</div>
            <div class="how-step-desc">
                7 autonomous agents execute simultaneously to gather live competitor pricing, market demand signals, and SWOT risks.
            </div>
            <div class="how-flow-box">
                <div class="how-node how-node-prompt">
                    Autonomous Multi-Agent Swarm Triggered
                </div>
                <div class="how-arrow">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none"><path d="M7 2v14m0 0l-4-4m4 4l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="how-subgrid">
                    <div class="how-subnode">🔍 Web Recon</div>
                    <div class="how-subnode">🥊 Competitor Intel</div>
                    <div class="how-subnode">🛡️ SWOT & Risk</div>
                    <div class="how-subnode">⚡ MVP Roadmap</div>
                </div>
                <div class="how-arrow">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none"><path d="M7 2v14m0 0l-4-4m4 4l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="how-node how-node-neutral">
                    <div style="font-size: 18px; margin-bottom: 4px;">🧠</div>
                    Multi-Agent Evidence Synthesizer
                </div>
                <div class="how-arrow">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none"><path d="M7 2v14m0 0l-4-4m4 4l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="how-node how-node-highlight">
                    <div style="font-size: 18px; margin-bottom: 4px;">📊</div>
                    Qualitative Intelligence Dossier
                </div>
            </div>
        </div>

        <!-- Column 3: Step 3 -->
        <div class="how-col">
            <span class="how-step-num">Step 3</span>
            <div class="how-step-title">Score empirical feasibility & optimize policy</div>
            <div class="how-step-desc">
                12 quantitative parameters feed into our Random Forest classifier, with continuous iterative tuning via the AI Advisor.
            </div>
            <div class="how-flow-box">
                <div class="how-node how-node-prompt">
                    12-Dimensional Feature Vector Extracted
                </div>
                <div class="how-arrow">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none"><path d="M7 2v14m0 0l-4-4m4 4l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="how-node how-node-neutral">
                    <svg width="26" height="22" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.6" style="margin: 0 auto 4px auto; display: block;">
                        <circle cx="12" cy="5" r="2.5"/>
                        <circle cx="5" cy="18" r="2.5"/>
                        <circle cx="19" cy="18" r="2.5"/>
                        <circle cx="12" cy="12" r="2"/>
                        <line x1="12" y1="7.5" x2="12" y2="10"/>
                        <line x1="10.5" y1="13.5" x2="6.5" y2="16.5"/>
                        <line x1="13.5" y1="13.5" x2="17.5" y2="16.5"/>
                    </svg>
                    Random Forest ML (5k+ Startups)
                </div>
                <div class="how-arrow">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none"><path d="M7 2v14m0 0l-4-4m4 4l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="how-node how-node-highlight">
                    <div style="font-size: 18px; margin-bottom: 4px;">🎯</div>
                    Score: 88% | Risk: Low Tier
                </div>
                <div class="how-arrow">
                    <svg width="14" height="20" viewBox="0 0 14 20" fill="none"><path d="M7 2v14m0 0l-4-4m4 4l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="how-node how-node-neutral">
                    <div style="font-size: 18px; margin-bottom: 4px;">💬</div>
                    Interactive Conversational Advisor
                </div>
                <div class="how-loop-back">
                    ⮑ Continuous iterative advisor loop to refine pitch
                </div>
            </div>
        </div>
    </div>
</div>
""")

    # =========================================================================
    # 3. FREQUENTLY ASKED QUESTIONS SECTION (Inspired by Image 1)
    # =========================================================================
    st.html("""
<div id="faqs" style="padding-top: 70px; text-align: center; position: relative; z-index: 10;">
    <span style="font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: #71717a;">Common Questions</span>
    <h2 style="font-size: 38px; font-weight: 600; color: #ffffff; letter-spacing: -0.035em; margin: 8px 0 14px 0;">Frequently Asked Questions</h2>
    <p style="color: #9a9a9a; font-size: 16px; max-width: 620px; margin: 0 auto; line-height: 1.6;">
        Answers to common questions regarding our evaluation methodology, offline ML mode, and security.
    </p>
</div>

<div class="faq-section">
    <!-- Q1 -->
    <div class="faq-pair">
        <div class="faq-user-card">
            <span class="faq-role">User</span>
            <p>How does IdeaValidator avoid AI bias and sycophancy?</p>
        </div>
        <div class="faq-ai-card">
            <span class="faq-role">IdeaValidator AI</span>
            <p>Standard LLMs tend to be overly agreeable ("sycophantic") to founder ideas. IdeaValidator breaks this by decoupling qualitative research from quantitative evaluation: while autonomous agents gather real-time web facts, an independent, offline Random Forest ML classifier trained on 5,000+ historical startup outcomes computes empirical success probability without subjective bias.</p>
        </div>
    </div>

    <!-- Q2 -->
    <div class="faq-pair">
        <div class="faq-user-card">
            <span class="faq-role">User</span>
            <p>Do I need an OpenAI or Gemini API key to run this?</p>
        </div>
        <div class="faq-ai-card">
            <span class="faq-role">IdeaValidator AI</span>
            <p>No. IdeaValidator includes a fully functional in-house Random Forest model (Demo Mode) that runs out of the box with zero external keys. If you wish to enable live autonomous web searching and custom reasoning, you can easily provide a free Google Gemini key in the sidebar console.</p>
        </div>
    </div>

    <!-- Q3 -->
    <div class="faq-pair">
        <div class="faq-user-card">
            <span class="faq-role">User</span>
            <p>Is my startup idea kept private and secure?</p>
        </div>
        <div class="faq-ai-card">
            <span class="faq-role">IdeaValidator AI</span>
            <p>100% yes. The application executes locally or inside your private session. Your startup hypotheses are never stored on public servers or used to train external public models.</p>
        </div>
    </div>

    <!-- Q4 -->
    <div class="faq-pair">
        <div class="faq-user-card">
            <span class="faq-role">User</span>
            <p>What tangible deliverables do I receive?</p>
        </div>
        <div class="faq-ai-card">
            <span class="faq-role">IdeaValidator AI</span>
            <p>Every analysis produces a complete investor-ready dossier: market sizing models (TAM/SAM/SOM), competitor feature matrix, predictive SWOT & risk grid, 3-phase technical MVP roadmap, and exportable Markdown, JSON, and PDF reports.</p>
        </div>
    </div>
</div>
""")

# SUBMIT IDEA PAGE
elif st.session_state.page == "submit":
    from ui.components.idea_input import show_idea_input
    show_idea_input()

# PROCESSING PAGE
elif st.session_state.page == "processing":
    from ui.components.processing_page import show_processing_page
    show_processing_page()

# REPORT PAGE
elif st.session_state.page == "report":
    from ui.components.report_viewer import show_report
    show_report()