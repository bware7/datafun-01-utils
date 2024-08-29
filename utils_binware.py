''' ITERATION 1

Module: Python With Bin - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''

import statistics

#####################################
# Declare a global variables
#####################################

# boolean indicating if project is privately held. 
is_privately_held: bool = True

# integer representing the size of the team involved in the project.
team_size: int = 7

# list of strings representing the tools being used in the project. 
tools_used: list = ["Git", "GitHub", "Python"]

# list of floating-point numbers representing recent daily temperatures. 
daily_temperatures: list = [72.5, 75.0, 69.8, 71.6, 74.2]

#####################################
# calculate basic statistics
#####################################

min_temp: float = min(daily_temperatures)
max_temp: float = max(daily_temperatures)
mean_temp: float = statistics.mean(daily_temperatures)
stdev_temp: float = statistics.stdev(daily_temperatures)

#####################################
# declare a global variable named byline.
# make it a multiline f-string to show our info. 
#####################################

byline: str = f""" 
-------------------------------------------------
 Python With Bin: A Coding Company
-------------------------------------------------
Is Privately Held: {is_privately_held}
Number of Team Members: {team_size}
Tools Used: {tools_used}
Recent Daily Temperatures of the Office: {daily_temperatures}
"""

#####################################
# Function to return the byline.
#####################################

# Function named get_byline.
# Returns the value of the byline variable.
def get_byline() -> str:
    '''Return the byline string.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(byline)

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
