from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = HexColor("#1565C0")

heading_style = styles["Heading2"]
heading_style.textColor = HexColor("#1565C0")

normal_style = styles["BodyText"]


def create_pdf(title, content, filename):

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("💊 PillVision AI", title_style))
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph(title, heading_style))
    story.append(Spacer(1, 0.15 * inch))

    for line in content.split("\n"):

        if line.strip() != "":
            story.append(
                Paragraph(line, normal_style)
            )

    story.append(Spacer(1, 0.3 * inch))

    story.append(
        Paragraph(
            "<b>Disclaimer:</b> "
            "This report is AI-generated and intended for educational purposes only. "
            "Always consult a qualified healthcare professional before taking any medication.",
            normal_style
        )
    )

    pdf.build(story)

    return filename
