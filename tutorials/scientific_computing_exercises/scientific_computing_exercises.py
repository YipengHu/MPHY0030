import numpy as np
from time import time
from scipy.optimize import curve_fit
import os
import matplotlib.pyplot as plt

###############################################################################
# Q) Create a 3x2 array of random float numbers between 0 and 1; then change
#    datatypes to integers

my_array = np.random.rand(3, 2)
my_array_as_int = my_array.astype(np.int16)


###############################################################################
# Q) Create an array which has integers 0-9 in order

my_array = np.arange(0, 10)


###############################################################################
# Q) Create an array which has integers 0-9 in order

my_range = np.arange(10)
my_array = np.reshape(my_range, (2, 5))

###############################################################################
# Write code to create a python list with numbers 0-10,000​
# Write code to create a numpy array with numbers 0-10,000​

# We need to square each element in the list and array​

# ​For the list, write a for loop to square each element​
# For the numpy array find a function that can square all elements of the array​

# Store your result in an empty list and array respectively​

# Time both operations and check which is faster

tic = time()

a = list(range(10000))
b = [0] * 10000

for i in range(len(a)):
    b[i] = a[i]**2

toc = time()
python_list_time = toc-tic
print('list took: ', python_list_time)



tic = time()

a = np.arange(10000)
b = np.zeros(10000)
b = a**2

toc = time()
numpy_array_time = toc-tic
print('array took: ', numpy_array_time)


###############################################################################
# Q) How do a and b look like before and after b has changed?​
#    How can we solve this?​

a = np.eye(4)
b = a[:, 0]

print('a before: \n', a)

b[0] = 5

print('a after: \n', a)

# The solution using np.copy:

a = np.eye(4)
b = np.copy(a)[:, 0]

print('a before: \n', a)

b[0] = 5

print('a after: \n', a)


###############################################################################
# Q) Reverse a vector. Given a vector, reverse it such that the last element 
#    becomes the first, e.g. [1, 2, 3] => [3, 2, 1]​

my_vec = np.array([1, 2, 3])
reversed_vec = my_vec[::-1]


###############################################################################
# Q) Create a 2D array with zeros on the borders and 1 inside​

my_array = np.ones((10, 10))
my_array[:, [0, -1]] = 0
my_array[[0, -1], :] = 0


###############################################################################
# Q) Create a random array with elements [0, 1), then add 10 to all elements in
#    the range [0.2, 0.7)​

# logical indexing (using condition to index) creates an array with Trues 
# and Falses which can be seen as 0 and 1 in mathematical operations
# so going from right to left: times each place where we get True by 10
# then add it to my_array
my_array = np.random.rand(100)
my_arrray_modified = my_array + 10*(my_array >= 0.2)*(my_array < 0.7)


###############################################################################
# Q) What is np.round(0.5)? What is np.round(1.5)? Why?​
print(np.round(0.5))
print(np.round(1.5))
# different because if a value is exactly between two integers then the nearest
# even number is picked as the answer (check docs to learn more)


###############################################################################
# Q) Create a 1D array with 10 random elements and sort it​
# 
#    For the random array in question 8, instead of sorting it, perform an 
#    indirect sort. That is, return the list of indices which would index the 
#    array in sorted order.​

# direct sort
my_array = np.random.rand(10)
my_array_sorted = np.sort(my_array)

# indirect sort
sort_indices = np.argsort(my_array)
my_array_sorted = my_array[sort_indices]


###############################################################################
# Q) Create a 4x4 array of zeros, and another 4x4 array of ones. Next combine 
# them into a single 8x4 array with the content of the zeros array on top and 
# the ones on the bottom. Finally, do the same, but create a 4x8 array with 
# the zeros on the left and the ones on the right.​

my_zeros = np.zeros((4, 4))
my_ones = np.ones((4, 4))

my_array_1 = np.concatenate([my_zeros, my_ones], axis=0)

my_array_2 = np.concatenate([my_zeros, my_ones], axis=-1)



###############################################################################
# Two clinicians measure the inter-pupillary distance (PD) for 100 patients
# in cm​
# Use numpy to report some statistics for this data in order to describe it ​
# E.g. mean, standard deviation, what is the most common bin, mean disagreement
# between clinicians​
# Find the anomalous cases where the clinicians disagree by more than 1 cm so 
#they can be re-evaluated

clin_a = np.loadtxt('/home/s-sd/Desktop/scientific_computing_lectures/clinician_1.txt')
clin_b = np.loadtxt('/home/s-sd/Desktop/scientific_computing_lectures/clinician_2.txt')

clin_a_mean = np.mean(a)
clin_b_mean = np.mean(b)

clin_a_std = np.std(a)
clin_b_std = np.std(b)

anomalous_cases = np.where(np.abs(clin_a-clin_b)>1.0)[0]



###############################################################################
# Q) Create two random 1x20 array of single digit integers then shuffle the first 
# randomly and then shuffle the second using the same sequence of indices​

array_len = 20

array_1 = np.random.randint(0, 9, (array_len))
array_2 = np.random.randint(0, 9, (array_len))

rand_perm = np.random.permutation(array_len)

shuffled_array_1 = array_1[rand_perm]
shuffled_array_2 = array_2[rand_perm]



###############################################################################
# Q) Generate a 1x10 array of random numbers, [0, 1), and ensure that when you 
# rerun your script, the same random numbers are generated again​
# From your array pick 5 values randomly​

np.random.seed(42)
my_array = np.random.rand(10)

picked_values = np.random.choice(my_array, 5, replace=False)



###############################################################################
# Q) From a binomial distribution with parameters n=1, p=0.3, sample 10,000 
#    values and check the mean value, is it 0.3?

binomial_values = np.random.binomial(1, 0.3, 10_000)
mean_value = np.mean(binomial_values)


###############################################################################
# Fit a polynomial using numpy and scipy to the following data:
# x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
# Which library produces a better fit?
# Which degree polynomial is the best fit?

# Can you write a function to automatically vary degrees of polynomial and
# choose and report the best fitting one?

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])

np_coefs = np.polyfit(x, y, 3)

def poly_3(x, a, b, c, d):
    return a*(x**3) + b*(x**2) + c*(x**1) + d

scipy_coefs, _ = curve_fit(poly_3, x, y)

def compute_error(y, y_pred):
    return np.mean((y-y_pred)**2)

y_pred_np = poly_3(x, *np_coefs) # could also use np.polyval

y_pred_scipy = poly_3(x, *scipy_coefs)

error_np = compute_error(y, y_pred_np)

error_scipy = compute_error(y, y_pred_scipy)

# Now we need to write a function to select the best polynomial degree
# Both numpy and scipy are valid, I will put both here

def poly_func(x, coefs):
    final_value = 0
    for coef, degree in zip(coefs, np.arange(len(coefs))[::-1]):
        final_value += coef*(x**degree)
    return final_value

####################### NUMPY #########################
def select_best_degree_np(x, y, low_degree, high_degree):
    degrees = np.arange(low_degree, high_degree)
    errors = []
    for degree in degrees:
        coefs = np.polyfit(x, y, degree)
        y_pred = poly_func(x, coefs)
        error = compute_error(y, y_pred)
        errors.append(error)
    selected_poly_degree_index = np.argmin(errors)
    print(selected_poly_degree_index+low_degree, 
          ' degree produces the lowest error')
    
select_best_degree_np(x, y, low_degree=1, high_degree=5)

####################### SCIPY #########################
def wrapper_poly_func(x, *coefs):
    return poly_func(x, list([*coefs]))

def select_best_degree_scipy(x, y, low_degree, high_degree):
    degrees = np.arange(low_degree, high_degree)
    errors = []
    for degree in degrees:
        coefs, _ = curve_fit(wrapper_poly_func, x, y, p0=np.ones(degree+1))
        y_pred = poly_func(x, coefs)
        error = compute_error(y, y_pred)
        errors.append(error)
    selected_poly_degree_index = np.argmin(errors)
    print(selected_poly_degree_index+low_degree, 
          ' degree produces the lowest error')

select_best_degree_scipy(x, y, low_degree=1, high_degree=5)




###############################################################################
# Two clinicians measure the inter-pupillary distance (PD) for 100 patients in 
# cm; last time we reported some statistics and found anomalous cases​
# Create a histogram for your data with 8 bins and plot it​
# Hint: Use matplotlib or numpy for your histogram data​

# Clinician 1 wants to better understand the data and has asked you to fit a 
# gaussian to the data to see if it follows an approximately normal 
# distribution​

# Fit the data from clinician 1 with 8 bins to a gaussian using the equation:​
# offset + height * np.exp(-1 * ( (x-mean)**2 / (2*(std**2)) ))​
# Hint: ignore the last bin value if you get an error because last value is 
# the end for the last bin​

# Plot the fitted curve and data together​

clin_a = np.loadtxt('/home/s-sd/Desktop/scientific_computing_lectures/clinician_1.txt')
clin_b = np.loadtxt('/home/s-sd/Desktop/scientific_computing_lectures/clinician_2.txt')

clin_a_mean = np.mean(clin_a)
clin_b_mean = np.mean(clin_b)

clin_a_std = np.std(clin_a)
clin_b_std = np.std(clin_b)

n_bins = 8

plt.figure()
n_clin_a, bins_clin_a, patches_clin_a = plt.hist(clin_a, n_bins)
plt.xlabel('PD / cm')
plt.ylabel('Number of cases')
plt.title('Clinician 1')

plt.figure()
n_clin_b, bins_clin_b, patches_clin_b = plt.hist(clin_b, n_bins)
plt.xlabel('PD / cm')
plt.ylabel('Number of cases')
plt.title('Clinician 2')

def my_gaussian(x, height, mean, std, offset):
    return offset + height * np.exp(-1 * ( (x-mean)**2 / (2*(std**2)) ))

popt_clin_a, _ = curve_fit(my_gaussian, n_clin_a[:], bins_clin_a[:-1])

plt.figure()

n_clin_a, bins_clin_a, patches_clin_a  = plt.hist(clin_a, n_bins)

x_data = np.linspace(2, 16, 128)
height, mean, std, offset = popt_clin_a
# shift the mean to account for bar centres rather than bar start points
new_mean = mean + (np.absolute(bins_clin_a[1] - bins_clin_a[2]))/2

plt.plot(x_data, my_gaussian(x_data, height, new_mean, std, offset))
plt.xlabel('PD / cm')
plt.ylabel('Number of cases')
plt.title('Clinician 2')
plt.legend(['fitted curve', 'data'])



###############################################################################
# Clinician 1 told us that they acquired a retina image for each patient​
# Now they want a tool which plots the image and a histogram of the data 
# together with the fitted curve ​
# In the histogram, the bin in which that sample belongs needs to be in a 
# different colour​
# Hint: check the output of plt.hist and how to change the patches i.e. 
# using patches[index].set_facecolor​

images_path = r'/home/s-sd/Desktop/scientific_computing_lectures/images'
   
def plotting_tools(index, images_path=images_path, popt=popt_clin_a):

    plt.figure(figsize=(30, 10))
    ax = plt.subplot(121)
    
    image = plt.imread(os.path.join(images_path, f'{index}.jpeg'))
    
    ax.imshow(image)
    ax.axis('off')
    
    ax1 = plt.subplot(122)
    x_data = np.linspace(2, 16, 128)
    n_clin_a, bins_clin_a, patches_clin_a  = plt.hist(clin_a, n_bins)
    ax1.plot(x_data, my_gaussian(x_data, *popt_clin_a))
    
    ax1.set_xlabel('PD / cm', size=32)
    ax1.set_ylabel('Number of cases', size=32)
    ax1.set_title('Clinician 1', size=32)
    ax1.legend(['fitted curve', 'data'], prop={'size': 24})
   
    bins = np.array(bins_clin_a)
    patch_ind = np.argmin(np.absolute(clin_a[index]-bins))
    patches_clin_a[patch_ind].set_facecolor('r')
    
    ax.set_title('Image', size=32)

plotting_tools(25)
