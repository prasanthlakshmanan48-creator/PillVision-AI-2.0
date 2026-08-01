from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

styles=getSampleStyleSheet()

def create_pdf(title,content,filename):

    pdf=SimpleDocTemplate(filename)

    story=[]

    story.append(
        Paragraph(title,styles["Heading1"])
    )

    story.append(
        Spacer(1,20)
    )

    for line in content.split("\n"):

        story.append(
            Paragraph(line,styles["BodyText"])
        )

    pdf.build(story)

    return filename
