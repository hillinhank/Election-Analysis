
from fileinput import close
import os
import csv
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("/Users/user/election_analysis.txt")
file_to_load = os.path.join("/Users/user/election_results-2.csv")
# Using the open() function with the "w" mode we will write data to the file.
txt_file = open(file_to_save, "w")
election_data = open(file_to_load,"r")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n-----------\nArapahoe\nDenver\nJefferson")

txt_file.close()


total_votes = 0

with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # print(headers)
    for row in file_reader:
        total_votes += 1

print(total_votes)






















