#Creating palindrome seqeunce.

# x=input('Enter a sequence: ')
for x in range(10,1000):
    lst=[]
    for i in str(x):
        lst.append(i)

    lst1=lst[::-1]
    
    y=''.join(lst1)
    #print(f'Reverse number: {y}')

    if x==int(y):
        print(f'{x} is a Palindrome.')
    else:
        pass
        #print(f'X is not Palindrome.')
    #print('*'*20)

#create a function to yield palindrome sequence. 


 

