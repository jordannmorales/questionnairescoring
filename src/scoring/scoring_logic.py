import pandas as pd

SCORING_RULES = {
    "PHQ9": {
        "num_questions": 9,
        "severity_cutoffs": {
            "minimal": (0, 4),
            "mild": (5, 9),
            "moderate": (10, 14),
            "moderately severe": (15, 19),
            "severe": (20, 27)

        }
    }

}


def score_phq9(df: pd.DataFrame) -> pd.DataFrame:
    # creating a list of the required columns ['q1', 'q2' ... 'q9']
    required_cols = [f"q{i}" for i in range(1, 10)]
    # f means to print
    # for i means that the numbers after it will be used in the string "q{i}"
    # str is 2 characters to infinity - str is a type of data (char, int are other types of data)
    # validating that each required column exists in the dataframe (which is the parameter passed to the function)
    for col in required_cols:
        if col not in df.columns:
            # if teh columns is not in the dataframe, raise a ValueError
            raise ValueError(f"Missing required column: {col}")

# calculate the total PHQ-9 score by summing question columns (q1 - q9) for each row
    df["phq9_total_score"] = df[required_cols].sum(axis=1)

    # map is a key value pair (in this example, number we are getting from the above calculation is the key and value is the severity levels from above
    def map_severity(score):

        # assigning the cutoffs from the chapter (severity_cutoffs) from the book (PHQ9) which was written above
        cutoffs = SCORING_RULES["PHQ9"]["severity_cutoffs"]


        for severity_label, (low, high) in cutoffs.items():
            # the score number has to be higher than the low value but lower than the high value
            if low <= score <= high:
                # label will return with some like "moderately severe" if the score was 16
                return severity_label
        return "Unknown"

    # apply the map severity function to each total score to get a severity label
    df["phq9_severity"] = df["phq9_total_score"].map(map_severity)
    # return the updated dataframe, now with total score and severity columns (labels)
    return df

