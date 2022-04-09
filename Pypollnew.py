import csv
import os

file_to_load = os.path.join('/Users/user/election_results1.csv')

election_data = open(file_to_load, 'r')

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Print the file object.
    headers = next(file_reader)
    print(headers)












file_to_save = os.path.join('/Users/user/try_again1.txt')
outfile = open(file_to_save, "w")
outfile.write('helloooo')
outfile.close()

file_to_save = os.path.join('/Users/user/try_again1.txt')
outfile = open(file_to_save, "w")
outfile.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
outfile.close()






