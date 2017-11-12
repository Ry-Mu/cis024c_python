
import sys

def add_Command(inputlist):
    return int(inputlist[1]) + int(inputlist[2])

print("The sum of your two numbers is %d" % add_Command(sys.argv))