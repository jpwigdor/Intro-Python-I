"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("Arguments: ")
for arg in sys.argv:
    print(arg)
# Print out the OS platform you're using:
# YOUR CODE HERE
print("My platform is: ", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("my version of python is: ", sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("the current process ID is: ", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("The current working directory is: ", os.getcwd())

import getpass
# Print out your machine's login name
# YOUR CODE HERE
print("the current machine's login name is: ", getpass.getuser())
# Since i'm using WSL, it said there was no login, but using the getpass package - I was able to obtain my login name
