# 4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that. (Using ChatGPT).
# 5. Label the program written in problem 4 with comments. 

import os

# Select the directory whose content you want to list
directory_path = '/Users'

# Use to os module to list the directory
content = os.listdir(directory_path)

# It's use to print content of directory
for item in content:
    print(item)