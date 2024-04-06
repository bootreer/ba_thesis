import pandas as pd
import sys


def average_iops_two_parts(csv_filepath, n):
    # Load the CSV file
    df = pd.read_csv(csv_filepath)

    # Check if 'iops' column exists
    if "iops" not in df.columns:
        raise ValueError("Column 'iops' does not exist in the CSV file.")

    # Split the DataFrame into two parts: The first 'n' rows and the rest
    first_n_df = df["iops"].head(n)
    rest_df = df["iops"].iloc[n:]

    # Calculate the average of the first 'n' iops values
    first_n_avg = first_n_df.mean()

    # Calculate the average of the rest of the iops values
    rest_avg = rest_df.mean()

    return first_n_avg, rest_avg


if __name__ == "__main__":
    csv_filepath = sys.argv[1]
    n = int(sys.argv[2])
    try:
        first_n_avg, rest_avg = average_iops_two_parts(csv_filepath, n)
        print(f"The average of the first {n} 'iops' values is: {first_n_avg}")
        print(f"The average of the rest of the 'iops' values is: {rest_avg}")
    except Exception as e:
        print(f"An error occurred: {e}")
