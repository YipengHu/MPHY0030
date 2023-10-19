import os
import csv
import sys
from datetime import date

# basal metabolic rate calculator; eq from https://en.wikipedia.org/wiki/Harris%E2%80%93Benedict_equation
def bmr_calculator(age, height, weight, mf):
    '''
    age : age in years
    height : height in cm
    weight : weight in kg
    mf : 'm' or 'f'
    '''
    bmr_base = (10 * weight) + (6.25 * height) - (5 * age) 
    if mf == 'm':
        bmr = bmr_base + 5
    elif mf == 'f':
        bmr = bmr_base - 161
    return bmr

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

# date utility functions
def get_current_date():
    return date.today()
def date_to_string(date_input):
    date_str = str(date_input)
    dd_mm_yyyy = '-'.join(date_str.split('-')[::-1])
    return dd_mm_yyyy
def string_to_date(date_str):
    dd, mm, yyyy = date_str.split('-')
    py_date = date(int(yyyy), int(mm), int(dd))
    return py_date

# function to get index of string in a list of strings
def str_index_in_list(list_input, string_input):
    try:
        index = list_input.index(string_input)
    except ValueError:
        index = None
    return index

# Path to CSV file
csv_file_path = r'./'
csv_file_name = r'calories.csv'
csv_path = os.path.join(csv_file_path, csv_file_name)

# =============================================================================
# Setup - comment out the code below after the first run
# =============================================================================

# CSV creation 
# with open(csv_path, 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Date', 'Calories'])

# modify value of cell in first row, second column
# csv_modify_cell(csv_path, row=0, column=1, new_entry='Calories (kCal)')

# Populate the CSV file with some fake data
# with open(csv_path, 'r') as file:
#     reader = csv.reader(file)
#     all_lines = list(reader)
# all_lines[0][1] = 'Calories (kCal)'
# all_lines.append(['01-10-2023', '+200'])
# all_lines.append(['02-10-2023', '+100'])
# all_lines.append(['03-10-2023', '-50'])
# all_lines.append(['04-10-2023', '-100'])
# with open(os.path.join(csv_file_path, csv_file_name), 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(all_lines)
    
# =============================================================================
# 
# =============================================================================

# read all lines in csv file
with open(os.path.join(csv_file_path, csv_file_name), 'r') as file:
    reader = csv.reader(file)
    all_lines = list(reader)

# get only date in first column from all lines
dates_list = [elem[0] for elem in all_lines]

# get today's date in correct format
date_today = get_current_date()
date_str = date_to_string(date_today)

# get index of current date in dates column 
index = str_index_in_list(dates_list, date_str)

# calculate bmr
height = 180
weight = 68
age = 25
mf = 'm'
bmr = int(bmr_calculator(age, height, weight, mf))

# get the input from the CLI
# on command line: python3 calorie_tracker.py -200
input_calorie_delta = int(sys.argv[1]) # if not CLI then just enter your value using input() or hardcode it

# add input calories to running total if date exists, otherwise create a new row
if index is not None:
    csv_path=os.path.join(csv_file_path, csv_file_name)
    row = index
    column = 1 # 1 as the calories are in second column
    old_entry = csv_get_single_cell(csv_path, row, column)
    new_calories = str(int(old_entry) + input_calorie_delta)
    csv_modify_cell(csv_path, row, column, new_entry=new_calories)
else:
    new_calories = str(int(-bmr +input_calorie_delta))
    all_lines.append([date_str, new_calories]) 
    # write all_lines to csv file to update
    with open(os.path.join(csv_file_path, csv_file_name), 'w') as file:
        writer = csv.writer(file)
        writer.writerows(all_lines)