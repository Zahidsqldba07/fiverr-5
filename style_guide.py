"""
Formating guidlines from PEP 8
https://www.python.org/dev/peps/pep-0008/

+ spaces are preferred indentation method (4 spaces)

+ maximum line length should be 79 characters
    + flowing long blocks (i.e. comments) should be limited to 72 characters

+ surround top-level function and class defs with two blank lines

+ method definitions withing a class are surrounded by a single blank line

+ extra lines may be used sparingly to seperate groups of related functions
+ blank lines may be omitted between a bunch of related one-liners

+ use blank lines in functions to indicate loglical sections

+ for Python 3.0 and beyond, only use ASCII encoding

+ use double-quotes for triple-quoted strings; otherwise, pick a conention
  and stick to it

+ modules should have short lowercase names
+ class names should follow the CapWords convention
+ function names should be lowercase
"""


""" dunder names """
# modue level dunders should be placed after the docstring and before imports
__all__=['a','b','c']
__version__='0.1'
__author__='Mark Topacio'

"""" imports """
# imports should be on seperate lines
# multiple imports from module can be comma seperated
# imports are always at the top of the file, just after any module commments 
# and docstrings, and before any globals and constants
#
# should be grouped in the following order:
# 1. standard library imports
# 2. related third party imports
# 3. local application/library specific imports
#
# absoute imports are preferred to relative
# wildcard imports (*) should be avoided
import os
import time
from subprocess import Popen, PIPE


''' line continuations  '''
# preferred method of continuation is implied (i.e. content within parentheses,
# brackets, or braces). These should be used in preference to backslashes.
# sometimes, backslashes are needed if implicits are unavailable
with open(some_file1) as input_1, \
     open(some_file2) as input_2:
    input_2.write(input_1.read())

''' indentation '''

# Aligned with opening delimeter
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces to distinguish between arguments
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

''' if statements '''
# no extra indentation
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# add a comment, which will provide distinction in some editors that support
# syntax highlighting
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we an frobnicate
    do_something()

# add some indentation on continuing conditional line
if (this_is_one_thing and
        that_is_another_thing):
    do_something()

# easy to match operands with operators
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_load_interest)

""" white-space """
# avoid extraneous white-spaces
spam(ham[1], {eggs: 2})             # inside brackets, braces, parenthese
foo = (0,)                          # trailing commas
if x == 4: print x, y; x, y = y, x  # immediately before comma, etc.
ham[1:9]                            # when : used as operator, equal spacing
ham[1 : 9]
