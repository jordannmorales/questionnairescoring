import pandas as pd


# command + option + L formats code on pycharm

# def - defines a function, functions are like small jobs in a file that work together to complete one greater task

# this line of code defines a function

# everything in the parentheses after the function is defined is a parameter

# everything after the arrow is what the function will return

def load_data(file_path: str) -> pd.DataFrame:

    """
        Loads participant responses from a CSV or Excel file into a pandas DataFrame.

        :param file_path: The path to the CSV or Excel file containing questionnaire data.
        :return: A pandas DataFrame with the loaded data.

        This function infers the file type from the file extension.
        If the file ends with '.csv', it uses pd.read_csv().
        If the file ends with '.xlsx', it uses pd.read_excel().
        Otherwise, it raises a ValueError.
        """

    if file_path.endswith('.csv'): # checking if a .csv file is being loaded
        # .read_csv is a function that comes from the pandas library
        df = pd.read_csv(file_path) # if it is, load the file using pd.read_csv()
    elif file_path.endswith('.xlsx'): # this will be what is at the end of the document name (ex. .pdf, .docx, etc)
        df = pd.read_excel(file_path) # the function to read the excel file is different then the .____ seen above
    else:
        raise ValueError('Unsupported file type. Please provide a CSV or Excel File')
    return df # used at the end of every function, so that the computer gets that value back