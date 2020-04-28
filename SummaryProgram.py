filep = open('StudentsData.csv','r')

gender = {}
college = {}
cat = {}

for line in filep:
    data = line.strip().split(',',3) #creating individual list and not saving the list just checking for values.
    '''
    [0] -> Name
    [1] -> Category
    [2] -> Gender 
    [3] -> College
    '''
    if data[3] in college: #if element 3 of list is in dictionary,add 1(increasing counter)
        college[data[3]] = college[data[3]]+1
    else: #if it is not, then adding the key(element 3 of list)
        #and assigning value=1..which will be increased by 1 next time if data[3] comes. 
        college[data[3]] = 1
    
    if data[2] in gender:
        gender[data[2]] = gender[data[2]] + 1
    else:
        gender[data[2]] = 1
    
    if data[1] in cat:
        cat[data[1]][0] = cat[data[1]][0] +  1
        #print(','.join(data),file=cat[data[1]][1])
        cat[data[1]][1].write(','.join(data)+'\n')
    else:
        fp = open(data[1] + '.csv', 'w') #data[1]= OBC...need not make different files-AUTOMATED. 
        #and concatenate 'CSV'
        cat[data[1]] = [1,fp] #assigning a list as a value in dictionary. 
        #fp is passed as an element. WHY? 
        #cat[data[1]][1] = fp...but not using it as fp As--> under IF, we are not initialising fp. 
        #print(','.join(data),file=cat[data[1]][1]) OR
        cat[data[1]][1].write(','.join(data)+'\n')
        
for i,v in gender.items():
    print(i,v)

print('-'*20)

for i,v in cat.items():
    print(i,v[0])
    
print('-'*20)

for i,v in college.items():
    print(i,v)
