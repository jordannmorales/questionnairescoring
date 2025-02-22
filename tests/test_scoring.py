# tests/test_scoring.py

from src.data_loading import load_data
from src.scoring.scoring_logic import score_phq9


def test_score_phq9():
    # Load the CSV file using our data loader.
    # Adjust the path if necessary (see note below).
    df = load_data("data/test_data.csv")

    # Apply the PHQ-9 scoring logic to the DataFrame.
    scored_df = score_phq9(df)

    # Print the results to verify scoring:
    # You should see columns for participant_id, phq9_total_score, and phq9_severity.
    print(scored_df[["participant_id", "phq9_total_score", "phq9_severity"]])


if __name__ == "__main__":
    test_score_phq9()
