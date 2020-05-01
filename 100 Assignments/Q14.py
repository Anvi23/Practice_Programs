#Question 14
#Level 2

#Write a program that accepts a sentence and calculate the number of upper case 
# letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

sentence=input('Enter a sentence: ')

dc={'Upper Case':0,'Lower Case':0}

for i in sentence:
    if i.isupper():
        dc['Upper Case']+=1
    if i.islower():
        dc['Lower Case']+=1

for i,v in dc.items():
    print(i,v)