#Question 16
#Level 2

#Use a list comprehension to square each odd number in a list.
#The list is input by a sequence of comma-separated numbers.


numbers=list(map(int,input('Enter a list of numbers: ').split(',')))
oddsqr=[i*2 for i in numbers if i%2!=0] #list comprehension

print(oddsqr)
'''
odd=[]
for val in numbers:
    if int(val)%2!=0:
        sqr=int(val)**2
        odd.append(str(sqr))
        #print(val**2,end=', ')
        
print(','.join(odd))
'''


 