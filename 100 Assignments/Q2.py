#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
'''
ntc=int(input('Enter the NUmber: '))

if ntc==0:
    print('Factorial of 0 is 1')
if ntc==1:
    print('Factorial of 1 is 1')
prod=1
if  ntc>1:
    
    for i in range(1,ntc+1):
        prod=prod*i

else:
    print('Invalid number')

print(prod)
'''

#Recursion 

def fact(ntc):
    if ntc==0:
        return 1
    if ntc==1:
        return 1
    if ntc>1:
        return ntc*fact(ntc-1)

#Result of multiple inputs in a single line string. 

ntc=int(input('Enter the number: '))
lst=[]
while ntc!=-1:
    
    x=fact(ntc)
    
    lst.append(str(x))
    ntc=int(input('Enter next number: '))

print(','.join(lst))

