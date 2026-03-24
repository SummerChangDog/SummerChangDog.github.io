from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_CENTER, TA_RIGHT

OUTPUT = r"Siyuan Chang_Resume.pdf"

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
    '<a href="https:///SummerChangDog.github.io/" color="#1155CC">'
    '<u>https:///SummerChangDog.github.io/</u></a>'
)
story.append(Paragraph(contact2, contact_style))
story.append(sp(5))

# ── Education ────────────────────────────────────────────────────────────────
story += sec("Education")
story.append(two_col(
    "<b>Renmin University of China, School of Statistics</b>",
    "Sep 2024 – Present",
))
story.append(Paragraph("Data Science and Big Data Technology", body_style))
story.append(b("GPA: 3.9/4.0, Top 5% in major"))
story.append(b("<b>Programming:</b> Proficient in C++ and Python; full score in Data Structures"))
story.append(b(
    "<b>Mathematics:</b> Full scores in Mathematical Analysis I, II &amp; III, "
    "Advanced Algebra, and Probability Theory"
))
story.append(b(
    "<b>Language:</b> CET-4: 688, CET-6: 656; full scores in all college English courses."
    "second foreign language: French"
))
story.append(b(
    "<b>Prize:</b> National Third Prize, National Mathematics Competition for College Students, 2025"
))
story.append(b(
    "<b>Honors:</b> First-class Academic Excellence Scholarship, RUC, 2025"
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

# ── Research Experiences ─────────────────────────────────────────────
story += sec("Research Experiences")
story.append(b("Advisor: <a href='https://xiaozhoucam.github.io/' color='#1155CC'><u>Xiao Zhou</u></a>, Gaoling School of Artificial Intelligence, Renmin University of China"))
skills = [
    ("<b>Academic Quality Crisis in the AI Era--LLM-Assisted Writing Effects and Paper Quality Detection System</b>",
     "Establish a 4-dimensional paper quality assessment framework based on LLM-as-Judge, achieve hierarchical measurement of reference hallucination rates, and identify the mediating effect of hallucination rates on paper quality."),
    
    ("<b>WED-Net: A Weather-Effect Disentanglement Network with Causal Augmentation for Urban Flow Prediction</b>",
     "Disentangle intrinsic and weather-induced traffic patterns via attention mechanisms, assisted by a weather discriminator and a causal data augmentation strategy that preserves causal structures while perturbing non-causal components."),
    
    ("<b>Controllable Affective Generation via Latent Vector Steering</b>",
     "Propose EmoVec, a post-hoc framework to achieve controllable affective generation in large language models via latent vector steering, addressing the emotional flattening issue caused by alignment techniques without weight tuning or retraining"
),
]
for label, content in skills:
    story.append(Paragraph(f"• {label}", body_style))
    for sub in content.replace(";<", "\x00<").replace("; ", "\x00").replace(";", "\x00").split("\x00"):
        sub = sub.strip()
        if sub:
            story.append(Paragraph(f"  · {sub}", body_style))
story.append(sp(3))

# ── Research Interests ─────────────────────────────────────────────
story += sec("Research Interests")

skills = [
    ("<b>Machine Learning</b>",
     "Pursuing generalizable knowledge discovery from <b>unlabeled or sparsely annotated data</b>.;"
     "Embedding <b>graph-structured</b> data into low-dimensional vector spaces while preserving topological and semantic properties."),
    
    ("<b>Data Mining</b>",
     "Characterizing interaction patterns and evolutionary dynamics in <b>social network</b>.;"
     "Extracting predictive and descriptive patterns from <b>sequential time-stamped</b> data.;"
     "Integrateing <b>heterogeneous information</b> across text, image, graph and other modalities for robust knowledge extraction."),
    
    ("<b>Optimization</b>",
     "Solving <b>Supply chain</b> under uncertainty for resilient and cost-efficient global logistics.;"
     "Optimizing model architectures to improve the efficiency and scalability of <b>personalized recommendation systems</b>."),
    
    ("<b>Social Computing</b>",
     "Building data-driven and AI-enabled frameworks to optimize <b>urban traffic</b> operation and management.;"
     "Revealing the <b>diffusion laws of information</b> and viewpoints in online social systems.;"
     "AI-powered <b>sentiment analysis</b> from textual and multimodal data."),
]

for label, content in skills:
    story.append(Paragraph(f"• {label}", body_style))
    for sub in content.replace(";<", "\x00<").replace("; ", "\x00").replace(";", "\x00").split("\x00"):
        sub = sub.strip()
        if sub:
            story.append(Paragraph(f"  · {sub}", body_style))

# ════════════════════════════════════════════════════════════════════════════
doc.build(story)
print(f"PDF generated: {OUTPUT}")

