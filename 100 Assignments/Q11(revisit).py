#Question 11
#Level 2

#Write a program which accepts a sequence of comma separated 4 digit binary numbers 
# as its input and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010
#Notes: Assume the data is input by console.
#bin- on int.


#1234

lst=[]
ntc=input('Enter a four digit numbers: ').split(',')
print(ntc)
for val in ntc:
    number= int(val[0])*2**0 + int(val[1])*2**1 + int(val[2])*2**2 + int(val[3])*2**3
    #print(number)
    if int(number)%5==0:
        lst.append(val)

print(','.join(lst))

'''

b_num = list(input("Input a binary number: "))
value = 0
print("b_num",b_num)

for i in range(len(b_num)):
    digit = b_num.pop()
    print(digit,'d')
    if digit == '1':
	    value = value + pow(2, i)

print(f'The decimal value of the number is {value}' )

'''
