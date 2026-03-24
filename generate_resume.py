from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_CENTER, TA_RIGHT

OUTPUT = r"d:\校务\重要人大模版\cv\Siyuan Chang_Resume.pdf"

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
    '<a href="https://csy24.github.io/" color="#1155CC">'
    '<u>https://csy24.github.io/</u></a>'
)
story.append(Paragraph(contact2, contact_style))
story.append(sp(5))

# ── Education ────────────────────────────────────────────────────────────────
story += sec("Education")
story.append(two_col(
    "<b>Renmin University of China, Department of Statistics</b>",
    "Sep 2024 – Present",
))
story.append(Paragraph("Data Science and Big Data Technology", body_style))
story.append(b("GPA: 3.9, Top 5% in major"))
story.append(b("<b>Programming:</b> Proficient in C++ and Python; full score in Data Structures"))
story.append(b(
    "<b>Mathematics:</b> Full scores in Mathematical Analysis I, II &amp; III, "
    "Advanced Algebra, and Probability Theory"
))
story.append(b(
    "<b>Language:</b> CET-4: 688, CET-6: 656; full scores in all college English courses; "
    "second foreign language: French"
))
story.append(sp(3))

# ── Academic Papers ──────────────────────────────────────────────────────────
story += sec("Academic Papers")

story.append(Paragraph(
    "• Qian Hong, <b>Siyuan Chang</b>, Xiao Zhou. "
    "\"WED-Net: A Weather-Effect Disentanglement Network with Causal Augmentation "
    "for Urban Flow Prediction.\" "
    '<a href="https://arxiv.org/abs/2601.22586" color="#1155CC"><u>arXiv:2601.22586</u></a>. '
    "<i>WWW 2026</i>.",
    body_style,
))
story.append(Paragraph(
    "• Xixian Yong, <b>Siyuan Chang</b>, Xiao Zhou, Zihe Wang, Yingying Zhang, "
    "Yefeng Zheng, Xian Wu. "
    "\"Controllable Affective Generation via Latent Vector Steering.\" "
    "<i>Under review at ACL 2026</i>.",
    body_style,
))
story.append(sp(3))

# ── Honors & Awards ──────────────────────────────────────────────────────────
story += sec("Honors & Awards")

awards = [
    ("Oct 2025", "First-class Academic Excellence Scholarship, Renmin University of China"),
    ("Nov 2025", "Third Prize (National Level), National Mathematics Competition for College Students"),
    ("Sep 2025",
     "Led team as captain in the 1st RUC AI Agent Innovation Application Competition; "
     "work \"Alpha Adventure Alliance — Three-Body Pass Challenge\" received Excellence Award"),
    ("Sep 2025",
     "Third-class Scholarship for Social Work and Volunteer Service Backbone, "
     "School of Statistics, RUC, 2025"),
]
for date, desc in awards:
    story.append(Paragraph(f"• <b>{date}</b>  {desc}", body_style))

story.append(sp(3))

# ── Personal Skills & Activities ─────────────────────────────────────────────
story += sec("Personal Skills & Activities")

skills = [
    ("<b>Academic:</b>",
     "Independently completed the \"Innovation Cup\" Science and Technology Competition; "
     "work: \"Academic Quality Crisis in the AI Era — LLM-Assisted Writing Effects "
     "and Paper Quality Detection System\""),
    ("<b>Technical:</b>",
     "Proficient in R, SPSS; proficient in LaTeX for academic typesetting; "
     "proficient in Excel, PowerPoint and other office software"),
    ("<b>Organizational:</b>",
     "Head of Theory Department, Party Building Promotion Committee, "
     "School of Statistics, Renmin University of China"),
    ("<b>Contemporary Insight:</b>",
     "April 2025 – researched the balance between content quality and traffic monetization "
     "in online videos; awarded \"Outstanding Individual\" in freshman seminar"),
    ("<b>Party Membership:</b>",
     "Dec 2025, selected as a Party development target; "
     "Mar 2025, awarded \"Outstanding Communist Youth League Member\" of RUC"),
    ("<b>Volunteer Work:</b>",
     "Accumulated 130 hours of volunteer service; participated in RUC's "
     "Middle School Collaborative Education Social Practice Project "
     "and received \"Excellent Project Completion\" recognition"),
]
for label, content in skills:
    story.append(Paragraph(f"• {label} {content}", body_style))

# ════════════════════════════════════════════════════════════════════════════
doc.build(story)
print(f"PDF generated: {OUTPUT}")
