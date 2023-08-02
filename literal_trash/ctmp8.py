import os

# List all files in the directory
directory = "C:/Users/USER/OneDrive/Desktop/Temp/Random_Programming/trash_codes-1"
files = os.listdir(directory)
for file in files:
    print(file)