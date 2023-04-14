"""
This will store the print_help function so that it is easier to document and read
"""

import sys

def print_help():
    print("This script will simplify creating users across the multiple")
    print("different platforms that Drive uses. For now it includes Google,")
    print("Mosyle, and Reftab. \n\n")
    print("USAGE:\n Run the script with one or more of the following arguments:")
    print("")
    print("new employee")
    print("This will allow for inputs to create user accounts across all platforms\n")
    print("term employee")
    print("This will change the user's password in Google, and update their loan in Reftab")
    print("to show that it needs to be shipped home\n")
    print("test")
    print("This will store all requests to be displayed at the end rather than")
    print("actually submitting the commands to the live platform APIs\n")
    print("\nhelp\nPrints this help message")
    sys.exit()
