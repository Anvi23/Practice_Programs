#Write a program to calculate area of a traingle, where all three sides are entered 
# as command line arguments. Before calculating, check if the sides entered are 3 and are valid sides. 
# Rule: In triangle, sum of any two sides is always greater than the third one. 

import sys

a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])

if len(sys.argv)==4:
    if (a+b)>c and (b+c)>a and (c+a)>b:
        s=(a+b+c)/2
        Area=(s*(s-a)*(s-b)*(s-c))**(1/2)
        print(f'Area of tirangle with sides {a},{b} and {c} is {Area}')
else:
    print('Invalid Sides')


