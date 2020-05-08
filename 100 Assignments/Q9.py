#Question 9
#Level 2

#Write a program that accepts sequence of lines as input and prints the lines 
#after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT
'''
#single line
line=input('Enter a single line: ').split()
lst=[]

for val in line:
    lst.append(val.upper())
print(' '.join(lst))
'''
#multiple lines
mlines=[]
while True:

    line=input()
    if line:
        mlines.append(line.upper())
    else:
        break

for i in range(len(mlines)):
    print(mlines[i])

