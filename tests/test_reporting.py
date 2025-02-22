# tests/test_reporting.py

from src.data_loading import load_data
from src.scoring.scoring_logic import score_phq9
from src.reporting.report_generator import generate_pdf_report

def test_report_generation():
    # 1. Load the CSV
    df = load_data("data/test_data.csv")

    # 2. Score it
    df_scored = score_phq9(df)

    # 3. Generate the PDF report
    generate_pdf_report(df_scored, output_pdf="reports/summary_report.pdf")

    print("PDF report generated at reports/summary_report.pdf")

if __name__ == "__main__":
    test_report_generation()
