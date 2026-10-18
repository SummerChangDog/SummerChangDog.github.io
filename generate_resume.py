from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_CENTER, TA_RIGHT


OUTPUT = str(Path(__file__).resolve().with_name("Siyuan Chang_Resume.pdf"))

# ── Page setup ───────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=0.70 * inch,
    rightMargin=0.70 * inch,
    topMargin=0.55 * inch,
    bottomMargin=0.55 * inch,
)

W = letter[0] - 1.40 * inch   # usable width
BLACK = colors.HexColor("#000000")

# ── Fonts: use built-in Times (= Times New Roman) ────────────────────────────
TNR       = "Times-Roman"
TNR_BOLD  = "Times-Bold"
TNR_ITAL  = "Times-Italic"
HELV_BOLD = "Helvetica-Bold"   # keep Helvetica only for the name header

FS   = 10.5   # base font size
LH   = 14     # base line height

# ── Styles ───────────────────────────────────────────────────────────────────
name_style = ParagraphStyle(
    "Name", fontName=HELV_BOLD, fontSize=21, leading=25,
    alignment=TA_CENTER, textColor=BLACK, spaceAfter=2,
)
contact_style = ParagraphStyle(
    "Contact", fontName=TNR, fontSize=10, leading=13,
    alignment=TA_CENTER, textColor=BLACK, spaceAfter=1,
)
sec_hdr_style = ParagraphStyle(
    "SecHdr", fontName=TNR_BOLD, fontSize=11.5, leading=15,
    textColor=BLACK, spaceBefore=5, spaceAfter=1,
)
body_style = ParagraphStyle(
    "Body", fontName=TNR, fontSize=FS, leading=LH,
    textColor=BLACK, leftIndent=0, spaceAfter=1,
)

# ── Helpers ──────────────────────────────────────────────────────────────────
def hr():
    return HRFlowable(width="100%", thickness=0.8, color=BLACK,
                      spaceBefore=1, spaceAfter=3)

def sec(title):
    return [Paragraph(title, sec_hdr_style), hr()]

def b(text):
    return Paragraph(f"• {text}", body_style)

def sp(h=3):
    return Spacer(1, h)

def two_col(left_txt, right_txt, lf=TNR_BOLD, rf=TNR, fs=FS):
    """Two-column row perfectly flush with the left page margin."""
    ls = ParagraphStyle("L", fontName=lf, fontSize=fs, leading=LH, leftIndent=0)
    rs = ParagraphStyle("R", fontName=rf, fontSize=fs, leading=LH,
                        alignment=TA_RIGHT, leftIndent=0)
    t = Table(
        [[Paragraph(left_txt, ls), Paragraph(right_txt, rs)]],
        colWidths=[W * 0.70, W * 0.30],
        # hAlign='LEFT' ensures the table itself sits at the left margin
        hAlign='LEFT',
    )
    t.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return t

# ════════════════════════════════════════════════════════════════════════════
# Story
# ════════════════════════════════════════════════════════════════════════════
story = []

# ── Header ───────────────────────────────────────────────────────────────────
story.append(Paragraph("Siyuan Chang", name_style))

contact1 = (
    f'Email: <a href="mailto:csy24@ruc.edu.cn" color="#1155CC">'
    f'<u>csy24@ruc.edu.cn</u></a>'
    f' | Phone: +86 17372238022'
)
story.append(Paragraph(contact1, contact_style))

contact2 = (
    'Renmin University of China | Homepage: '
    '<a href="https://SummerChangDog.github.io/" color="#1155CC">'
    '<u>https://SummerChangDog.github.io/</u></a>'
)
story.append(Paragraph(contact2, contact_style))
story.append(sp(4))

# ── Education ────────────────────────────────────────────────────────────────
story += sec("Education")
story.append(two_col(
    "<b>Renmin University of China, School of Statistics</b>",
    "Sep 2024 – Present",
))
story.append(Paragraph("Data Science and Big Data Technology", body_style))
story.append(b("<b>GPA:</b> 3.9/4.0, Top 5% in major"))
# story.append(b("<b>Programming:</b> Proficient in C++ and Python; full score in Data Structures"))
# story.append(b(
#     "<b>Mathematics:</b> Full scores in Mathematical Analysis I, II &amp; III, "
#     "Advanced Algebra, and Probability Theory"
# ))
story.append(b(
    "<b>Selected Coursework:</b> Machine Learning Theory; Advanced Optimization; High-Dimensional Statistics; Probability Theory; Stochastic Processes; Reinforcement Learning; Deep Learning; Parallel Computing; Data Structures."
))
story.append(b(
    "<b>Language:</b> CET-4: 688, CET-6: 656;"
    "second foreign language: French"
))
story.append(b(
    "<b>Honor:</b> First-class Academic Excellence Scholarship, RUC, 2025 & 2026"
))
story.append(sp(2))

# ── Academic Papers ──────────────────────────────────────────────────────────
story += sec("Academic Papers")

story.append(Paragraph(
    "[1] WED-Net: A Weather-Effect Disentanglement Network with Causal Augmentation for Urban Flow Prediction.<br/>"
    "Qian Hong, <b>Siyuan Chang</b>, Xiao Zhou.<br/>"
    "<i>WWW 2026</i>."
    '<a href="https://arxiv.org/abs/2601.22586" color="#1155CC"><u> Paper Link</u></a>. ',
    body_style,
))
story.append(Paragraph(
    "[2] Controllable Affective Generation via Latent Vector Steering.<br/>"
    "Xixian Yong, <b>Siyuan Chang</b>, Xiao Zhou, Zihe Wang, Yingying Zhang,"
    "Yefeng Zheng, Xian Wu.<br/>"
    "<i>EMNLP 2026</i>."
    '<a href="https://arxiv.org/abs/2608.25569" color="#1155CC"><u> Paper Link</u></a>. ',
    body_style,
))
story.append(sp(2))

# ── Research Experiences ─────────────────────────────────────────────
story += sec("Research Experiences")

# 样式设置
title_style = ParagraphStyle(
    "ResearchTitle",
    parent=body_style,
    fontSize=11,
    leading=14,
    spaceAfter=0,
)

date_style = ParagraphStyle(
    "ResearchDate",
    parent=title_style,
    alignment=TA_RIGHT,
)

advisor_style = ParagraphStyle(
    "ResearchAdvisor",
    parent=body_style,
    spaceAfter=3,
)

bullet_style = ParagraphStyle(
    "ResearchBullet",
    parent=body_style,
    leftIndent=14,
    firstLineIndent=-10,
    spaceAfter=3,
)

# 添加一段研究经历
def add_research(title, date, advisor, bullets):
    table = Table(
        [[
            Paragraph(f"<b>{title}</b>", title_style),
            Paragraph(date, date_style),
        ]],
        colWidths=[doc.width - 125, 125],
    )

    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    story.append(table)
    story.append(Paragraph(f"<i>Advisor: {advisor}</i>", advisor_style))

    for bullet in bullets:
        story.append(Paragraph(f"&#8226; {bullet}", bullet_style))

    story.append(sp(3))


# 1. Bandit Convex Optimization
add_research(
    title="Bandit Convex Optimization with Gradient Variation",
    date="Sep. 2026 – Present",
    advisor=(
        '<a href="https://www.lamda.nju.edu.cn/zhaop/" color="#1155CC">'
        '<u>Peng Zhao</u></a>'
    ),
    bullets=[
        "Investigate high-probability regret bounds for two-point BCO against adaptive adversaries.",
        "Extend gradient-variation-based bandit learning to bilinear games.",
        "Explore improved dimension dependence for regret bounds under convex regret."
    ]
)


# 2. Controllable Affective Generation
add_research(
    title="Controllable Affective Generation via Latent Vector Steering",
    date="Sep. 2025 – Dec. 2025",
    advisor=(
        '<a href="https://xiaozhoucam.github.io/" color="#1155CC">'
        '<u>Xiao Zhou</u></a>'
    ),
    bullets=[
        "Propose EmoVec, a post-hoc framework for controllable affective generation in LLMs via latent vector steering, addressing emotional flattening caused by alignment techniques without weight tuning or retraining."
    ]
)


# 3. WED-Net
add_research(
    title="WED-Net: A Weather-Effect Disentanglement Network with Causal Augmentation for Urban Flow Prediction",
    date="Jun. 2025 – Aug. 2025",
    advisor=(
        '<a href="https://xiaozhoucam.github.io/" color="#1155CC">'
        '<u>Xiao Zhou</u></a>'
    ),
    bullets=[
        "Disentangle weather-induced traffic patterns via attention mechanisms, with a weather discriminator and a causal data augmentation strategy that preserves causal structures while perturbing non-causal components."
    ]
)
story.append(sp(2))

# ── Research Interests ─────────────────────────────────────────────
story += sec("Research Interests")

story.append(Paragraph(
    "<b>Online Learning</b>: Developing algorithms that remain effective "
    "and computationally efficient over long horizons, even under uncertainty "
    "and limited information.",
    body_style,
))

interest_style = ParagraphStyle(
    "InterestBullet", parent=body_style, leftIndent=18, firstLineIndent=-10,
)

for text in [
    "<b>Game Theory</b>: No-regret learning and equilibrium convergence "
    "in multi-agent systems, with a focus on learning dynamics, gradient "
    "variation, and parameter-free algorithms.",

    "<b>Bandit Learning</b>: Regret minimization under limited feedback, "
    "focusing on the exploration–exploitation tradeoff and obtaining regret "
    "guarantees against both oblivious and adaptive adversaries.",

    "<b>Reinforcement Learning</b>: Sequential decision-making under uncertainty, "
    "with a particular interest in its fundamental connections to online "
    "learning, game theory, and bandit learning.",
]:
    story.append(Paragraph(f"• {text}", interest_style))

# ════════════════════════════════════════════════════════════════════════════
doc.build(story)
print(f"PDF generated: {OUTPUT}")

