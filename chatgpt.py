import os
import pandas
directory = '/workspaces/Chat-GPT'

# Get all files in the directory
files = os.listdir(directory)

# Iterate over the files and print their names
for file in files:
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):
        print(file_path)
