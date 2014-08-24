from os import system
import sys

number_of_args = len(sys.argv)-1
print number_of_args

sys.argv.pop(0)

for argfile in sys.argv: 
	print argfile
