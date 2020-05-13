#Custom errors
'''
1.Invalid Account number
2.Invalid Transaction type
3. Invalid Amount
4. Insufficient Balance

Transaction file :
 0- ID
 1- Type
 2- Source A/c
 3- Destination A/c
 4- Amount
'''
class InvalidAccountN(Exception):
    def __init__(self,accnum,acctype,transactID):
        self.accnum=accnum
        self.transactID=transactID
        self.acctype=acctype
    def __str__(self):
        return f'Invalid {self.acctype} Account: {self.accnum} in transaction ID: {self.transactID}'

class InvalidTransactiontype(Exception):
    def __init__(self,transacttype,transactID):
        self.transacttype=transacttype
        self.transactID=transactID
    def __str__ (self):
        return f'Invalid transaction type {self.transacttype} in transaction ID: {self.transactID}'

class InvalidAmount(Exception):
    def __init__(self,amount,transactID):
        self.amount=amount
        self.transactID=transactID
    def __str__(self):
        return f'Invalid amount {self.amount} in transaction ID: {self.transactID}'

class InsufficientBalance(Exception):
    def __init__(self,accnum,transactID):
        self.accnum=accnum
        self.transactID=transactID
    def __str__(self):
        return f'Insufficient Account Balance for Account {self.accnum} in transaction ID: {self.transactID}'
class Logfile:
    def __init__(self):
        self.inaccnum=open('Invalid_AcNum.txt','a') #file extension
        self.inamount=open('Invalid_Amount.txt','a')
        self.intt=open('Invalid_Type.txt','a')
        self.insuffb=open('Invalid_Balance.txt','a')
    def close(self):
        self.inaccnum.close()
        self.inamount.close()
        self.intt.close()
        self.insuffb.close()

logfile=Logfile()

import mysql.connector
mdb=mysql.connector.connect(host='localhost',user='root',passwd='Anvijain@2305',auth_plugin='mysql_native_password',database='Demodata')
cur=mdb.cursor()
print()
minimumbal=1500
try:
    with open ('Transactionfile.csv','r') as tf:
        for transaction in tf:
            transdata=transaction.strip().split(',')
            try:
                '''
                0- ID
                1- Type
                2- Source A/c
                3- Destination A/c
                4- Amount
                '''
                #if amount is wrong
                if int(transdata[4])>0:
                    #type=transfer
                    if transdata[1]=='Transfer':
                        cur.execute(f'Select count(*) from BankDetails where AccountNumber={transdata[2]}') #checking source account
                        if (cur.fetchone()[0])==1:
                            cur.execute(f'Select count(*) from BankDetails where AccountNumber={transdata[3]}')#checking destination account
                            if (cur.fetchone()[0])==1:
                                cur.execute(f'Select * from BankDetails where AccountNumber={transdata[2]}')
                                if (cur.fetchone()[2]-int(transdata[4]))>=minimumbal:
                                    cur.execute(f'Update BankDetails set Balance=Balance-{transdata[4]} where AccountNumber={transdata[2]}')
                                    cur.execute(f'Update BankDetails set Balance=Balance+{transdata[4]} where AccountNumber={transdata[3]}')
                                    mdb.commit()
                                else:
                                    raise InsufficientBalance(transdata[2],transdata[0])
                            else:
                                raise InvalidAccountN(transdata[3],'Destination',transdata[0])
                        else:
                            raise InvalidAccountN(transdata[2],'Source',transdata[0])
                    #type=Deposit
                    elif transdata[1]=='Deposit':
                        cur.execute(f'Select count(*) from BankDetails where AccountNumber={transdata[3]}') #checking destination account
                        if (cur.fetchone()[0])==1:
                            cur.execute(f'Update BankDetails set Balance=Balance+{transdata[4]} where AccountNumber={transdata[3]}')    
                        else:
                            raise InvalidAccountN(transdata[3],'Destination',transdata[0])
                    #type=Withdraw
                    elif transdata[1]=='Withdraw':
                        cur.execute(f'Select count(*) from BankDetails where AccountNumber={transdata[2]}') #checking source account
                        if (cur.fetchone()[0])==1:
                            cur.execute(f'Select * from BankDetails where AccountNumber={transdata[2]}')
                            if cur.fetchone()[2]-int(transdata[4])>=minimumbal:
                                cur.execute(f'Update BankDetails set Balance=Balance-{transdata[4]} where AccountNumber={transdata[2]}')
                            else:
                                raise InsufficientBalance(transdata[2],transdata[0])
                        else:
                            raise InvalidAccountN(transdata[2],'Source',transdata[0])
                    else:
                        raise InvalidTransactiontype(transdata[1],transdata[0])
                else:
                    raise InvalidAmount(transdata[4],transdata[0])

            except InvalidAmount as ia:
                print(ia,file=logfile.inamount)
            except InvalidTransactiontype as it:
                print(it,file=logfile.intt)
            except InsufficientBalance as isb:
                print(isb,file=logfile.insuffb)
            except InvalidAccountN as ian:
                print(ian,file=logfile.inaccnum)
except:
    print('All Exceptions')
finally:
    mdb.close()
    logfile.close()
    
            



