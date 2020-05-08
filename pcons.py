#parameterized Constructor

class Student:
    #Fees (Already added)
    #Name
    #Class
    #dateofbirth
    #age
    def __init__(self,name1,sec,dob,age,f=0): #Constructor
        #print("Object Created. This is a message from constructor")
        self.fees = f
        self.name1 = name1
        self.sec = sec
        self.dob = dob
        self.age = age

    def payFees(self,amount):
        self.fees = self.fees + amount
    
    def getFees(self):
        return self.fees

    def describe(self):
        print(f'Name of student: {self.name1}')
        print(f'Subject: {self.sec}')
        print(f'DOB: {self.dob}')
        print(f'Age: {self.age}')

    def __del__(self): #Destructor 
        #print('Destructor')
        pass

s1=Student('Anvi','Python','23.05.1996',23)
s1.describe()

#st = Student()
#st1 = Student(1000)
#st2 = Student(2000)

#print(st1.getFees())
#print(st2.getFees())

#print(st.fees)
#st.fees = 5000
#print(st.getFees())
#print(st1.getFees())
#sprint(st2.getFees())