#Write a program to print all the factors of a given number.

n=int(input('Enter a number: '))

print('Factors of n are: ')
for i in range(1,n+1):
   if n%i==0: 
    print(i)

