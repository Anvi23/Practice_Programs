#Question 13
#Level 2

#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3


sentence=input('Enter a sentence: ')
digits=0
letters=0
for val in sentence:
    if val.isdigit():
        digits+=1
    if val.isalpha():
        letters+=1

print(f'Letters = {letters} and Digits = {digits}')

#using dictionary..
