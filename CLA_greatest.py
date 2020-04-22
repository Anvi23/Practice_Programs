#Write a Program to print greatest of all the values entered as command line arguments.

import sys #every time we need to run CLA.


g=sys.argv[1]

for i in range(1,len(sys.argv)):
    if g<sys.argv[i]:
        g=sys.argv[i]

print(f'Greatest of all the numbers in {sys.argv[1:]} is {g}')

#inbuilt method.

