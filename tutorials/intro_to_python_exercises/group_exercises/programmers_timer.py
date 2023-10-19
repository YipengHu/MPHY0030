import time
import random

# fibonacci generation function which returns the num_terms of fibonacci sequence
# it also prints all numbers in sequence between print_start and print_stop
def fibonacci_generator(num_terms, print_start, print_stop):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1
    fibonacci_list = []
    while count <= num_terms:
        fibonacci_list.append(next_number)
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        
    start_differences = [abs(elem-print_start) for elem in fibonacci_list] # get differences between print_start and each element in fibonacci sequence
    start_index = start_differences.index(min(start_differences)) # get the index of the place where the difference is smalles
    if fibonacci_list[start_index] < print_start: # ensure that the start_index fibonacci element is greater than print_start
        start_index += 1
    
    stop_differences = [abs(elem-print_stop) for elem in fibonacci_list]
    stop_index = stop_differences.index(min(stop_differences))
    if fibonacci_list[stop_index] > print_stop:
        stop_index -= 1    
    
    print(fibonacci_list[start_index:stop_index+1])
    return(fibonacci_list)

fibonacci_list = fibonacci_generator(20, 10, 88)

# timing function with fixed arguments on each iteration
def fixed_argument_timer(func, args, num_iterations):
    toc = time.time()
    for i in range(num_iterations):
        func(*args)
    tic = time.time()
    time_taken = tic - toc
    return time_taken

time_fixed_argument = fixed_argument_timer(fibonacci_generator, args=(20, 10, 90), num_iterations=10)

# create a fake arguments list
args_list = []
for _ in range(10):
    args_list.append([random.randint(20, 30), random.randint(10, 20), random.randint(100, 200)])

# timing function with variable arguments on each iteration
def varying_argument_timer(func, args_list):
    toc = time.time()
    for args in args_list:
        func(*args)
    tic = time.time()
    time_taken = tic - toc
    return time_taken

time_varying_argument = varying_argument_timer(fibonacci_generator, args_list)


