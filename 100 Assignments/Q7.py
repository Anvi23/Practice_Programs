#Question:
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
#The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,...­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#i=0,1,2
#j=0,1,2,3 
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
#[[0*1,0*2...0*j],[1*0,1*2...i*j],[2*0,2*1,2*2...]]

x=int(input('Enter number X: '))
y=int(input('Enter number Y: '))

matrix=[]
for i in range(x):
    lst=[] #for every row, lst gets empty.
    for j in range(y):
        lst.append(i*j)
    matrix.append(lst)
        
print(matrix)