#Write a program to print all numbers divisible by 5 and 7 in the given range by user.

a=int(input('Enter the starting value: '))
b=int(input('Enter the ending value: '))

for i in range (a,b+1):
    if i%5==0 and i%7==0:
        print(i)



