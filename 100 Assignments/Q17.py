#Question 17
#Level 2

#Write a program that computes the net amount of a bank account based a transaction log 
#from console input. The transaction log format is shown as following:
#D 100
#W 200
'''D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''


dc={'D':0,'W':0}

while True:
    trans=input('Enter the transaction details: ').split()
    if trans:
        if trans[0]=='D':
            dc['D']+=int(trans[1])
        if trans[0]=='W':
            dc['W']+=int(trans[1])
    else:
        break

netamount=dc['D']-dc['W']
print(netamount)