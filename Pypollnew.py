import csv
import os

file_to_load = os.path.join('/Users/user/election_results1.csv')
file_to_save = os.path.join('/Users/user/try_again1.txt')

# election_data = open(file_to_load, 'r')


total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)












#file_to_save = os.path.join('/Users/user/try_again1.txt')
#outfile = open(file_to_save, "w")
#outfile.write('helloooo')
#outfile.close()

#file_to_save = os.path.join('/Users/user/try_again1.txt')
#outfile = open(file_to_save, "w")
#outfile.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
#outfile.close()






