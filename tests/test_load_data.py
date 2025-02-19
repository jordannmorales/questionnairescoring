from src.data_loading import load_data

def test_loading(): # you only need parameters if you are passing data into that function, so this one does not need a parameter
    df = load_data("data/test_data.csv") # signing this variable some data, this data is the function we built earlier using the CSV file, passing in the string which is the CSV file
    print(df) # printing the file to the terminal

if __name__ == "__main__":
    test_loading()