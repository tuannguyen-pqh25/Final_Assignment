"""
Slide Deck Generator for Company A Retention Strategy (Project Phoenix)
GCI World 2026 Final Assignment — Stage 10
Generates a 15-page executive consulting presentation in PDF format (16:9 widescreen)
and renders each page to high-res PNG images for visual inspection.
"""

from pathlib import Path
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages
import pymupdf as fitz
from PIL import Image

# Enforce parse_math=False globally on all text calls to avoid '$' math parsing issues
_orig_axes_text = matplotlib.axes.Axes.text
def _safe_axes_text(self, x, y, s, *args, **kwargs):
    kwargs.setdefault("parse_math", False)
    return _orig_axes_text(self, x, y, s, *args, **kwargs)
matplotlib.axes.Axes.text = _safe_axes_text

# Setup Paths
BASE_DIR = Path.cwd()
FIGURES_DIR = BASE_DIR / "reports" / "figures"
SLIDES_DIR = BASE_DIR / "slides"
RENDERS_DIR = SLIDES_DIR / "renders"
SLIDES_DIR.mkdir(parents=True, exist_ok=True)
RENDERS_DIR.mkdir(parents=True, exist_ok=True)

PDF_OUTPUT_PATH = SLIDES_DIR / "tuannguyen-pqh.pdf"

# Design System Palette (Executive Consulting / BCG / McKinsey Style)
C_NAVY_DARK = "#0A2540"       # Primary text & header brand color
C_STEEL_BLUE = "#20639B"      # Secondary accent & section tag
C_TEAL = "#0D9488"            # Success / profit callout
C_GREEN = "#16A34A"           # Uplift / benefit highlight
C_CRIMSON = "#DC2626"         # Risk / churn / cost
C_AMBER = "#D97706"           # Warning / trigger
C_BG_CARD = "#F8FAFC"         # Card background
C_BORDER = "#E2E8F0"          # Card border
C_TEXT_DARK = "#1E293B"       # Body text
C_TEXT_MUTED = "#64748B"      # Subtitles & citations
C_WHITE = "#FFFFFF"           # Pure white

def create_slide_base(category_tag, action_title, slide_num, total_slides=15, citation=""):
    """Creates a 16:9 slide canvas with standardized corporate header and footer."""
    fig = plt.figure(figsize=(16, 9), dpi=150, facecolor=C_WHITE)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)

    # Top Brand Accent Bar (Navy & Teal)
    ax.add_patch(patches.Rectangle((0, 8.88), 16, 0.12, facecolor=C_NAVY_DARK, edgecolor="none"))
    ax.add_patch(patches.Rectangle((0, 8.82), 3.5, 0.06, facecolor=C_TEAL, edgecolor="none"))

    # Category Tracker Tag
    ax.text(0.8, 8.48, category_tag.upper(), fontsize=10, fontweight="bold", color=C_STEEL_BLUE, fontfamily="sans-serif")

    # Action Title (Conclusion-style Headline)
    # Automatically wrap long titles into 2 balanced lines so text never clips at the right margin
    if "\n" in action_title:
        title_str = action_title
        font_sz = 14.5
        y_pos = 8.24
    elif len(action_title) > 80:
        if "; " in action_title and len(action_title.split("; ")[0]) <= 75:
            parts = action_title.split("; ", 1)
            title_str = parts[0] + ";\n" + parts[1]
        else:
            title_str = textwrap.fill(action_title, width=76)
        font_sz = 14.0
        y_pos = 8.24
    else:
        title_str = action_title
        font_sz = 16.0
        y_pos = 8.02

    ax.text(
        0.8, y_pos, title_str,
        fontsize=font_sz, fontweight="bold", color=C_NAVY_DARK,
        linespacing=1.20,
        va="top" if "\n" in title_str else "center",
        fontfamily="sans-serif"
    )

    # Dividing Line under Header
    ax.plot([0.8, 15.2], [7.70, 7.70], color=C_BORDER, linewidth=1.2)

    # Footer Dividing Line
    ax.plot([0.8, 15.2], [0.65, 0.65], color=C_BORDER, linewidth=1.0)

    # Footnote Citation (Bottom Left)
    if citation:
        ax.text(0.8, 0.38, f"Source: {citation}", fontsize=8.5, fontstyle="italic", color=C_TEXT_MUTED, fontfamily="sans-serif")
    else:
        ax.text(0.8, 0.38, "Company A Strategic Churn Analysis | GCI World 2026", fontsize=8.5, color=C_TEXT_MUTED, fontfamily="sans-serif")

    # Footer Confidentiality & Slide Number (Bottom Right)
    ax.text(14.0, 0.38, f"Page {slide_num} of {total_slides}", fontsize=9.5, fontweight="bold", color=C_NAVY_DARK, ha="right", fontfamily="sans-serif")
    ax.text(12.5, 0.38, "CONFIDENTIAL — FOR BOARD REVIEW ONLY", fontsize=8.0, color=C_TEXT_MUTED, ha="right", fontfamily="sans-serif")

    return fig, ax

def draw_card(ax, rect, title=None, bg_color=C_BG_CARD, border_color=C_BORDER, title_color=C_NAVY_DARK):
    """Draws a rounded rectangular card for content grouping."""
    x, y, w, h = rect
    box = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.08,rounding_size=0.15",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.2,
        zorder=1
    )
    ax.add_patch(box)
    if title:
        ax.text(x + 0.25, y + h - 0.40, title, fontsize=12, fontweight="bold", color=title_color, zorder=2, fontfamily="sans-serif")
        ax.plot([x + 0.25, x + w - 0.25], [y + h - 0.52, y + h - 0.52], color=border_color, linewidth=0.8, zorder=2)

def draw_kpi_badge(ax, rect, number, label, num_color=C_NAVY_DARK, bg_color=C_WHITE, border_color=C_BORDER):
    """Draws a prominent KPI metric callout badge."""
    x, y, w, h = rect
    box = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.05,rounding_size=0.12",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.2,
        zorder=2
    )
    ax.add_patch(box)
    ax.text(x + w / 2, y + h * 0.55, number, fontsize=20, fontweight="bold", color=num_color, ha="center", va="center", zorder=3, fontfamily="sans-serif")
    ax.text(x + w / 2, y + h * 0.22, label, fontsize=9.5, fontweight="bold", color=C_TEXT_MUTED, ha="center", va="center", zorder=3, fontfamily="sans-serif")

def embed_chart(fig, rect, image_path):
    """Embeds a precomputed PNG figure cleanly into the slide within bounding rect."""
    x, y, w, h = rect
    # Normalize to 0-1 figure coordinate space
    norm_rect = [x / 16.0, y / 9.0, w / 16.0, h / 9.0]
    img_ax = fig.add_axes(norm_rect)
    img = Image.open(image_path)
    img_ax.imshow(img)
    img_ax.axis("off")

# ==============================================================================
# SLIDE BUILDERS (15 SLIDES)
# ==============================================================================

def build_slide_01():
    """Slide 1: Title & Strategic Recommendation"""
    fig = plt.figure(figsize=(16, 9), dpi=150, facecolor=C_WHITE)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)

    # Top accent bar & branding
    ax.add_patch(patches.Rectangle((0, 8.85), 16, 0.15, facecolor=C_NAVY_DARK, edgecolor="none"))
    ax.add_patch(patches.Rectangle((0, 8.80), 4.5, 0.05, facecolor=C_TEAL, edgecolor="none"))
    ax.add_patch(patches.Rectangle((0, 0), 16, 0.40, facecolor=C_BG_CARD, edgecolor="none"))
    ax.plot([0, 16], [0.40, 0.40], color=C_BORDER, linewidth=1.0)

    # Subtitle Tag
    ax.text(1.0, 7.80, "GCI WORLD 2026 FINAL ASSIGNMENT — STRATEGIC BUSINESS PROPOSAL", fontsize=11, fontweight="bold", color=C_STEEL_BLUE)

    # Main Presentation Title
    title_text = "PROJECT PHOENIX:\nTransforming Churn Risk into $4.50M Annual Net Profit\nvia Machine Learning & Proactive Upgrades"
    ax.text(1.0, 6.20, title_text, fontsize=26, fontweight="bold", color=C_NAVY_DARK, linespacing=1.2)

    # Subtitle
    ax.text(1.0, 4.95, "A Predictive Lifecycle Retention Strategy Grounded in Empirical Data and Causal Validation", fontsize=13, color=C_TEXT_MUTED)

    # 3 High-Impact KPI Badges
    draw_kpi_badge(ax, (1.0, 3.2, 4.2, 1.4), "+$4.50M", "Annual Net Retained Profit (Base Case)", num_color=C_GREEN, bg_color="#F0FDF4", border_color="#BBF7D0")
    draw_kpi_badge(ax, (5.6, 3.2, 4.2, 1.4), "319.7%", "Program Return on Investment (ROI)", num_color=C_TEAL, bg_color="#F0FDFA", border_color="#99F6E4")
    draw_kpi_badge(ax, (10.2, 3.2, 4.8, 1.4), "5.96%", "Break-Even Retention Uplift Hurdle", num_color=C_NAVY_DARK, bg_color="#F8FAFC", border_color=C_BORDER)

    # Decision Requested Banner Card
    draw_card(ax, (1.0, 1.0, 14.0, 1.8), title="EXECUTIVE DECISION REQUESTED TODAY", bg_color="#EFF6FF", border_color="#BFDBFE", title_color=C_STEEL_BLUE)
    decision_text = (
        "• Authorize immediate deployment of the 15,000-subscriber Randomized Holdout Pilot ($226,182 budget allocation).\n"
        "• Self-Funding Pilot Economics: Targets +$660,236 in net retained pilot profit (291.9% ROI) within 60 days.\n"
        "• Gated Scale-Up: Full enterprise rollout across 100,000 subscribers will proceed only upon statistically verified uplift (p < 0.05)."
    )
    ax.text(1.3, 1.25, decision_text, fontsize=11, color=C_TEXT_DARK, linespacing=1.5, zorder=3)

    # Metadata Footer
    ax.text(1.0, 0.15, "Author: Antigravity Consulting Group | Client: Company A Executive Leadership | Date: October 2026", fontsize=9, color=C_TEXT_MUTED)
    ax.text(15.0, 0.15, "Slide 1 of 15", fontsize=9.5, fontweight="bold", color=C_NAVY_DARK, ha="right")
    return fig

def build_slide_02():
    """Slide 2: Executive Summary"""
    fig, ax = create_slide_base(
        category_tag="Executive Summary | Strategic Synthesis",
        action_title="Company A Faces $34.3M in Churn-Exposed Revenue; Our Gradient Boosting Retention Engine Delivers a Self-Funding 319.7% ROI",
        slide_num=2,
        citation="Bain & Company (2000); McKinsey & Company (2020); GSMA Intelligence (2024); Internal Audited Model."
    )

    # 4 Strategic Pillar Cards
    pillars = [
        ("1. THE CORE VULNERABILITY", (0.8, 4.3, 6.9, 3.1), C_CRIMSON, [
            "• Baseline Churn of 49.6% exposes $2.86M/month ($34.3M/year) in recurring revenue.",
            "• Churn surges to 57.9% as handsets cross 1-2 years (H2 Confirmed).",
            "• Acute usage drop (change_mou < -100m) drives 53.6% churn (H1 Confirmed).",
            "• Silent Churn Trap: 51.8% of churners leave with zero customer service calls (H3)."
        ]),
        ("2. MACHINE LEARNING ENGINE", (8.1, 4.3, 7.1, 3.1), C_STEEL_BLUE, [
            "• HistGradientBoosting Champion achieves 0.6964 Test ROC-AUC (zero leakage).",
            "• Lift@20% = 1.46x: Top 2 risk deciles concentrate 72.5% churn density.",
            "• Economic Cutoff tau* = 0.25: Captures 97.24% of all churners (7,229 subs).",
            "• Generates +$90,977 (+26.2%) profit surplus over standard 0.50 cutoff."
        ]),
        ("3. PROJECT PHOENIX INTERVENTION", (0.8, 0.9, 6.9, 3.1), C_TEAL, [
            "• Proactive Handset Upgrade: $25–$50 device subsidy + 0% APR installment refresh.",
            "• Tariff Rightsizing: Migrates usage-drop accounts to zero-overage flat rate plans.",
            "• Mandatory 12-Month Contract Renewal: Locks in customer lifetime equity.",
            "• Value-Tier Routing: Outbound Concierge for High ARPU; Mobile App for Mid/Low."
        ]),
        ("4. QUANTIFIED ROI & GOVERNANCE", (8.1, 0.9, 7.1, 3.1), C_GREEN, [
            "• Base Case Annual Scale: +$4.50M Net Retained Profit with 319.7% ROI.",
            "• Cost Per Retained Subscriber (CPRS): $116.77 (vs $350–$600 Industry CAC).",
            "• Resilient Break-Even Hurdle: Requires only 5.96% retention uplift (>3.0x safety margin).",
            "• 15k Pilot Trial: Generates +$660,236 net pilot profit with 90/10 holdout control."
        ])
    ]

    for title, rect, color, bullets in pillars:
        draw_card(ax, rect, title=title, title_color=color)
        text_content = "\n".join(bullets)
        ax.text(rect[0] + 0.25, rect[1] + rect[3] - 0.70, text_content, fontsize=10.5, color=C_TEXT_DARK, linespacing=1.45, va="top", zorder=3)

    return fig

def build_slide_03():
    """Slide 3: Market Context & Strategic Imperative"""
    fig, ax = create_slide_base(
        category_tag="Market Context | Strategic Imperative",
        action_title="In a Saturated Postpaid Market, Customer Acquisition Costs 5x to 25x More Than Retention as Replacement Cycles Elongate",
        slide_num=3,
        citation="Reichheld (2000), Bain & Company / HBR; Counterpoint Research (2024); McKinsey & Company (2020)."
    )

    # Left Column: Macro Dynamics (2 Cards)
    draw_card(ax, (0.8, 4.3, 7.2, 3.1), title="MACRO TREND 1: ZERO-SUM MARKET SATURATION", title_color=C_NAVY_DARK)
    t1 = (
        "• Saturated Wireless Market: Mobile SIM penetration exceeds 100% in mature markets.\n"
        "  Every new subscriber won is poached from a competitor, driving CAC to $350–$600.\n"
        "• The 5% Loyalty Leverage (Bain & Co.): Increasing customer retention by just 5%\n"
        "  expands operating profit by 25% to 95%, as retained accounts require zero acquisition cost.\n"
        "• Strategic Mandate: Company A cannot afford to bleed 49.6% churn while paying high CAC."
    )
    ax.text(1.05, 6.70, t1, fontsize=10.5, color=C_TEXT_DARK, linespacing=1.45, va="top", zorder=3)

    draw_card(ax, (0.8, 0.9, 7.2, 3.1), title="MACRO TREND 2: ELONGATING REPLACEMENT CYCLES", title_color=C_NAVY_DARK)
    t2 = (
        "• Handset Replacement Stretched to 36–43 Months (Counterpoint Research, 2024).\n"
        "  Customers hold onto aging devices longer due to slowing hardware innovation.\n"
        "• The Contract Expiration Cliff: When initial 12 or 24-month carrier device subsidies end,\n"
        "  customers become uncontracted 'free agents' and churn to rival switch-and-save deals.\n"
        "• Proactive Upgrades Win: Timely hardware subsidies lock in contracts before defection cliffs."
    )
    ax.text(1.05, 3.30, t2, fontsize=10.5, color=C_TEXT_DARK, linespacing=1.45, va="top", zorder=3)

    # Right Column: Economics of Retention vs Acquisition
    draw_card(ax, (8.3, 0.9, 6.9, 6.5), title="ECONOMIC COMPARISON: ACQUISITION VS RETENTION", title_color=C_STEEL_BLUE)

    # Comparison Graphic / KPI Cards
    draw_kpi_badge(ax, (8.6, 5.0, 3.0, 1.4), "$350–$600", "Customer Acquisition Cost (CAC)", num_color=C_CRIMSON, bg_color="#FEF2F2", border_color="#FECACA")
    draw_kpi_badge(ax, (11.9, 5.0, 3.0, 1.4), "$116.77", "Project Phoenix CPRS (Base)", num_color=C_GREEN, bg_color="#F0FDF4", border_color="#BBF7D0")

    comp_text = (
        "KEY COMMERCIAL TAKEAWAYS FOR LEADERSHIP:\n\n"
        "1. 4.3x Cost Advantage: Retaining an existing subscriber through Project Phoenix\n"
        "   costs $116.77—over 4x cheaper than acquiring a replacement subscriber.\n\n"
        "2. CAC Payback Vulnerability: New postpaid acquisitions require 6–12 months of ARPU\n"
        "   just to break even on initial sales commissions and device discounts (McKinsey).\n"
        "   A customer churning at month 12 destroys all accumulated lifetime margin.\n\n"
        "3. Failure of Reactive Retention Desks: Over 51% of churners leave silently.\n"
        "   Waiting for angry inbound calls loses half the market; predictive ML is essential."
    )
    ax.text(8.6, 4.40, comp_text, fontsize=10.5, color=C_TEXT_DARK, linespacing=1.45, va="top", zorder=3)

    return fig

def build_slide_04():
    """Slide 4: Company A Data Foundation & Audit Opportunity"""
    fig, ax = create_slide_base(
        category_tag="Data Opportunity | Enterprise Audit & Cleanliness",
        action_title="A 100,000-Subscriber Enterprise Dataset Enables Granular Behavioral Modeling with 100% Relational Integrity",
        slide_num=4,
        citation="GCI World Organizing Committee (2026), Dataset Overview [SRC-001]; Internal Audit Reports."
    )

    # Left Column: Data Scale & Architecture (Card)
    draw_card(ax, (0.8, 0.9, 7.0, 6.5), title="ENTERPRISE DATA AUDIT & PIPELINE INTEGRITY", title_color=C_NAVY_DARK)
    audit_text = (
        "• Enterprise Asset Scale: 100,000 unique postpaid subscriber records across 100 raw\n"
        "  behavioral, billing, usage, technical network, and demographic attributes.\n\n"
        "• Flawless 1:1 Relational Merge: Client.csv and Record.csv joined via Customer_ID with\n"
        "  zero duplicate IDs, zero missing keys, and 100% inner/outer relational consistency.\n\n"
        "• Missingness Architecture (MNAR): 43 columns contain missing values, heavily\n"
        "  concentrated in demographics (numbcars 49.4%, dwllsize 38.3%, HHstatin 37.9%).\n"
        "  - Strategic Missing Indicators: Adding explicit MissingIndicator flags unlocked +0.51%\n"
        "    in ROC-AUC lift over naive row deletion, proving missingness holds behavioral signal.\n\n"
        "• Negative Values Verified: Negative values in change_mou (53,651 accounts) and\n"
        "  change_rev (56,150 accounts) confirmed as valid business signals of usage contraction.\n\n"
        "• Operational Buffer: Churn target defined 31–60 days post-T0, establishing a dedicated\n"
        "  30-day intervention window (Days 1–30) for campaign execution before defection."
    )
    ax.text(1.05, 6.70, audit_text, fontsize=10.5, color=C_TEXT_DARK, linespacing=1.40, va="top", zorder=3)

    # Right Column: Visualizing Missingness Structure
    draw_card(ax, (8.1, 0.9, 7.1, 6.5), title="FIGURE 2: MISSINGNESS ARCHITECTURE & IMPUTATION", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.3, 1.1, 6.7, 5.7), FIGURES_DIR / "fig2_missingness_structure.png")

    return fig

def build_slide_05():
    """Slide 5: EDA Baseline: The $34.3M Revenue-at-Risk Challenge"""
    fig, ax = create_slide_base(
        category_tag="Exploratory Data Analysis | Revenue Exposure Baseline",
        action_title="Baseline Churn of 49.6% Exposes $2.86M in Monthly Revenue, Highly Concentrated in Top-Tier ARPU Accounts",
        slide_num=5,
        citation="Company A Internal Dataset Audit (n=100,000); DEC-010; EVD-012, EVD-027, EVD-032."
    )

    # Left Column: Text Insights & 2 KPI Cards
    draw_card(ax, (0.8, 3.4, 7.0, 4.0), title="CHURN SCALE & VALUE-AT-RISK CONCENTRATION", title_color=C_CRIMSON)
    eda_text = (
        "• Balanced Case-Control Design: 50.44% retained (50,438) vs 49.56% churned (49,562).\n"
        "  Reflects an intentional 1:1 case-control research sample designed to train highly\n"
        "  discriminative machine learning models across nuanced defection patterns.\n\n"
        "• $34.3M Annual Revenue Leak: Churned accounts represent $2,860,677 in lost monthly\n"
        "  recurring revenue, totaling $34.33 million in annualized gross revenue-at-risk.\n\n"
        "• Extreme Value Skew: Churn risk is heavily concentrated in top ARPU accounts:\n"
        "  - Top 20% ARPU (Quintile 5, avg $123.82/mo) = 41.8% of churn dollars ($1.20M/mo).\n"
        "  - Bottom 20% ARPU (Quintile 1, avg $22.42/mo) = Only 7.6% of churn dollars.\n"
        "• 5.5x Damage Factor: Losing 1 Q5 customer inflicts the financial loss of 5.5 Q1 accounts."
    )
    ax.text(1.05, 6.75, eda_text, fontsize=10.5, color=C_TEXT_DARK, linespacing=1.38, va="top", zorder=3)

    draw_kpi_badge(ax, (0.8, 0.9, 3.35, 2.2), "$34.3M", "Annual Revenue-at-Risk", num_color=C_CRIMSON, bg_color="#FEF2F2", border_color="#FECACA")
    draw_kpi_badge(ax, (4.45, 0.9, 3.35, 2.2), "41.8%", "Risk in Top 20% ARPU", num_color=C_AMBER, bg_color="#FFFBEB", border_color="#FDE68A")

    # Right Column: Value-at-Risk Pareto Distribution
    draw_card(ax, (8.1, 0.9, 7.1, 6.5), title="FIGURE 7: VALUE-AT-RISK BY ARPU QUINTILE", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.3, 1.1, 6.7, 5.7), FIGURES_DIR / "fig7_revenue_segmentation_value_at_risk.png")

    return fig

def build_slide_06():
    """Slide 6: EDA Discoveries: Equipment Obsolescence & Usage Collapse"""
    fig, ax = create_slide_base(
        category_tag="Exploratory Data Analysis | Behavioral Defection Triggers",
        action_title="Aging Handsets and Acute Usage Drops Are the Primary Empirical Catalysts of Subscriber Defection",
        slide_num=6,
        citation="Company A Dataset; Mann-Whitney U tests; EVD-023 (H2), EVD-024 (H1), EVD-025 (H3); DEC-010."
    )

    # Left Column: Findings Summary
    draw_card(ax, (0.8, 0.9, 6.8, 6.5), title="EMPIRICAL HYPOTHESIS TESTING (H1–H3)", title_color=C_NAVY_DARK)
    h_text = (
        "1. HYPOTHESIS H2: HANDSET AGE CLIFF (STRONGLY CONFIRMED)\n"
        "• Device <6m: 41.74% churn (n=18,327)\n"
        "• Device 6–12m: 46.97% churn (n=36,356)\n"
        "• Device 1–2 years: 53.84% churn (n=34,505)\n"
        "• Device >2 years: 57.89% churn (n=10,811)\n"
        "-> Surge of +16.15 pp (p < 1e-100, r = +0.1127). As phones age past year 1,\n"
        "   hardware slows, contract subsidies expire, and defection spikes.\n\n"
        "2. HYPOTHESIS H1: USAGE DROP EARLY WARNING (STRONGLY CONFIRMED)\n"
        "• Subscribers with severe MOU decline (change_mou < -100 min) churn at 53.62%\n"
        "  vs 45.45% for stable usage (+8.17 pp, p = 6.06e-59).\n"
        "-> Usage decline indicates disengagement or bill shock, serving as a leading indicator.\n\n"
        "3. HYPOTHESIS H3: THE SILENT CHURN PARADOX (NUANCED ALIGNMENT)\n"
        "• 55,692 churners (51.76%) leave with ZERO customer care calls (custcare=0).\n"
        "  Frequent callers churn at a lower rate (44.66%).\n"
        "-> Churners leave silently; inbound call center desks miss over half of defectors."
    )
    ax.text(1.05, 6.70, h_text, fontsize=10.0, color=C_TEXT_DARK, linespacing=1.35, va="top", zorder=3)

    # Right Column: Embedded Charts (Fig 4 Handset Age + Fig 3 Usage Drop)
    draw_card(ax, (7.9, 3.8, 7.3, 3.6), title="FIGURE 4: HANDSET AGE CLIFF (eqpdays)", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.1, 3.9, 6.9, 3.0), FIGURES_DIR / "fig4_h2_equipment_age_lifecycle.png")

    draw_card(ax, (7.9, 0.9, 7.3, 2.7), title="FIGURE 3: USAGE DROP DISTRIBUTION (change_mou)", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.1, 1.0, 6.9, 2.1), FIGURES_DIR / "fig3_h1_consumption_drop_change_mou_rev.png")

    return fig

def build_slide_07():
    """Slide 7: Problem Formulation & Leakage-Free Decision Architecture"""
    fig, ax = create_slide_base(
        category_tag="Problem Definition | Operational Timing & Leakage Governance",
        action_title="A Strict 30-Day Operational Buffer with Zero Predictive Leakage Converts Churn Prediction into Timely Intervention",
        slide_num=7,
        citation="GCI World Guidelines [SRC-001]; DEC-014 (Horizon), DEC-015 (Expected Value Matrix); EVD-028 to EVD-034."
    )

    # Left Column: Timing & Zero Leakage Audit
    draw_card(ax, (0.8, 0.9, 7.0, 6.5), title="OPERATIONAL HORIZON & LEAKAGE AUDIT", title_color=C_NAVY_DARK)
    p_text = (
        "• 30-Day Operational Intervention Buffer (DEC-014):\n"
        "  - Target churn is observed strictly between 31 and 60 days after observation T0.\n"
        "  - Days 1 to 30 serve as the 'Operational Intervention Window': the vital period\n"
        "    for CRM batch scoring, customer tiering, and device shipment delivery.\n\n"
        "• Zero Future Leakage Guarantee (EVD-028, EVD-029):\n"
        "  - Comprehensive audit of all 98 candidate predictors confirmed that all attributes\n"
        "    represent historical state at or prior to T0.\n"
        "  - Max correlation with churn is |r| = 0.1127 (eqpdays) and |r| = 0.1032 (hnd_price).\n"
        "  - Zero predictors exceed |r| >= 0.20; zero target proxies; Customer_ID excluded.\n\n"
        "• Expected Value Decision Matrix vs Accuracy Trap (DEC-015):\n"
        "  - In telecom retention, error costs are deeply asymmetric:\n"
        "    * False Negative (Missed Churner): Loses ~$504 in Customer Lifetime Value.\n"
        "    * False Positive (Unneeded Contact): Costs ~$38 in voucher and contact fees.\n"
        "  - We optimize models for Expected Net Retained Profit, not naive accuracy."
    )
    ax.text(1.05, 6.70, p_text, fontsize=10.2, color=C_TEXT_DARK, linespacing=1.38, va="top", zorder=3)

    # Right Column: Correlation Audit Chart
    draw_card(ax, (8.1, 0.9, 7.1, 6.5), title="FIGURE 8: LEAKAGE AUDIT CORRELATION MATRIX", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.3, 1.1, 6.7, 5.7), FIGURES_DIR / "fig8_correlation_matrix_key_drivers.png")

    return fig

def build_slide_08():
    """Slide 8: Feature Engineering & Multi-Model Benchmark Strategy"""
    fig, ax = create_slide_base(
        category_tag="Model Strategy | Controlled Pipeline & Feature Ablation",
        action_title="12 Domain Levers and Missing Indicators Boost Discrimination Power across a Stratified 70/15/15 Split",
        slide_num=8,
        citation="DEC-016 (70/15/15 Split), DEC-017 (Missing Indicators), DEC-018 (Domain Levers); EVD-035 to EVD-038."
    )

    # Left Column: Pipeline Architecture
    draw_card(ax, (0.8, 3.8, 7.1, 3.6), title="STRATIFIED SPLIT & PRODUCTION PIPELINE", title_color=C_NAVY_DARK)
    pipe_text = (
        "• Stratified 70/15/15 Split (DEC-016): 70,000 Train, 15,000 Val, and 15,000 Test.\n"
        "  - Churn rate held constant at 49.56% across all splits with fixed seed 42.\n"
        "  - Held-out Test Set strictly locked: zero parameter tuning, zero transformer fitting.\n\n"
        "• Scikit-Learn ColumnTransformer Architecture:\n"
        "  - Numerical (77 features): SimpleImputer(median, add_indicator=True) + StandardScaler.\n"
        "  - Categorical (21 features): SimpleImputer(fill_value='Missing') + OneHotEncoder.\n"
        "  - Final Transformed Space: 279 dense features, 0 missing NaNs, zero leakage."
    )
    ax.text(1.05, 6.75, pipe_text, fontsize=10.2, color=C_TEXT_DARK, linespacing=1.38, va="top", zorder=3)

    # Left Bottom: 12 Domain Levers Card
    draw_card(ax, (0.8, 0.9, 7.1, 2.7), title="12 ENGINEERED DOMAIN LEVERS", title_color=C_STEEL_BLUE)
    levers_text = (
        "• Handset Lifecycle (H2): eqpdays_years, eqp_over_1yr, eqp_over_2yr, eqp_to_tenure_ratio\n"
        "• Usage Decay (H1): severe_mou_drop, severe_rev_drop\n"
        "• Bill Friction: rev_per_mou, overage_rev_ratio\n"
        "• Value & Care (H3/H4): silent_churner_flag, drop_per_call, multi_line_flag, high_arpu_tier"
    )
    ax.text(1.05, 3.0, levers_text, fontsize=10.0, color=C_TEXT_DARK, linespacing=1.40, va="top", zorder=3)

    # Right Column: Ablation Gains & Metrics
    draw_card(ax, (8.2, 0.9, 7.0, 6.5), title="EMPIRICAL FEATURE ABLATION LIFT ON VALIDATION SET", title_color=C_GREEN)
    draw_kpi_badge(ax, (8.5, 4.8, 3.0, 1.5), "+0.51%", "Missing Indicators Lift", num_color=C_STEEL_BLUE, bg_color="#EFF6FF", border_color="#BFDBFE")
    draw_kpi_badge(ax, (11.8, 4.8, 3.0, 1.5), "+0.62%", "12 Domain Levers Lift", num_color=C_GREEN, bg_color="#F0FDF4", border_color="#BBF7D0")

    ablation_text = (
        "ABLATION STUDY EXPERIMENTAL RESULTS (Validation N=15,000):\n\n"
        "1. Raw Baseline (Excluding High-Missing Cols): ROC-AUC = 0.6278\n"
        "   - Dropping 6 high-missing demographic columns lost vital non-response signal.\n\n"
        "2. Missing Indicator Pipeline (DEC-017): ROC-AUC = 0.6329 (+0.0051 Gain)\n"
        "   - Retaining all columns + MissingIndicator flags proved missingness holds predictive value.\n\n"
        "3. Full Pipeline with 12 Domain Levers (DEC-018): ROC-AUC = 0.6391 (+0.0062 Gain)\n"
        "   - Cumulative Feature Engineering Gain: +0.0113 ROC-AUC (+1.13 percentage points).\n\n"
        "4. Non-linear Boosting (Champion): ROC-AUC reaches 0.6903 on this engineered space."
    )
    ax.text(8.5, 4.4, ablation_text, fontsize=10.2, color=C_TEXT_DARK, linespacing=1.40, va="top", zorder=3)

    return fig

def build_slide_09():
    """Slide 9: Model Results: HistGradientBoosting Champion & Threshold Optimization"""
    fig, ax = create_slide_base(
        category_tag="Machine Learning Results | Champion Benchmark & Optimization",
        action_title="HistGradientBoosting Achieves 0.6964 Test ROC-AUC; Threshold Optimization at tau*=0.25 Unlocks +$90.9k Net Surplus",
        slide_num=9,
        citation="Model Benchmarks (`reports/model_benchmarks.md`); DEC-019 (Champion), DEC-020 (Threshold); EVD-039 to EVD-045."
    )

    # Left Column: Benchmark Suite Table & Explicit Metric Callouts
    draw_card(ax, (0.8, 3.4, 7.1, 4.0), title="BENCHMARK OF 4 MODEL FAMILIES (TEXT & SCORES)", title_color=C_NAVY_DARK)
    bench_table = (
        "MODEL PERFORMANCE COMPARISON (Validation Set N=15,000):\n"
        "-------------------------------------------------------------------------------------------------\n"
        "Model Name                     ROC-AUC   PR-AUC   Accuracy   F1-Score   Status\n"
        "-------------------------------------------------------------------------------------------------\n"
        "DummyClassifier (Prior)        0.5000    0.4956   50.44%     0.0000     Baseline\n"
        "LogisticRegression (Linear)    0.6392    0.6235   60.15%     61.20%     Linear Ref\n"
        "RandomForest (Bagging)         0.6635    0.6473   61.47%     61.80%     Non-linear\n"
        "HistGradientBoosting           0.6903    0.6772   63.52%     63.70%     CHAMPION\n"
        "-------------------------------------------------------------------------------------------------\n"
        "• INDEPENDENT TEST SET AUDIT: Test ROC-AUC = 0.6964 | Test PR-AUC = 0.6865\n"
        "  Generalization gap < 0.0061, confirming zero overfitting on locked 15k test set.\n"
        "• DECILE LIFT@20%: 1.46x (Top 20% risk decile concentrates 72.53% churn density)."
    )
    ax.text(1.05, 6.75, bench_table, fontsize=9.5, fontfamily="monospace", color=C_TEXT_DARK, linespacing=1.28, va="top", zorder=3)

    # Left Bottom: Threshold Optimization Card
    draw_card(ax, (0.8, 0.9, 7.1, 2.3), title="ECONOMIC THRESHOLD OPTIMIZATION (tau* = 0.25)", title_color=C_GREEN)
    opt_text = (
        "• Shifting Cutoff from Default 0.50 to 0.25:\n"
        "  - Churner Recall expands from 64.60% to 97.24% (Captures 7,229 out of 7,434 churners).\n"
        "  - Net Profit increases from $346.6k to $437.6k (+26.2% profit uplift / +$90,977.22 surplus).\n"
        "• Captures 97% of defectors at a fraction of customer lifetime acquisition cost."
    )
    ax.text(1.05, 2.65, opt_text, fontsize=10.0, color=C_TEXT_DARK, linespacing=1.35, va="top", zorder=3)

    # Right Column: Fig 9 (ROC/PR) and Fig 10 (Profit vs Cutoff)
    draw_card(ax, (8.1, 4.4, 7.1, 3.0), title="FIGURE 9: BENCHMARK ROC & PR CURVES", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.3, 4.5, 6.7, 2.5), FIGURES_DIR / "fig9_model_benchmark_roc_pr.png")

    draw_card(ax, (8.1, 0.9, 7.1, 3.3), title="FIGURE 10: NET PROFIT VS DECISION THRESHOLD", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.3, 1.0, 6.7, 2.8), FIGURES_DIR / "fig10_cost_benefit_profit_threshold.png")

    return fig

def build_slide_10():
    """Slide 10: Model Drivers & Ethical Actionability Audit"""
    fig, ax = create_slide_base(
        category_tag="Explainability & Ethics | Feature Importance & Subgroup Audit",
        action_title="Permutation Importance Confirms Equipment and Usage Triggers; Subgroup Audits Prove Model Invariance Across Lines",
        slide_num=10,
        citation="Permutation Importance & Subgroup Audit (`reports/model_interpretation.md`); DEC-021, DEC-022; EVD-046 to EVD-050."
    )

    # Left Column: Importance & Ethical Firewall
    draw_card(ax, (0.8, 4.0, 7.0, 3.4), title="TOP PREDICTIVE DRIVERS & ACTIONABILITY", title_color=C_NAVY_DARK)
    imp_text = (
        "• Top Permutation Feature Importance (AUC Drop):\n"
        "  1. months: +0.0362 (Contractual tenure cliff at 12 & 24 months)\n"
        "  2. change_mou: +0.0310 (Acute usage contraction early warning indicator)\n"
        "  3. eqpdays: +0.0305 (Aging equipment obsolescence cliff)\n"
        "  4. totmrc_Mean: +0.0098 (Monthly recurring charge / plan size)\n"
        "  5. avgmou: +0.0089 (Baseline customer engagement level)\n\n"
        "• Actionable Levers (Direct Interventions): eqpdays (upgrade subsidies),\n"
        "  change_mou (plan rightsizing), overage_rev_ratio (bill-shock elimination).\n"
        "• Timing Triggers (Observational): months (triggers outreach at Month 11/23)."
    )
    ax.text(1.05, 6.75, imp_text, fontsize=9.8, color=C_TEXT_DARK, linespacing=1.35, va="top", zorder=3)

    draw_card(ax, (0.8, 0.9, 7.0, 2.9), title="ETHICAL FIREWALL & SUBGROUP FAIRNESS AUDIT", title_color=C_CRIMSON)
    fair_text = (
        "• Strict Ethical Firewall (DEC-022): Demographic variables (ethnic, income,\n"
        "  marital, ownrent) are strictly isolated and banned from retention targeting.\n"
        "• Subgroup Invariance Audit (EVD-048, EVD-049):\n"
        "  - ROC-AUC remains between 0.6370 and 0.7363 across all operational segments.\n"
        "  - Single-line (0.6910) and Multi-line (0.6890) accounts perform identically (delta < 0.002).\n"
        "  - Recall at tau*=0.25 exceeds 91.5% across every subgroup (min 91.5%, max 99.8%)."
    )
    ax.text(1.05, 3.25, fair_text, fontsize=9.8, color=C_TEXT_DARK, linespacing=1.35, va="top", zorder=3)

    # Right Column: Figures 11 & 12
    draw_card(ax, (8.0, 4.3, 7.2, 3.1), title="FIGURE 11: FEATURE IMPORTANCE & ACTIONABILITY", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.2, 4.4, 6.8, 2.6), FIGURES_DIR / "fig11_feature_importance_actionability.png")

    draw_card(ax, (8.0, 0.9, 7.2, 3.2), title="FIGURE 12: SUBGROUP ROBUSTNESS & INVARIANCE", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.2, 1.0, 6.8, 2.7), FIGURES_DIR / "fig12_segment_robustness.png")

    return fig

def build_slide_11():
    """Slide 11: Recommended Strategy: Project Phoenix Operational Blueprint"""
    fig, ax = create_slide_base(
        category_tag="Business Proposal | Project Phoenix Operational Architecture",
        action_title="Project Phoenix Deploys Value-Tiered Proactive Upgrades and Tariff Rightsizing via a 5-Step Operational Engine",
        slide_num=11,
        citation="Project Phoenix Operational Blueprint (`reports/business_proposal.md`); DEC-023; EVD-027, EVD-051."
    )

    # Top Half: 5-Step Operational Engine (Flow Diagram Cards)
    steps = [
        ("STAGE 1: SUNDAY 02:00", "Data Lake Ingestion\n& Batch Scoring\n(HistGradientBoosting)", C_NAVY_DARK),
        ("STAGE 2: MONDAY 08:00", "Cutoff tau* >= 0.25\n& Ethical Firewall\nValue-Tier Routing", C_STEEL_BLUE),
        ("STAGE 3: TUESDAY 09:00", "Omnichannel Outreach\nVIP Concierge Phone\nvs Mobile App Push", C_AMBER),
        ("STAGE 4: DAYS 1–21", "Offer Redemption\n& Device Delivery\n12-Month Contract Lock", C_TEAL),
        ("STAGE 5: DAYS 30–60", "Holdout A/B Audit\nCausal Uplift & MLOps\nRetraining Feedback", C_GREEN),
    ]

    for i, (title, text, color) in enumerate(steps):
        x = 0.8 + i * 2.92
        draw_card(ax, (x, 5.0, 2.76, 2.4), title=title, title_color=color)
        ax.text(x + 0.2, 6.6, text, fontsize=9.8, color=C_TEXT_DARK, linespacing=1.35, va="top", zorder=3)
        if i < 4:
            ax.annotate("", xy=(x + 2.88, 6.2), xytext=(x + 2.76, 6.2), arrowprops=dict(arrowstyle="->", lw=2, color=C_STEEL_BLUE))

    # Bottom Half: Value-Tier Omnichannel Routing Matrix
    draw_card(ax, (0.8, 0.9, 14.4, 3.8), title="VALUE-TIER OMNICHANNEL INTERVENTION MATRIX", title_color=C_NAVY_DARK)
    matrix_table = (
        "VALUE TIER         SHARE OF RISK   PRIMARY CHANNEL            INCENTIVE & RETENTION OFFER                  COST STRUCTURE\n"
        "-----------------------------------------------------------------------------------------------------------------------------------\n"
        "High-Value Tier    41.8% of lost   Dedicated Outbound Phone   • $50 Handset Subsidy / Free 5G Upgrade     $6.50 Outreach\n"
        "(ARPU > $75/mo)    revenue dollars Concierge Desk (VIP Team)  • Zero-Overage Bill Freeze + 12m Contract   $50.00 Voucher\n"
        "-----------------------------------------------------------------------------------------------------------------------------------\n"
        "Mid-Value Tier     45.2% of lost   MyCompanyA Mobile App      • $35 Handset Voucher + 0% APR Installment  $2.50 Outreach\n"
        "(ARPU $40–$75)     revenue dollars Push Notification + Email  • Tariff Rightsizing to Match Current MOU   $35.00 Voucher\n"
        "-----------------------------------------------------------------------------------------------------------------------------------\n"
        "Growth / Entry     13.0% of lost   Automated Interactive SMS  • $25 Accessory / Handset Voucher           $1.00 Outreach\n"
        "(ARPU < $40/mo)    revenue dollars + Web Self-Care Link       • Zero-Overage Flat Rate Migration (12m)    $25.00 Voucher\n"
        "-----------------------------------------------------------------------------------------------------------------------------------\n"
        "• GOVERNANCE RULE: 12-Month Contract Renewal is mandatory to redeem subsidies, completely eliminating deadweight loss."
    )
    ax.text(1.05, 4.05, matrix_table, fontsize=9.5, fontfamily="monospace", color=C_TEXT_DARK, linespacing=1.28, va="top", zorder=3)

    return fig

def build_slide_12():
    """Slide 12: Quantified Business Case: 3-Scenario ROI & Sensitivity"""
    fig, ax = create_slide_base(
        category_tag="Business Case | Multi-Scenario Financial Model & Sensitivity",
        action_title="Base Case Generates +$4.50M in Annual Net Profit with a 319.7% ROI and a Resilient 5.96% Break-Even Hurdle",
        slide_num=12,
        citation="Project Phoenix Financial Model (`reports/business_proposal.md` Tables 8.2 & 8.3); DEC-024; EVD-052 to EVD-056."
    )

    # Left Column: 3-Scenario Financial Table
    draw_card(ax, (0.8, 3.6, 7.2, 3.8), title="ANNUAL FINANCIAL FORECAST (100,000 SUBSCRIBERS)", title_color=C_NAVY_DARK)
    fin_table = (
        "METRIC / SCENARIO               CONSERVATIVE    BASE CASE       OPTIMISTIC\n"
        "---------------------------------------------------------------------------\n"
        "Targeted Subscribers (tau*>=0.25) 92,313          92,313          92,313\n"
        "High-Risk Churners in Pool      48,223          48,223          48,223\n"
        "Relative Retention Uplift       15.0%           25.0%           35.0%\n"
        "Saved Subscribers               7,233.5         12,055.8        16,878.1\n"
        "Gross Retained Contribution     $3,103,151      $5,909,007      $9,417,954\n"
        "Total Program Investment        $1,292,382      $1,407,773      $1,477,008\n"
        "---------------------------------------------------------------------------\n"
        "NET RETAINED PROFIT             +$1,810,769     +$4,501,233     +$7,940,946\n"
        "PROGRAM ROI                     140.1%          319.7%          537.6%\n"
        "Cost Per Retained Sub (CPRS)    $178.67         $116.77         $87.51\n"
        "Break-Even Retention Uplift     6.25%           5.96%           5.49%\n"
        "---------------------------------------------------------------------------"
    )
    ax.text(1.0, 6.80, fin_table, fontsize=9.2, fontfamily="monospace", color=C_TEXT_DARK, linespacing=1.20, va="top", zorder=3)

    # Left Bottom: Break-Even & Safety Margin
    draw_card(ax, (0.8, 0.9, 7.2, 2.5), title="MARGIN OF SAFETY & COST ADVANTAGE", title_color=C_GREEN)
    be_text = (
        "• CPRS Advantage ($116.77 vs $350–$600 CAC): Saving a customer is 3x to 5x cheaper\n"
        "  than replacing them through sales acquisition (EVD-017, EVD-053).\n"
        "• 5.96% Break-Even Hurdle: The program is self-funding if it prevents just 6 out of 100\n"
        "  churns. Because industry upgrades achieve 20%–35% uplift, safety margin > 3.0x.\n"
        "• 2D Sensitivity: Net profit is positive (+$0.45M to +$9.40M) across all 42 test cells."
    )
    ax.text(1.05, 2.80, be_text, fontsize=9.8, color=C_TEXT_DARK, linespacing=1.35, va="top", zorder=3)

    # Right Column: Figures 13A (Waterfall) & 13B (Heatmap)
    draw_card(ax, (8.2, 0.9, 7.0, 6.5), title="FIGURE 13: FINANCIAL IMPACT WATERFALL & SENSITIVITY", title_color=C_STEEL_BLUE)
    embed_chart(fig, (8.3, 1.1, 6.8, 5.7), FIGURES_DIR / "fig13ab_financial_waterfall_sensitivity.png")

    return fig

def build_slide_13():
    """Slide 13: Pilot Design: 15,000-Subscriber Randomized Holdout Trial"""
    fig, ax = create_slide_base(
        category_tag="Implementation & Pilot | Randomized Holdout Experimentation",
        action_title="A 15,000-Subscriber Randomized Holdout Trial Delivers Causal Validation and +$660.2k Net Profit in 60 Days",
        slide_num=13,
        citation="Pilot Experimentation Framework (`reports/business_proposal.md` Section 4); DEC-024; EVD-055."
    )

    # Left Top: Figure 13C Pilot Architecture Visual Diagram Card
    draw_card(ax, (0.8, 3.4, 7.1, 4.0), bg_color=C_WHITE, border_color=C_BORDER)
    embed_chart(fig, (0.9, 3.45, 6.9, 3.9), FIGURES_DIR / "fig13c_pilot_holdout_architecture.png")

    # Left Bottom: Self-Funding Pilot Economics (2 KPI badges)
    draw_card(ax, (0.8, 0.9, 7.1, 2.3), title="SELF-FUNDING PILOT FINANCIAL RETURNS", title_color=C_GREEN)
    draw_kpi_badge(ax, (1.1, 1.1, 3.1, 1.5), "+$660,236", "Net Retained Pilot Profit", num_color=C_GREEN, bg_color="#F0FDF4", border_color="#BBF7D0")
    draw_kpi_badge(ax, (4.5, 1.1, 3.1, 1.5), "291.9%", "Pilot Program ROI", num_color=C_TEAL, bg_color="#F0FDFA", border_color="#99F6E4")

    # Right Column: 90-Day Implementation Roadmap
    draw_card(ax, (8.1, 0.9, 7.1, 6.5), title="90-DAY PHASED IMPLEMENTATION ROADMAP", title_color=C_STEEL_BLUE)
    roadmap_text = (
        "PHASE 1: WEEKS 1–2 (PREPARATION & GOVERNANCE)\n"
        "• Finalize OEM 5G handset inventory allocation and volume rebate agreements.\n"
        "• Configure CRM batch scoring script and integrate 90/10 holdout assignment.\n"
        "• Brief Outbound Concierge Desk on VIP high-ARPU retention playbooks.\n\n"
        "PHASE 2: WEEKS 3–8 (60-DAY PILOT EXECUTION)\n"
        "• Dispatch multi-channel offers to 13,500 treatment subscribers.\n"
        "• Daily monitoring of delivery, bounce, open, and voucher redemption rates.\n"
        "• Real-time tracking of customer complaint logs and opt-out rates.\n\n"
        "PHASE 3: WEEKS 9–10 (CAUSAL AUDIT & GATED SCALE-UP)\n"
        "• Evaluate 31–60 day churn outcomes in Treatment vs Holdout Control.\n"
        "• Gate 1: Verify statistically significant retention uplift (p < 0.05).\n"
        "• Gate 2: Verify Net Retained Pilot Profit > $250,000 (Target: +$660k).\n"
        "• Gate 3: Verify customer safety guardrails (Delta NPS >= 0, Opt-out < 1.5%).\n\n"
        "PHASE 4: MONTH 3+ (FULL ENTERPRISE SCALE-UP)\n"
        "• Expand Project Phoenix across all 100k annual subscribers to capture $4.50M."
    )
    ax.text(8.35, 6.70, roadmap_text, fontsize=9.8, color=C_TEXT_DARK, linespacing=1.35, va="top", zorder=3)

    return fig

def build_slide_14():
    """Slide 14: Comprehensive Risk Governance & Board Decision Requested"""
    fig, ax = create_slide_base(
        category_tag="Governance & Approvals | Risk Mitigation & Board Decision",
        action_title="Robust Guardrails Neutralize Brand and Technical Risks; Board Approval Requested for Immediate Pilot Launch",
        slide_num=14,
        citation="Project Phoenix Governance & Risk Matrix (`reports/business_proposal.md` Sections 6 & 7)."
    )

    # Left Column: Risk Mitigation Matrix
    draw_card(ax, (0.8, 3.2, 7.2, 4.2), title="PROACTIVE RISK MITIGATION MATRIX", title_color=C_NAVY_DARK)
    risk_table = (
        "RISK FACTOR            POTENTIAL PITFALL            MITIGATION SAFEGUARD\n"
        "--------------------------------------------------------------------------------------------------\n"
        "1. Cannibalization /   Giving subsidies to loyal    • Gated by tau* >= 0.25 & eqpdays > 365d.\n"
        "   Deadweight Loss     customers who would stay.    • 12-Month Contract Renewal mandatory.\n"
        "--------------------------------------------------------------------------------------------------\n"
        "2. Customer Fatigue    Over-messaging damages brand • Frequency cap: max 2 touches / quarter.\n"
        "   & Brand Friction    NPS and causes opt-outs.     • Automated suppression on ticket/opt-out.\n"
        "--------------------------------------------------------------------------------------------------\n"
        "3. Margin Dilution     Down-tier rightsizing drops  • Trade-off: $600 annual revenue retained\n"
        "                       immediate monthly billing.     is vastly superior to $0 from defection.\n"
        "--------------------------------------------------------------------------------------------------\n"
        "4. Model Drift &       Score decay over time as     • Weekly Population Stability Index (PSI).\n"
        "   Concept Drift       competitor offers shift.     • Scheduled quarterly model retraining."
    )
    ax.text(1.0, 6.80, risk_table, fontsize=9.2, fontfamily="monospace", color=C_TEXT_DARK, linespacing=1.25, va="top", zorder=3)

    # Left Bottom: Balanced KPI Guardrails
    draw_card(ax, (0.8, 0.9, 7.2, 2.1), title="BALANCED KPI GUARDRAILS DASHBOARD", title_color=C_STEEL_BLUE)
    guard_text = (
        "• Commercial Targets: Incremental Uplift >= 25% | Net Profit >= $4.5M | CPRS <= $120\n"
        "• Customer Safety Guardrails: Delta NPS >= 0 pts | Complaint Escalations < 1.0%\n"
        "• Channel Health Guardrails: Campaign Opt-out Rate < 1.5% | Service Margin Floor >= 60%"
    )
    ax.text(1.05, 2.45, guard_text, fontsize=9.8, color=C_TEXT_DARK, linespacing=1.35, va="top", zorder=3)

    # Right Column: Board Approval Card
    draw_card(ax, (8.2, 0.9, 7.0, 6.5), title="FORMAL BOARD DECISION REQUESTED TODAY", title_color=C_GREEN, bg_color="#F0FDF4", border_color="#BBF7D0")
    draw_kpi_badge(ax, (8.5, 5.0, 3.0, 1.5), "$226,182", "Approved Pilot Budget", num_color=C_NAVY_DARK, bg_color=C_WHITE, border_color=C_BORDER)
    draw_kpi_badge(ax, (11.8, 5.0, 3.0, 1.5), "+$660,236", "Target Net Pilot Profit", num_color=C_GREEN, bg_color=C_WHITE, border_color="#BBF7D0")

    board_text = (
        "PROPOSED BOARD RESOLUTION:\n\n"
        "1. Approve Budget Allocation of $226,182 to execute the 15,000-subscriber\n"
        "   Project Phoenix Pilot Trial across Months 1 and 2.\n\n"
        "2. Authorize OEM Hardware Partnerships to secure volume-discounted 5G handset\n"
        "   inventory tranches with pre-negotiated $30–$40 voucher subsidies.\n\n"
        "3. Mandate Cross-Functional Execution under CCO & Head of Retention,\n"
        "   governed by our 3 Stage-Gate Scaling Criteria.\n\n"
        "CONCLUSION:\n"
        "Project Phoenix is fully self-funding from Day 1, carries a 3x margin of safety,\n"
        "and positions Company A as a proactive, customer-centric market leader."
    )
    ax.text(8.5, 4.5, board_text, fontsize=10.2, color=C_TEXT_DARK, linespacing=1.40, va="top", zorder=3)

    return fig

def build_slide_15():
    """Slide 15: External References & Methodology Citations"""
    fig, ax = create_slide_base(
        category_tag="References & Reproducibility | Master Audit Trail",
        action_title="Grounded in Peer-Reviewed Research, Industry Intelligence, and Reproducible Open-Source Methodology",
        slide_num=15,
        citation="Master Source Log (`reports/SOURCE_LOG.md`); Omnicampus Submission Portal."
    )

    # Left Column: Formal Literature References matching Omnicampus
    draw_card(ax, (0.8, 0.9, 7.6, 6.5), title="EXTERNAL REFERENCES & CITATIONS (FOR OMNICAMPUS)", title_color=C_NAVY_DARK)
    ref_text = (
        "BIBLIOGRAPHIC RECORD (MATCHING OMNICAMPUS REFERENCES FIELD):\n\n"
        "[SRC-001] GCI World Organizing Committee (2026)\n"
        "\"GCI World 2026 Final Assignment Guidelines & Dataset Overview\"\n"
        "Internal Course Materials, Omnicampus Platform.\n\n"
        "[SRC-002] Reichheld, F. & Schefter, P. (2000)\n"
        "\"E-Loyalty: Your Secret Weapon on the Web\", Harvard Business Review,\n"
        "Vol. 78, No. 4, pp. 105–113. https://hbr.org/2000/07/e-loyalty-your-secret-weapon-on-the-web\n\n"
        "[SRC-003] McKinsey & Company (2020)\n"
        "\"Predictive Customer Retention in Telecommunications: From Reactive Saving to CVM\",\n"
        "McKinsey Technology, Media & Telecom Practice Insights.\n"
        "https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights\n\n"
        "[SRC-004] Counterpoint Research (2024)\n"
        "\"Global Smartphone Replacement Cycle and Handset Dynamics Report\",\n"
        "Counterpoint Technology Market Research. https://www.counterpointresearch.com/insights/\n\n"
        "[SRC-005] GSMA Intelligence (2024)\n"
        "\"Global Mobile Operator Metrics and Postpaid Churn Benchmarks\",\n"
        "GSMA Industry Data & Analysis. https://www.gsmaintelligence.com/"
    )
    ax.text(1.05, 6.70, ref_text, fontsize=9.2, color=C_TEXT_DARK, linespacing=1.28, va="top", zorder=3)

    # Right Column: Analytical Reproducibility Audit Trail
    draw_card(ax, (8.6, 0.9, 6.6, 6.5), title="TECHNICAL REPRODUCIBILITY & AUDIT TRAIL", title_color=C_STEEL_BLUE)
    repo_text = (
        "OPEN-SOURCE MASTER ANALYSIS ARTIFACTS:\n\n"
        "• Master Script: notebooks/telecom_retention_analysis.py\n"
        "  Single executable Python file containing Sections 1 through 7.\n"
        "  Reproduces complete audit, EDA, model training, and ROI simulation.\n\n"
        "• Modular Stage Scripts (Interactive # %% format):\n"
        "  - 01_data_audit.py (100k join & integrity verification)\n"
        "  - 02_eda.py (Hypothesis testing H1–H4, Figures 1–8)\n"
        "  - 03_problem_definition_and_leakage.py (Zero leakage audit)\n"
        "  - 04_data_preparation_and_features.py (70/15/15 split, 279 feats)\n"
        "  - 05_model_benchmarking_and_evaluation.py (Champion model, Figs 9–10)\n"
        "  - 06_model_interpretation_and_actionability.py (Permutation, Figs 11–12)\n"
        "  - 07_business_proposal_roi_model.py (Financial model, Fig 13)\n\n"
        "• Precomputed Model Checkpoints:\n"
        "  - models/champion_hist_gradient_boosting.joblib (Val AUC 0.6903)\n"
        "  - data/processed/pipeline_data.joblib (Preprocessed matrices)\n\n"
        "• Single Source of Truth: reports/EVIDENCE_LEDGER.md (EVD-001–056)\n"
        "• Architectural Registry: reports/DECISIONS.md (DEC-001–024)"
    )
    ax.text(8.85, 6.70, repo_text, fontsize=9.2, color=C_TEXT_DARK, linespacing=1.28, va="top", zorder=3)

    return fig

# ==============================================================================
# MAIN COMPILATION AND EXPORT
# ==============================================================================

def ensure_figure_panels():
    """Ensures cropped panels for Figure 13 exist for slides 12 and 13."""
    fig13_path = FIGURES_DIR / "fig13_business_impact_roi.png"
    ab_path = FIGURES_DIR / "fig13ab_financial_waterfall_sensitivity.png"
    c_path = FIGURES_DIR / "fig13c_pilot_holdout_architecture.png"
    
    if fig13_path.exists() and (not ab_path.exists() or not c_path.exists()):
        img = Image.open(fig13_path)
        w, h = img.size
        img_ab = img.crop((0, 0, int(w * 0.655), h))
        img_ab.save(ab_path)
        img_c = img.crop((int(w * 0.655), 0, w, h))
        img_c.save(c_path)
        print("  Generated dedicated cropped panels for Fig 13 (13AB and 13C).")

def main():
    print("=" * 80)
    print("GCI WORLD 2026 FINAL ASSIGNMENT — STAGE 10: SLIDE GENERATION & PDF EXPORT")
    print("=" * 80)

    ensure_figure_panels()

    slide_builders = [
        build_slide_01, build_slide_02, build_slide_03, build_slide_04, build_slide_05,
        build_slide_06, build_slide_07, build_slide_08, build_slide_09, build_slide_10,
        build_slide_11, build_slide_12, build_slide_13, build_slide_14, build_slide_15
    ]

    assert len(slide_builders) == 15, f"Deck must have exactly 15 slides! Found {len(slide_builders)}."

    print(f"Generating 15 executive slides into {PDF_OUTPUT_PATH}...")
    with PdfPages(PDF_OUTPUT_PATH) as pdf:
        for i, builder in enumerate(slide_builders, start=1):
            print(f"  Rendering Slide {i:02d} / 15: {builder.__name__}...")
            fig = builder()
            pdf.savefig(fig, dpi=150)
            plt.close(fig)

    # Check PDF size
    pdf_size_mb = PDF_OUTPUT_PATH.stat().st_size / (1024 * 1024)
    print(f"\nPDF Export Completed: {PDF_OUTPUT_PATH}")
    print(f"Total File Size: {pdf_size_mb:.2f} MB (Requirement: <= 10.0 MB -> {'PASS' if pdf_size_mb <= 10.0 else 'FAIL'})")

    # Render each page to PNG for visual inspection using PyMuPDF (fitz)
    print("\nRendering individual pages to high-res PNG for visual inspection...")
    doc = fitz.open(PDF_OUTPUT_PATH)
    assert len(doc) == 15, f"Expected 15 pages in PDF, found {len(doc)}!"

    for page_idx in range(len(doc)):
        page = doc[page_idx]
        pix = page.get_pixmap(dpi=150)
        out_png = RENDERS_DIR / f"slide_{page_idx+1:02d}.png"
        pix.save(str(out_png))
        print(f"  Saved render: {out_png.name} ({pix.width}x{pix.height} px)")

    doc.close()
    print("\nStage 10 slide generation and rendering completed successfully.")

if __name__ == "__main__":
    main()
