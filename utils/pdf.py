from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

def create_pdf(title, content, filename):

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph(f"<b>{title}</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(content.replace("\n", "<br/>"), styles["BodyText"]))

    pdf.build(story)

    return filename
