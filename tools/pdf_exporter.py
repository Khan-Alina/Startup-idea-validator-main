import io
from fpdf import FPDF

def sanitize_text(text: str) -> str:
    """Sanitize text to be compatible with latin-1 for standard PDF fonts."""
    if not text:
        return ""
    # Map common unicode symbols to clean ASCII equivalents
    replacements = {
        "•": "-",
        "✓": "[OK]",
        "✔": "[OK]",
        "❌": "[X]",
        "✗": "[X]",
        "🚀": ">",
        "⚡": "*",
        "💡": "*",
        "🎯": "*",
        "★": "*",
        "⊙": "*",
        "’": "'",
        "‘": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2022": "-",
    }
    for orig, rep in replacements.items():
        text = text.replace(orig, rep)
    
    # Fallback encode to latin-1
    return text.encode("latin-1", "replace").decode("latin-1")


class StartupValidationPDF(FPDF):
    def __init__(self, startup_name="Startup"):
        super().__init__()
        self.startup_name = sanitize_text(startup_name)
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, f"AI STARTUP IDEA VALIDATOR // REPORT: {self.startup_name.upper()}", border=0, ln=True, align="L")
        self.set_draw_color(180, 180, 180)
        self.line(10, 16, 200, 16)
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}} - Autonomous Multi-Agent Feasibility Evaluation", 0, 0, "C")

    def section_heading(self, title: str):
        self.ln(4)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(30, 41, 59) # Slate 800
        self.set_fill_color(241, 245, 249) # Slate 100
        self.cell(0, 8, f"  {sanitize_text(title)}", ln=True, fill=True)
        self.ln(2)

    def sub_heading(self, subtitle: str):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(71, 85, 105)
        self.cell(0, 6, sanitize_text(subtitle), ln=True)

    def body_paragraph(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(51, 65, 85)
        self.multi_cell(0, 5, sanitize_text(text))
        self.ln(2)

    def bullet_item(self, bold_prefix: str, text: str):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(30, 41, 59)
        clean_prefix = sanitize_text(bold_prefix)
        clean_text = sanitize_text(str(text))
        self.write(5, f"- {clean_prefix} ")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(71, 85, 105)
        self.write(5, f"{clean_text}\n")
        self.ln(1)


def generate_pdf_report(idea: dict, results: dict, report: dict) -> bytes:
    """Generate a clean, structured PDF report and return as bytes."""
    startup_name = idea.get("startup_name") or "Startup Idea"
    industry = idea.get("industry") or "Technology"
    business_model = idea.get("business_model") or "B2B SaaS"
    score = report.get("final_validation_score", results.get("final_validation_score", 80))

    pdf = StartupValidationPDF(startup_name=startup_name)

    # Document Title Block
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, sanitize_text(startup_name), ln=True)

    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 6, sanitize_text(f"Industry: {industry}  |  Business Model: {business_model}"), ln=True)
    pdf.ln(2)

    # Validation Score Highlight Box
    pdf.set_fill_color(238, 242, 255) # Indigo 50
    pdf.set_draw_color(99, 102, 241) # Indigo 500
    pdf.rect(10, pdf.get_y(), 190, 16, style="DF")
    pdf.set_y(pdf.get_y() + 3)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(67, 56, 202)
    pdf.cell(100, 10, f"  Validation Score: {score}/100", ln=False)
    pdf.set_font("Helvetica", "I", 9)
    status_label = "High Viability" if score >= 75 else ("Moderate Viability" if score >= 50 else "High Risk")
    pdf.cell(85, 10, f"Tier: {status_label} (In-House ML Model)  ", ln=True, align="R")
    pdf.ln(6)

    # 1. Executive Summary
    pdf.section_heading("1. Executive Opportunity Summary")
    exec_sum = report.get("executive_summary") or results.get("executive_summary") or "Comprehensive multi-agent evaluation completed."
    pdf.body_paragraph(exec_sum)

    # Problem & Solution
    if idea.get("problem"):
        pdf.sub_heading("Core Problem Statement:")
        pdf.body_paragraph(idea.get("problem"))
    if idea.get("solution"):
        pdf.sub_heading("Proposed Solution:")
        pdf.body_paragraph(idea.get("solution"))

    # 2. Market Analysis
    pdf.section_heading("2. Market Opportunity & Sizing")
    market = report.get("market_analysis") or results.get("market_analysis", {})
    if isinstance(market, dict):
        if market.get("market_size"):
            pdf.bullet_item("Market Size & TAM:", market.get("market_size"))
        if market.get("target_audience"):
            pdf.bullet_item("Target Customer Segment:", market.get("target_audience"))
        if market.get("industry_trends"):
            pdf.bullet_item("Industry Macro Trends:", market.get("industry_trends"))
        if market.get("opportunities"):
            pdf.bullet_item("Identified Opportunities:", market.get("opportunities"))

    # 3. Competitor Analysis
    pdf.section_heading("3. Competitor Intelligence & Benchmarking")
    comp_data = report.get("competitor_analysis") or results.get("competitor_analysis", {})
    competitors = comp_data.get("competitors", []) if isinstance(comp_data, dict) else (comp_data if isinstance(comp_data, list) else [])

    if competitors:
        for idx, comp in enumerate(competitors[:4], 1):
            if hasattr(comp, "model_dump"):
                comp = comp.model_dump()
            if isinstance(comp, dict):
                c_name = comp.get("name", f"Competitor {idx}")
                c_web = comp.get("website", "N/A")
                c_desc = comp.get("description", "Incumbent player")
                pdf.sub_heading(f"{idx}. {c_name} ({c_web})")
                pdf.body_paragraph(f"Overview: {c_desc}")
                strengths = ", ".join(comp.get("strengths", []))
                weaknesses = ", ".join(comp.get("weaknesses", []))
                if strengths:
                    pdf.bullet_item("Strengths:", strengths)
                if weaknesses:
                    pdf.bullet_item("Vulnerability Gaps:", weaknesses)
                pdf.ln(1)
    else:
        pdf.body_paragraph("No direct incumbents detected during search queries. Suggests first-mover potential.")

    # 4. SWOT & Risk Matrix
    pdf.section_heading("4. SWOT & Risk Matrix")
    swot = report.get("swot_analysis") or results.get("swot_analysis", {})
    if isinstance(swot, dict):
        for s in swot.get("strengths", []):
            pdf.bullet_item("Strength (Internal):", s)
        for w in swot.get("weaknesses", []):
            pdf.bullet_item("Weakness (Internal):", w)
        for o in swot.get("opportunities", []):
            pdf.bullet_item("Opportunity (External):", o)
        for t in swot.get("threats", []):
            pdf.bullet_item("Threat (External):", t)

        risks = swot.get("risks", [])
        if risks:
            pdf.ln(2)
            pdf.sub_heading("Execution Risk Mitigation:")
            for r in risks:
                if isinstance(r, dict):
                    pdf.bullet_item(f"Risk [{r.get('severity', 'Med')}]:", f"{r.get('risk', '')} -> Mitigation: {r.get('mitigation', '')}")

    # 5. MVP Feature Recommendations
    pdf.section_heading("5. MVP Feature Roadmap (MoSCoW Prioritization)")
    mvp = report.get("mvp_recommendation") or results.get("mvp_recommendation", {})
    if isinstance(mvp, dict):
        must = mvp.get("must_have", [])
        if must:
            pdf.sub_heading("Must-Have Core MVP Features (Phase 1):")
            for item in must:
                if isinstance(item, dict):
                    pdf.bullet_item(item.get("feature", "Feature"), f"Rationale: {item.get('reason', '')} | KPI: {item.get('validation_goal', '')}")
                else:
                    pdf.bullet_item("Core Feature:", str(item))
        nice = mvp.get("nice_to_have", [])
        if nice:
            pdf.sub_heading("Nice-To-Have Features (Phase 2):")
            for item in nice:
                text = item.get("feature") if isinstance(item, dict) else str(item)
                pdf.bullet_item("Phase 2 Feature:", text)

    # 6. Go-To-Market Strategy
    pdf.section_heading("6. Go-To-Market & Launch Roadmap")
    gtm = report.get("gtm_strategy") or results.get("gtm_strategy", {})
    if isinstance(gtm, dict):
        if gtm.get("positioning_strategy"):
            pdf.bullet_item("Positioning:", gtm.get("positioning_strategy"))
        for p in gtm.get("pricing_ideas", []):
            if isinstance(p, dict):
                pdf.bullet_item("Pricing Model:", f"{p.get('model')}: {p.get('reason')}")
        for c in gtm.get("customer_acquisition_channels", []):
            if isinstance(c, dict):
                pdf.bullet_item("Acquisition Channel:", f"{c.get('channel')}: {c.get('reason')}")
        for step in gtm.get("launch_strategy", []):
            pdf.bullet_item("Launch Step:", str(step))

    # Output to in-memory bytes
    return bytes(pdf.output())


def generate_markdown_report(idea: dict, results: dict, report: dict) -> str:
    """Format the validation results into an academic Markdown document."""
    startup_name = idea.get("startup_name") or "Startup Idea"
    score = report.get("final_validation_score", results.get("final_validation_score", 80))
    exec_sum = report.get("executive_summary") or results.get("executive_summary") or "N/A"
    
    md = [
        f"# Startup Feasibility Validation Report: {startup_name}",
        f"**Domain:** {idea.get('industry', 'N/A')} | **Business Model:** {idea.get('business_model', 'N/A')}",
        f"**Validation Score:** {score}/100",
        "",
        "## 1. Executive Summary",
        exec_sum,
        "",
        "### Problem & Solution",
        f"- **Problem:** {idea.get('problem', 'N/A')}",
        f"- **Solution:** {idea.get('solution', 'N/A')}",
        f"- **Target Persona:** {idea.get('target_audience', 'N/A')}",
        "",
        "## 2. Market Opportunity Analysis"
    ]
    
    market = report.get("market_analysis") or results.get("market_analysis", {})
    if isinstance(market, dict):
        md.append(f"- **TAM & Market Sizing:** {market.get('market_size', 'N/A')}")
        md.append(f"- **Target Audience Profile:** {market.get('target_audience', 'N/A')}")
        md.append(f"- **Macro Industry Trends:** {market.get('industry_trends', 'N/A')}")
        md.append(f"- **Growth Opportunities:** {market.get('opportunities', 'N/A')}")
    
    md.extend(["", "## 3. Competitor Intelligence & Feature Gaps"])
    comp_data = report.get("competitor_analysis") or results.get("competitor_analysis", {})
    competitors = comp_data.get("competitors", []) if isinstance(comp_data, dict) else (comp_data if isinstance(comp_data, list) else [])
    for idx, c in enumerate(competitors, 1):
        if hasattr(c, "model_dump"):
            c = c.model_dump()
        if isinstance(c, dict):
            md.append(f"### {idx}. {c.get('name', 'Competitor')} ({c.get('website', 'N/A')})")
            md.append(f"{c.get('description', '')}")
            md.append(f"- **Strengths:** {', '.join(c.get('strengths', []))}")
            md.append(f"- **Vulnerabilities:** {', '.join(c.get('weaknesses', []))}")
    
    md.extend(["", "## 4. SWOT Matrix & Execution Risks"])
    swot = report.get("swot_analysis") or results.get("swot_analysis", {})
    if isinstance(swot, dict):
        md.append("### Strengths & Opportunities")
        for s in swot.get("strengths", []): md.append(f"- [+] {s}")
        for o in swot.get("opportunities", []): md.append(f"- [+] {o}")
        md.append("### Weaknesses & Threats")
        for w in swot.get("weaknesses", []): md.append(f"- [-] {w}")
        for t in swot.get("threats", []): md.append(f"- [-] {t}")
        
        md.append("### Execution Risk Mitigations")
        for r in swot.get("risks", []):
            if isinstance(r, dict):
                md.append(f"- **[{r.get('severity', 'Medium')} Risk]** {r.get('risk', '')} -> *Mitigation:* {r.get('mitigation', '')}")

    md.extend(["", "## 5. MVP Feature Recommendations (MoSCoW Prioritization)"])
    mvp = report.get("mvp_recommendation") or results.get("mvp_recommendation", {})
    if isinstance(mvp, dict):
        md.append("### Must-Have Core MVP Features (Phase 1)")
        for item in mvp.get("must_have", []):
            if isinstance(item, dict):
                md.append(f"- **{item.get('feature')}:** {item.get('reason')} (Validation Goal: `{item.get('validation_goal')}`)")
            else:
                md.append(f"- {item}")
        
        md.append("### Nice-to-Have Features (Phase 2)")
        for item in mvp.get("nice_to_have", []):
            md.append(f"- {item.get('feature') if isinstance(item, dict) else str(item)}")

    md.extend(["", "## 6. Go-To-Market Strategy & Launch Timeline"])
    gtm = report.get("gtm_strategy") or results.get("gtm_strategy", {})
    if isinstance(gtm, dict):
        md.append(f"**Positioning:** {gtm.get('positioning_strategy', 'N/A')}\n")
        md.append("### Pricing Strategy")
        for p in gtm.get("pricing_ideas", []):
            md.append(f"- **{p.get('model') if isinstance(p, dict) else p}:** {p.get('reason') if isinstance(p, dict) else ''}")
        md.append("### Customer Acquisition Channels")
        for c in gtm.get("customer_acquisition_channels", []):
            md.append(f"- **{c.get('channel') if isinstance(c, dict) else c}:** {c.get('reason') if isinstance(c, dict) else ''}")
        md.append("### Launch Steps")
        for step in gtm.get("launch_strategy", []):
            md.append(f"1. {step}")

    return "\n".join(md)


def generate_pitch_deck(idea: dict, results: dict, report: dict) -> list:
    """Generate an 8-slide investor pitch deck structure."""
    name = idea.get("startup_name", "Startup")
    industry = idea.get("industry", "Technology")
    problem = idea.get("problem", "Market friction identified.")
    solution = idea.get("solution", "Automated intelligent solution.")
    market = report.get("market_analysis") or results.get("market_analysis", {})
    market_size = market.get("market_size", "$10B+ TAM opportunity") if isinstance(market, dict) else "$10B+ TAM"
    mvp = report.get("mvp_recommendation") or results.get("mvp_recommendation", {})
    gtm = report.get("gtm_strategy") or results.get("gtm_strategy", {})

    slides = [
        {
            "slide_num": 1,
            "title": f"Slide 1: Title & Vision",
            "bullets": [
                f"Company: {name}",
                f"Tagline: The next-generation platform for {industry}",
                f"Target Audience: {idea.get('target_audience', 'Founders & Innovators')}",
                f"Validated Feasibility Score: {report.get('final_validation_score', 80)}/100"
            ],
            "speaker_notes": f"Introduce {name} and hook the audience with the core mission and validated opportunity."
        },
        {
            "slide_num": 2,
            "title": "Slide 2: The Core Problem",
            "bullets": [
                f"Pain Point: {problem}",
                "Existing methods are slow, manual, expensive, and uncoordinated.",
                "Target users lose weeks of productive capacity overcoming this bottleneck."
            ],
            "speaker_notes": "Emphasize the acute friction and emotional/financial cost of leaving this problem unsolved."
        },
        {
            "slide_num": 3,
            "title": "Slide 3: The Solution",
            "bullets": [
                f"Value Proposition: {solution}",
                "Automates end-to-end workflows with intelligent multi-agent reasoning.",
                "Delivers 10x faster execution compared to incumbent manual alternatives."
            ],
            "speaker_notes": "Present your solution as the inevitable evolution of the industry."
        },
        {
            "slide_num": 4,
            "title": "Slide 4: Market Opportunity (TAM/SAM)",
            "bullets": [
                f"Estimated Market: {market_size}",
                f"Target Sector: {industry} experiencing strong tailwinds and digital transformation.",
                f"Target Buyer Profile: {market.get('target_audience', idea.get('target_audience', 'Modern SMBs and Tech Leads'))}"
            ],
            "speaker_notes": "Demonstrate that the addressable market is large enough to build a venture-scale business."
        },
        {
            "slide_num": 5,
            "title": "Slide 5: Core Product & MVP Roadmap",
            "bullets": [
                "Prioritized MoSCoW Product Scoping:",
                f"• Must-Have MVP: Core automated workflow engine & analytics",
                f"• Nice-to-Have (Phase 2): Extended API integrations and collaboration tools",
                f"• Future: Enterprise multi-tenancy and continuous intelligence monitoring"
            ],
            "speaker_notes": "Show investors that you have a disciplined execution roadmap that avoids scope creep."
        },
        {
            "slide_num": 6,
            "title": "Slide 6: Business & Revenue Model",
            "bullets": [
                f"Primary Model: {idea.get('business_model', 'B2B SaaS Subscription')}",
                "Freemium / Product-Led Growth for viral user onboarding",
                "Tiered recurring subscription for professional & enterprise features",
                "High gross margins characteristic of software platforms"
            ],
            "speaker_notes": "Explain how each user converts into predictable recurring cash flow."
        },
        {
            "slide_num": 7,
            "title": "Slide 7: Competitive Advantage & Moat",
            "bullets": [
                "Direct competitors suffer from legacy UX, high pricing, or slow cycle times.",
                "Our Moat: Real-time autonomous synthesis, self-service onboarding, and high data accuracy.",
                "Positioning: First-mover advantage in specialized automation."
            ],
            "speaker_notes": "Convince investors why incumbents cannot easily squash or copy your specific advantage."
        },
        {
            "slide_num": 8,
            "title": "Slide 8: Go-To-Market & The Ask",
            "bullets": [
                "GTM Channels: Product-Led Growth (PLG), Targeted Community Outreach, Developer Inbound SEO",
                "Milestone 1: Closed alpha with 15 design partners (Weeks 1-4)",
                "Milestone 2: Public beta and Product Hunt launch (Weeks 5-8)",
                "The Ask: Looking for seed capital / advisory partners to accelerate development."
            ],
            "speaker_notes": "Close with a concrete ask, clear timeline milestones, and expected ROI."
        }
    ]
    return slides
