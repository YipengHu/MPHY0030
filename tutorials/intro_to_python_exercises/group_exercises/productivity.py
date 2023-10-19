import os
import csv
import sys
from datetime import date
import webbrowser

# function to modify a single cell
def csv_modify_cell(csv_path, row, column, new_entry):
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        all_lines = list(reader)
    all_lines[row][column] = new_entry
    with open(csv_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(all_lines)

# function to get the value in a single cell
def csv_get_single_cell(csv_path, row, column):
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        all_lines = list(reader)
    return all_lines[row][column]

# function to split strings using ;
def string_splitter(string):
    return string.split(';')

# function to join strings using ;
def string_joiner(strings):
    return ';'.join(strings)

# function to add new line for new shortcut to csv
def shortcut_adder(shortcut_name, urls, csv_path):
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        all_lines = list(reader)
    all_lines.append([shortcut_name, urls])
    with open(csv_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(all_lines)

# function to get index of string in a list of strings
def str_index_in_list(list_input, string_input):
    try:
        index = list_input.index(string_input)
    except ValueError:
        index = None
    return index

# function to add new line for new shortcut to csv if duplicate does not exist
def shortcut_adder_with_duplicates(shortcut_name, urls, csv_path):
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        all_lines = list(reader)
    shortcut_names = [elem[0] for elem in all_lines]
    
    duplicate_index = str_index_in_list(shortcut_names, shortcut_name)
    if duplicate_index is not None:
        all_lines[duplicate_index][1] = urls
    else:
        all_lines.append([shortcut_name, urls])
    
    with open(csv_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(all_lines)

# open url / ; separated list of urls
def url_opener(urls):
    urls = string_splitter(urls)
    urls = [elem.strip(' ') for elem in urls]
    for url in urls:
        webbrowser.open_new(url)


# Path to CSV file
csv_file_path = r'./'
csv_file_name = r'productivity.csv'
csv_path = os.path.join(csv_file_path, csv_file_name)

# =============================================================================
# Setup - comment out the code below after the first run
# =============================================================================

# CSV creation 
# with open(csv_path, 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Shortcut Name', 'URL'])

# modify value of cell in first row, second column
# csv_modify_cell(csv_path, row=0, column=1, new_entry='URL/s')

# Populate the CSV file with some fake data
# with open(csv_path, 'r') as file:
#     reader = csv.reader(file)
#     all_lines = list(reader)
# all_lines.append(['research', r'https://scholar.google.com/; https://pubmed.ncbi.nlm.nih.gov/; https://www.sciencedirect.com/'])
# all_lines.append(['search', 'https://www.google.com/'])
# with open(os.path.join(csv_file_path, csv_file_name), 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(all_lines)
    
# =============================================================================
# 
# =============================================================================

# on the command line: python3 productivity.py 'r' 'research'
# on the command line: python3 productivity.py 'w' 'mphy0030' 'https://moodle.ucl.ac.uk/; https://github.com/YipengHu/MPHY0030'

mode = sys.argv[1] # specifies read or write to open or add shortcuts
shortcut_name = sys.argv[2] # shortcut name

try:
    shortcut_urls = sys.argv[3] # urls, if mode is write
except IndexError:
    pass

if mode == 'r':
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        all_lines = list(reader)
        
    shortcut_names = [elem[0] for elem in all_lines]  
    index = str_index_in_list(shortcut_names, shortcut_name)

    urls = all_lines[index][1]
    
    url_opener(urls)

elif mode == 'w':
    shortcut_adder_with_duplicates(shortcut_name, shortcut_urls, csv_path)