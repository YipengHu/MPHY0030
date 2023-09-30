"""
Print n rows with stars.

The number of stars in row i should be i.

For example, for 5 stars:

python stars.py
*
**
***
****
*****

"""


def print_star():
    print('*')

def print_stars(max_stars):
    for row_index in range(max_stars):
        num_stars = row_index
        for star_index in range(num_stars):
            print_star()
        print()


print_stars(5)
