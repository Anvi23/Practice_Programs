#Write a program to find greater of three numbers.
a=int(input('Enter a: '))
b=int(input('Enter b: '))
c=int(input('Enter c: '))

if a==b and b==c and c==a:
    print('All values are equal',a)

elif a>b and b>c:
    print(a, 'is greatest')

elif a==b:
    if a>c:
        print(a, 'is the greatest')
    else:
        print(c,'is the greatest')
elif b==c:
    if b>a:
        print(b, 'is the greatest')
    else:
        print(a, 'is the greatest')
elif c==a:
    if c>b:
        print(c,a, 'are equal and greatest')
    else:
        print(b, 'is the greatest')
