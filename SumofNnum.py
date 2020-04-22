#Write a program to print sum of all the numbers up to n. Value of n is entered by user.

n=int(input('Value of n: '))
#s=(n*(n+1)/2
#sum of n terms= (n*(n+1))/2
'''
sum=sum+1
i=i+1
'''

sum=0
for i in range (1,n+1):
    sum=sum+i
print(sum)



