#Reading a CSV file. 

#uni=open('/Users/anvi/Downloads/Uni.csv','r')

uni=open('Uni.csv','r')

#Save file in the form of a list.
x=uni.readline()
data=[]
for line in uni:
    data.append(line.split(',')[0:5])
    
   
print(data)


#calculate max of fees. 
    
maxf=data[1][4]
maxp=0
for i in range(2,len(data)):
    if maxf<data[i][4]:
        maxf=data[i][4]
        maxp=i
    
print(f'Maximum fees is {maxf} of {data[i][0]}')
    