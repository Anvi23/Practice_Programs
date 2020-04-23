male=open('Male.csv','w')
female=open('Female.csv','w')

with open('./masterfile.txt','r') as master:
    fnamelst=master.read().strip().split()

    print(fnamelst)

    for val in fnamelst:
        with open(val,'r') as dest:
            for line in dest:
                data=line.strip().split(',')
                #print(data)
                if data[1]=='Male':
                    male.write(line)
                    #print(line,file=male)
                else:
                    female.write(line)
                    #print(line,file=female) - giving new line character

