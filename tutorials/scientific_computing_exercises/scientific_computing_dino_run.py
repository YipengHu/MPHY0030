# Note that commands begining with a ! must be executed on the terminal or
# in spyder with a ! before the command (if on the terminal, exclude the !)

# Task 1:
# !pip install pyautogui


# Task 2:

# !mkdir dino-run
# !cd dino-run
# !git clone https://github.com/s-sd/Chrome-Dino-Runner.git
# !ls
# !cd Chrome-Dino-Runner
# !pip install -r requirements.txt 
# (error if you follow the online instructions because missing -r)

# !python3 chromedino.py 
# should return an error related to score.txt
# create a file called score.txt and add a zero inside it (manusally or in
# your script)
# the author used their own score.txt
# ls

# if you created a file but left it empty
# python3 chromedino.py (opens but closes when you press a key)
# max arg is an empty sequence error is shown
# check trace  and find that score_ints is empty
# what is score_ints?
# search chromedino.py and find that score_ints is from score.txt
# populate score.txt with some dummy values (add a zero is okay)

# if unable to access it, https://chromedino.com/

# if creating a venv:
# python3 -m venv dino
# chmod +x dino/bin/activate
# . ./dino/bin/activate

import time
import numpy as np
import pyautogui as pg
import matplotlib.pyplot as plt


time.sleep(5)
sc = pg.screenshot()
print('done!')

plt.imshow(sc)
plt.grid(True)

sc = np.array(sc)
sc_crop = sc[300:400, 2600:3200] # adjust these values
plt.imshow(sc_crop)
# the values above crop the screenshot such that only the game window is 
# visible roughly
# to get these values for your display, run the three lines at the top
# then you have 5 seconds to open the game window such that the screenshot
# has the game window visible
# plt.imshow will show the image with a grid and simply check which values to 
# use to crop your screenshot such that only the game window is visible
# Advanced: alternatively look into locateonscreen in pyautogui 
# Advanced: alternatively find a way to launch the game window from your script
#           hint: check sys and how to execute system commands

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
sc_crop_grey = rgb2gray(sc_crop)
plt.imshow(sc_crop_grey, cmap='gray')
# if above rgb2gray doesn't work please use the function from this answer:
# https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python

def get_sc():
    sc = pg.screenshot()
    sc = np.array(sc)
    sc_crop = sc[300:400, 2600:3200] # these values are the same as above
    sc_crop_grey = rgb2gray(sc_crop)
    return sc_crop_grey
sc_sample = get_sc()
# plt.imshow(sc_sample)

def press_up():
    pg.keyDown('up')
    time.sleep(0.05)
    pg.keyUp('up')
# press_up()

num_iter = 1000
threshold = 243

for iter in range(num_iter):
    sc = get_sc()
    print(np.mean(sc[:, 200:300]))
    if np.mean(sc[:, 200:300]) < threshold:
        # plot your cropped grayscale image with a grid and check where the
        # obstacles appear such that the dino can jump in time
        # we found between x axis values 200-300
        # so we check the mean of the pixel values at this patch
        # and we jump if there are too many black in the patch i.e. an obstacle 
        time.sleep(0.1) # add a small delay to delay our jumps
        press_up()


