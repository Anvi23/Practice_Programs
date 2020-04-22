# Write a Program to print fibonacci series. 
#series: 1,1,2,3,5,8,13,21,34...
# 3rd element=1st and 2nd element


n=int(input('Length of series: '))
lst=[1,1]
a=0
i=0
while len(lst)<=n:
    a=lst[i]+lst[i+1]
    lst.append(a)
    i=i+1
    
print(lst)