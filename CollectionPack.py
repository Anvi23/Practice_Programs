#Collection Package Assignment
import collections as co


#1.Creating Ordered dict from named tuple. Try _asdict method. 

namedtup=co.namedtuple('Student',['Name','Surname','ID'])
tup1=namedtup('Anvi','Jain','101')
print(namedtup)

orderdict=co.OrderedDict()
for i in range(len(tup1)): 
    orderdict[((tup1._fields)[i])]=tup1[i]

print(orderdict)

#creating Ordered dict from two different named tuples.

namedtup1=co.namedtuple('Student',['Subject','Marks','Status'])
tup2=namedtup1('Python',45,'Completed')

lst1=[tup1,tup2]
orderdict1=co.OrderedDict()

for i in lst1: #i=tup1
    for j in range(len(i)):#3 
        orderdict1[((i._fields)[j])]=(i[j]) 

print(orderdict1)

#2. Creating default dict from dict.

co.defaultdict()

demodict={'name':'Anvi', 'subject':'Python', 'marks': 45}

demodict1=co.defaultdict(lambda :'No field found',demodict)
print(demodict1)

print(demodict1['surname'])

#OR
trydict={'name':'Saransh', 'subject':'Java', 'marks': 87}
trydefaultdict=co.defaultdict(lambda: 'No field Present')

for i in trydict.keys():
    trydefaultdict[i]=trydict[i]
    

print(trydefaultdict)
print(trydefaultdict['surname'])


#Changing list of list(seqeunce of key-value pairs) into default dictionary.

lst=['anvi','saransh','divu']

demodict2=co.defaultdict(lambda :'No field present')
for i in range(len(lst)):
    demodict2[i]=lst[i]
print(demodict2,'1')

print(demodict2[1])
print(demodict2[7])


