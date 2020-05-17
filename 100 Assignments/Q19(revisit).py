#Question 19
#Level 3

#You are required to write a program to sort the (name, age, height) tuples by ascending order
#  where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
'''1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), 
('Json', '21', '85'), ('Tom', '19', '80')]'''

lst=[]
while True:
    desc=input('Enter name, age and height: ') #when we split(',') - it considers (space,) an element and loop will not break.
    if desc:
        desc1=desc.split(',')
        one=sorted(desc1,key=lambda desc1:desc1[1])
        print(one)
        #two=sorted(one,key=lambda one:one[2])
        lst.append(one)
        lst.sort()
        print(lst)
        '''name=lst[0][0]
        for i in range(len(lst)):
            if lst[i][0]==lst[0][0]:
                lst[i].sort()'''
    else:
        break


 