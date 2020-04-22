#Sort and store it in different files according to the categories. 

fp=open('./StudentsData.csv','r')

'''
fp1=open('OBC.csv','w')


data=[]
for line in fp:
    data.append(line.strip().split(','))
    


for i in range(len(data)):
    if data[i][1]=='OBC':
        print(','.join(data[i]),file=fp1)
        #fp1.write(','.join(data[i]))
'''

cat={}
gender={}
college={}

for line in fp:
    data=line.strip().split(',')
#Summary of records.
    if data[1] in cat:
        cat[data[1]]=cat[data[1]]+1
    else:
        cat[data[1]]=1


    if data[2] in gender:
        gender[data[2]]=gender[data[2]]+1
    else:
        gender[data[2]]=1


    if data[3] in college:
        college[data[3]]=college[data[3]]+1
    else:
        college[data[3]]=1
        
#create new files for every category.
    

for i,v in cat.items():
    print(i,v)
print('__'*20)

for i,v in gender.items():
    print(i,v)
print('__'*20)

for i,v in college.items():
    print(i,v)
print('__'*20)