#Write a program that yields prime number in given range.


def prime(ll,ul):
    if ul>ll and ll>1:
        for ntc in range(ll,ul+1):
            flag=0
            for i in (2,int(ntc/2)+1):
                if ntc%i==0 :
                    flag=1

            if flag==0:
                yield ntc
    else:
        yield ('Invalid Range')

ll=int(input('Enter lower limit: '))
ul=int(input('Enter upper limit: '))

for i in prime(ll,ul):
    print(i,end=' ')