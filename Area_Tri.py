#Write a program to calculate area of a traingle. 
#User needs to enter all three sides as input.
#Check if the sides entered by user are valid or not.

print ('Enter the three sides of the triangle below: ')
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))

if (a+b)>c and (b+c)>a and (c+a)>b:
    s=(a+b+c)/2
    Area=(s*(s-a)*(s-b)*(s-c))**(1/2)
    print('Area of triangle with sides {},{},{} is {}'.format(a,b,c,Area))

else: 
    print('Sides entered are invalid')