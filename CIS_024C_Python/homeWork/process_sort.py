
import sys
import sorthelper
import ast

if len(sys.argv) != 2:
    print "Syntax: python process_sort.py [number1,number2,...]"
    
numbers = ast.literal_eval(sys.argv[1])

print "Input List:",numbers
print "Sorted List:",sorthelper.sortNumbers(numbers)