###############################################################################
# What happens when you add two strings?
print('Hello' + 'World')

# What happens when you multiply a string by an integer?
print('Hi' * 4)

# What happens when you multiply a list by an integer?
print([1, 2, 'three'] * 3)

# What happens if you add two lists?
print([1, 2, 'three'] + [4.0, 'five'])

# What happens when you multiply/ add/ subtract/ divide an integer with a float 
# (what is the type)? How about float with float or integer with integer?
print(isinstance(16 / 4.0, float))
print(isinstance(16 + 4, float))
print(isinstance(16 / 4, float))

# What purpose do (brackets) serve? How about multiple operations in the same 
# line for computing a mean of 5 numbers
# brackets are for operation priority
mean = (1+2+3+4+5) / 5
print(mean)

# What does the % operator do? How about the ** operator?
# % modulo operator gets the remainder from a division so 4 / 2 is  0 (4 % 0)
# ** is the exponentiation operator
print(4 % 2)
print(2 ** 4)

# Does anything happen if you try a combination not listed here e.g., divide a 
# string by a string or subtract a list from a string?
# print('hi, how are you' / 'hi')
# the above returns a TypeError, which is whn an operation between the two
# variable types is not supported in python


###############################################################################
# Create a list_final with 4 elements, with the last element being a list with 
# two elements
list_final = [1, 2, 3, [4, 5]]

# Write an expression involving list_final to get the second element of 
# list_final
second_elem = list_final[1]

# Write an expression involving list_final to get the first element of the last 
# element of list_final
first_of_last_elem = list_final[-1][0]

# What does len(list_final) reveal? How about len(list_final[-1])?
print(len(list_final), len(list_final[-1]))
# prints the length of the list

# What does : mean while indexing?
# : specifies the range for indexing
print(list_final[0:3])
# gets elements 0, 1, 2

# Create a string 'Hi my name is Name' and extract from it the string 'my name'
# using :
my_str = 'Hi my name is Name'
print(my_str[3:10])

# From the same string, write an expression to extract the 'Name' regardless of 
# the length of the Nam
my_str_1 = 'Hi my name is Shaheer'
my_str_2 = 'Hi my name is Name'
print(my_str_1[14:])
print(my_str_2[14:])

###############################################################################
# Given a list of integers called numbers

# Create a function which:
# returns True if any value appears at least twice in the list
# returns False if every element is distinct

# Evaluate using the following cases:
# numbers = [1, 2, 3, 1]; Returns True
# numbers = [1, 2, 3, 4]; Returns False
# numbers = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]; Returns True

# Hints: append (to add elements to list), in (to check if element is in list),
# return (to return a value), True/ False

# Challenge: Use as few iterations as possible!

def my_function(numbers):
    flag = False
    list_2 = []
    for number in numbers:
        if number in list_2:
            flag = True
            break
        else:
            list_2.append(number)
    return flag

print(my_function([1, 2, 3, 1]))
print(my_function([1, 2, 3, 4]))
print(my_function([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

###############################################################################
# What function can you call to list all the files and folders in a specified 
# path?
import os
os.listdir(r'./')
# list all files in the current directory

# How can you unzip a compressed .zip file?
import zipfile
# open zipfile in read mode 'r' and create a reference for this
with zipfile.ZipFile(r'./zipped_fle.zip', 'r') as zip_ref:
    # extract the contents
    zip_ref.extractall(r'./')
# zipped_file.zip from current directory unzipped into current directory

# How can you add a line to a csv file?
from csv import writer
List = [6, 'William', 5532, 1, 'UAE'] # this is the list to add as a new row 
# Open our existing CSV file in append mode 'a'
# Create a file object for this file
with open('event.csv', 'a') as f_object:
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(List)
    # Close the file object
    f_object.close()

# How can you check the current date and time?
import datetime
current_date_time = datetime.datetime.now()
# dd/mm/YY H:M:S
dt_string = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
print("date and time:", dt_string)

# How can you compute the time taken to append an element to a list 1000 times?
import time
tic = time.time()
my_list = []
for i in range(1000):
    my_list.append(42)
toc = time.time()
time_taken = toc-tic
print(f'It took {time_taken} seconds')

# How can you make a python script such that when you run 'script.py' from the
# terminal, it prints 'Hello World!'
# Contents of script.py:
print('Hello World!')

# On the terminal:
# python3 script.py

# How can you make a python script such that it takes an argument? (check
# sys.argv); make a script that prints 'Hello world! I am a script and I was 
# given the number X' where 'X' is the argument used when running the script
# Contents of script.py:
import sys
X = sys.argv[1]
print(f'Hello world! I am a script and I was given the number {X}')

# On the terminal:
# python3 script.py '42'

###############################################################################
