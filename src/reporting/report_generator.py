# src/reporting/report_generator.py

# importing all the libraries to build the charts and pdf generating
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, Spacer
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt

# defining the function of generating the score distribution chart - png is an image files - the out path path will be creating an image file for the scoring distribution
def generate_score_distribution_chart(df, output_path="score_distribution.png"):
    """
    Generates a bar chart (or histogram) of the 'phq9_total_score' column in df
    and saves it as a PNG file at output_path.
    """
    scores = df["phq9_total_score"] # variable scores is being assigned to the data form of the phq9 total score

    # Let's do a histogram of total scores
    plt.figure(figsize=(6, 4))
    plt.hist(scores, bins=range(0, 29), edgecolor="black", alpha=0.7)
    plt.title("Distribution of PHQ-9 Total Scores")
    plt.xlabel("Total Score")
    plt.ylabel("Count of Participants")

    # Save chart as a PNG
    plt.savefig(output_path)
    plt.close()


def generate_pdf_report(df, output_pdf="reports/summary_report.pdf"):
    """
    Generates a PDF report with:
    1) A table of participant data (ID, Q1..Q9, total score, severity).
    2) A chart showing the distribution of total scores across participants.
    """
    # Ensure the reports directory exists
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

    # Create the PDF document
    doc = SimpleDocTemplate(output_pdf, pagesize=LETTER)
    styles = getSampleStyleSheet()
    story = []

    # 1. Title
    title = Paragraph("PHQ-9 Summary Report", styles["Title"])
    story.append(title)
    story.append(Spacer(1, 20))  # Add some vertical space

    # 2. Create a table of participant data
    # Let's define the table header
    table_header = [
        "Participant ID",
        "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9",
        "Total Score",
        "Severity"
    ]

    # Build the rows for each participant
    table_data = [table_header]
    for _, row in df.iterrows():
        row_data = [
            row["participant_id"],
            row["q1"], row["q2"], row["q3"], row["q4"], row["q5"], row["q6"], row["q7"], row["q8"], row["q9"],
            row["phq9_total_score"],
            row["phq9_severity"]
        ]
        table_data.append(row_data)

    # Convert table_data into a ReportLab Table object
    participant_table = Table(table_data)

    # Add some basic styling
    participant_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ]))

    story.append(participant_table)
    story.append(Spacer(1, 20))

    # 3. Generate and insert the score distribution chart
    chart_path = "reports/score_distribution.png"
    generate_score_distribution_chart(df, output_path=chart_path)

    # Add the image to the PDF
    # (width, height) can be adjusted based on the original figure size
    story.append(Image(chart_path, width=400, height=300))

    # Build the PDF
    doc.build(story)
