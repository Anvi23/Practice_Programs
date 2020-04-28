#Master data file handling. Sorting names on the basis of gender. 

with open('Male.csv','w') as male, open('Female.csv','w') as female, open('./masterfile.txt','r') as master:
 
    fnamelst=master.readlines()
    #fnamelst=master.read().strip().split() 
    # #readline() is better, need to use strip then. 

    print(fnamelst)

    for val in fnamelst:
        with open(val,'r') as dest:
            for line in dest:
                #data=line.strip().split(',')
                #line.find string method.
                if line.find('Female')==-1: #line.find returns index if 'Female' exists 
                    #& otherwise returns -1.
                
                #if data[1]=='Male':
                    male.write(line)
                    #print(line,file=male)
                else:
                    female.write(line)
                    #print(line,file=female) - giving new line character

