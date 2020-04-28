fp=open('MARKS.csv','r')
#percent=open('Percentages.csv','w')
fout=[]

fout.append(open('Failed_sub1.csv','w')) #Should open all connections once not in loop.
fout.append(open('Failed_sub2.csv','w')) #making a list of pointer is better than creating individual connections
# closing is easier.
fout.append(open('Failed_sub3.csv','w'))
fout.append(open('Failed_sub4.csv','w'))
fout.append(open('Failed_sub5.csv','w'))

top=open('topper.csv','w')
fail=open('More_than_2_Fail.csv','w')
pas=open('Pass.csv','w')
max=[0,0,0,0,0]
maxd=[[],[],[],[],[]] #1.Can add more than one topper for a subject and replace it in case next students scores more.
#maxd=["","","","",""]- can't add more than one value in this list. Specifying position so that updating is easier. 
x=fp.readline()

#calculate percentage
#sdata=[]
for line in fp:
    data=line.strip().split(',')
    perc=sum(list(map(int,data[5:])))/500*100
    data.append(str(perc))
    #sdata.append(data)
    #print(f'Percentage of {data[0]} is {data[-1]}',file=percent)
    
    count=0
    
#topper of individual subject. BUT what if there are more than one students scoring max marks in a subject. 

    if int(data[5])>max[0]:
        max[0]=int(data[5])
        maxd[0]=[] #deletes previous elements in the lost.
        maxd[0].append(line)
    elif int(data[5])==max[0]:
        maxd[0].append(line)

    if int(data[6])>max[1]:
        max[1]=int(data[6])
        maxd[1]=[]
        maxd[1].append(line)
    elif int(data[6])==max[1]:
        maxd[1].append(line)

    if int(data[7])>max[2]:
        max[2]=int(data[7])
        maxd[2]=[]
        maxd[2].append(line)
    elif int(data[7])==max[2]:
        maxd[2].append(line)
    
    if int(data[8])>max[3]:
        max[3]=int(data[8])
        maxd[3]=[]
        maxd[3].append(line)
    elif int(data[8])==max[3]:
        maxd[3].append(line)

    if int(data[9])>max[4]:
        max[4]=int(data[9])
        maxd[4]=[]
        maxd[4].append(line)
    elif int(data[9])==max[4]:
        maxd[4].append(line)

#fail marks<40
    if int(data[5])<40:
        fout[0].write(line)
        count+=1
    if int(data[6])<40:
        fout[1].write(line)#sub2.write(','.join(data)+'\n')
        count+=1
    if int(data[7])<40:
        fout[2].write(line)
        count+=1
    if int(data[8])<40:
        fout[3].write(line)
        count+=1
    if int(data[9])<40:
        fout[4].write(line)
        count+=1
    
    if count>1:
        fail.write(','.join(data)+'\n')
    
    if count==0:
        pas.write(','.join(data)+'\n')
   
for v in maxd:
    for v1 in v: 
        top.write(v1)
    print('__'*20,file=top)

    

fp.close()
fail.close()
pas.close()
top.close()

for v in fout:
    v.close()
    