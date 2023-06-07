import csv
from datetime import datetime

# Get the current date in the format "YYYY-MM-DD"
current_date = datetime.now().strftime("%Y-%m-%d")

# Define the file path and name
file_name = f"{current_date}.csv"
file_path = f"/Users/yipingzhou/Chat-GPT/{file_name}"  # Replace with your desired directory path

# Define the starting row and column
start_row = 5
start_column = 5

# Define the data to be written to the file
data = [
    ["Value 1", "Value 2", "Value 3"],
    ["Value 4", "Value 5", "Value 6"],
    ["Value 7", "Value 8", "Value 9"],
]

# Check if the file already exists, otherwise create a new file
try:
    with open(file_path, "r") as file:
        # File exists, do nothing
        pass
except FileNotFoundError:
    # File doesn't exist, create a new file with headers
    headers = ["Header 1", "Header 2", "Header 3"]
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

# Append data to the file starting from the specified row and column
with open(file_path, "a", newline="") as file:
    writer = csv.writer(file)
    for i, row in enumerate(data):
        writer.writerow([""] * (start_column - 1) + row)

print(f"Data written to {file_path} successfully!")


