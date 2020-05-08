#Check the memory usage of list vs yeild. 
import memory_profiler as mp
'''
with open('./File1.csv','r') as f1, open('./File2.csv','r') as f2,open('./File3.csv','r') as f3, open('./File4.csv','r') as f4, open('./Compiledfile.csv','w') as cp:
    
    for line in f1 :
            cp.write(line)
    for line in f2 :
            cp.write(line)
    for line in f3 :
            cp.write(line)
    for line in f4 :
            cp.write(line)
'''          
def readfile():
    with open('./Compiledfile.csv','r') as cp:
        for line in cp:
            data=line.strip().split(',')
            yield data[0]

print(mp.memory_usage())

#for i in readfiles():
    #print(i,end=' ')

def readfiles2():
    with open('./Compiledfile.csv','r') as cp:
        lst=[]
        for line in cp:
            data=line.strip().split(',')
            lst.append(data[0])
        return lst

print(mp.memory_usage())
print(readfiles2())