#1.Best supplier for (prod1,prod2), (prod2,prod3),(prod3,prod1)


productdata={
    'prod1':['supp1','supp2','supp3'],
    'prod2': ['supp3','supp4','supp5'],
    'prod3': ['supp1','supp3','supp5']}
#1&2- supp3
#2&3-supp3,supp5
#1&3-supp1, supp3


lst=[]
for i,v in productdata.items(): 
    productdata[i]=set(productdata[i]) 
    lst.append(productdata[i])
print(lst)

for i in range(len(lst)): #0 #1 #2
    for j in range(i): #0..#0,1 #0,1,2
        set1=lst[j]&lst[i] #does not executed.. #prod2&prod1..#prod3&prod1 + prod3&prod2
        print(f'Best supplier for product {j+1}&{i+1} is {set1}')
    
#2.Supplying one prod but not other. 
#1 but not 2&3
#2 but not 1&3 
#3 but not 1&2 
set1=lst[0]-(lst[1]|lst[2])
set2=lst[1]-(lst[0]|lst[2])
set3=lst[2]-(lst[1]|lst[0])
print(set1,set2,set3)