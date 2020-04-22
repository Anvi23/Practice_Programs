lst1=[2,3,4]
lst2=[1,3,5]
prod=1
sum=0
for i in range(0,len(lst1)):
    for j in range(0,len(lst2)):
        prod=lst1[i]*lst2[j] #value of product is changing
        sum=sum+prod #value of sum is updating
    
print(sum)



