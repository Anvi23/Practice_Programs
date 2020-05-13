#9-3. Users: Make a class called User. Create two attributes called first_name 
# and last_name, and then create several other attributes that are typically stored
#in a user profile. Make a method called describe_user() that prints a summary
#of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.

class User:
    def __init__(self,first_name='',last_name='',cat=''):
        self.first_name=first_name
        self.last_name=last_name
        self.cat=cat
        self.login_attempts=0
        '''
        while self.cat:
            if self.cat=='Premium' or self.cat=='VIP':
                self.cat=cat
            else:
                print('Choose Premium or VIP category.')
                self.cat=input('Enter your valid category: ')''' #??not checking the input again.

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is a {self.cat} customer.')

    def greet_user(self):
        print(f'Hello ! Mr/Mrs.{self.first_name}. Greetings of the day !')
    
    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

#anvi=User('Anvi','Jain','Premium')
#anvi.describe_user()

ami=User('Ami','Jain','VIP')
ami.describe_user()
    
#9-5. Login Attempts: Add an attribute called login_attempts to your Userclass.
#  Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
#Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, 
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

print(ami.__dict__)
ami.increment_login_attempts()
print(ami.login_attempts)

ami.increment_login_attempts()
print(ami.login_attempts)

ami.increment_login_attempts()
print(ami.login_attempts)

ami.reset_login_attempts()
print(ami.login_attempts)

#9-7. Admin: An administrator is a special kind of user. Write a class called Admin that 
#inherits from the User class. Add an attribute, privileges, that stores a list
#of strings like "can add post", "can delete post", "can ban user", and so on.
#Write a method called show_privileges() that lists the administrator’s set of privileges. 
#Create an instance of Admin, and call your method. 


#9-8. Privileges: Write a separate Privileges class. The class should have one attribute privileges.
#Move the show_privileges() method to this class. Make a Privileges instance 
#as an attribute in the Admin class. Create a new instance of Admin and use your
#method to show its privileges .

class Privileges():
    def __init__(self,privileges=''):
        self.privileges=['can add post','can delete post','can ban user']
     
    def show_privileges(self):
        print("Following are adminstrator's set of privileges:-")
        for i in self.privileges:
            print('-',i)

class Admin(User):
    def __init__(self,first_name,privileges=''):
        super().__init__(first_name)
        self.privileges=Privileges() #Instance as an attribute.
        
anvi=Admin('Anvi','jain')
anvi.privileges.show_privileges()
print(anvi.__dict__) #for priviledges it points towards Priveleges Object

