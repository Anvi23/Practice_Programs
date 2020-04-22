#Write a program to print all numbers divisible by 7 between 1000 and 2000(inlcusive)

print('Number divisible by 7 between 1000 and 2000: ')

for i in range (1001,2001,7):
    print(i)  

#OR using FOR and nested IF
for i in range (1000,2001):
    if i%7==0:
        print(i)
    
