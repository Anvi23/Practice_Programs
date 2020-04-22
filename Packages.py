lst=[10,11,12,13,14,15,10,11,10]

 
#Search list
def search_list(ntc,lst):
    flag=0
    for i in range(len(lst)):
        if ntc==lst[i]:
            flag=1
    if flag==1:
        return True
    else:
        return False

print(search_list(10,lst))

#prime number
def prime_no(ntc):
    if ntc>1:
        flag=0
        for i in range(2,ntc//2+1):
            if ntc%i==0:
                flag=1
                break
        if flag==1:
            return f'{ntc} is not a Prime Number'
        else:
            return f'{ntc} is a Prime Number'

print(prime_no(23))
print(prime_no(4))

#Prime Number in Range

#NO. is even/odd
def even(ntc):
    if ntc%2==0:
         return f'{ntc} is even'
    else:
        return f'{ntc} is odd'

print(even(5))

#Factorial of a number.

def fact(ntc):
    if ntc==0:
        return 1
    if ntc==1:
        return 1 
    if ntc>1:
        return ntc*fact(ntc-1)

print(fact(5))

#Sum of n number:
def sumN(ntc):
    sum=0
    for i in range(ntc+1):
        sum=sum+i
    return f'Sum of {ntc} numbers is {sum}'

print(sumN(10)) 

# Fibonacci series
def fibo(ntc):
    lst=[0,1]
    if ntc>2:
        for i in range(ntc+1):
            x=lst[i]+lst[i+1]
            lst.append(x)
        return f'{lst}' 
    else:
        return f'{lst}'

print(fibo(10))
print(fibo(1))

#F to C:
# C=(F-32)*(5/9)
#F=C*(9/5)+32

def FtoC(temp):
    C=(temp-32)*(5/9)
    return f'{temp} Fahrenheit is {C} degree Celsius.'

print(FtoC(32))

def CtoF(temp):
    F=temp*(9/5)+32
    return f'{temp} degree Celsius is {F} Fahrenheit.'

print(CtoF(32))

#Standard Deviation

lst1=[10,11,15,20,13,15,16,17,18,20]

def SD(lst):
    sum1=0
    denom=[]
    sum2=0
    for i in range(len(lst)):
        sum1=sum1+lst[i]
    mean=sum1/len(lst)
    for i in range(len(lst)):
        val=(lst[i]-mean)**2
        denom.append(val)
    
    for i in range(len(denom)):
        sum2=sum2+denom[i]
    sd=(sum2/len(lst))**(0.5)
    return f'Standard Deviation of {lst} is {sd:.3f}'

print(SD(lst1))

#Range of Prime Number.

def RangePrime(lowerlimit,upperlimit):
    nlst=[]
    if lowerlimit>1 and lowerlimit<upperlimit:
        for n in range(lowerlimit,upperlimit+1):
            flag=0
            for i in range(2,n//2+1):
                if n%i==0:
                    flag=1
                    
            if flag==0:
                nlst.append(n)
    return nlst    

    
print(RangePrime(2,10))



