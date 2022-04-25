import email


class User :
   """
   Class that generates new instance of user
   """

   userlist = []
   def __init__(self,first_name,last_name,phone_number,password,email, ):
       self.first_name = first_name
       self.last_name = last_name
       self.phone_number = phone_number
       self.password = password
       self.email = email
       
   def  save_user(self):

        """
        save-user method is used to  create new user objects to the user_list 
        """     
        User.userlist.append(self)
   
   def delete_user(self):# delete method deletes saved user from the userlist
         
       User.userlist.remove(self)

   @classmethod
   def display_users(cls):
       return cls.userlist


   @classmethod
   def find_by_number(cls,number):

       for user in cls.userlist:
           if user.email == email:
               return user

             

       else:
            for user in cls.userlist:
                cls.userlist.remove(user)

class Credentials:
    """
    this class generates new instance of Credentials
    """

    user_accounts =[]
    def __init__(self,account_username,account_name,account_password):
        """
        init methos helps define properties of the object
        """

        self.account_username = account_username
        self.account_name = account_name
        self.account_password = account_password
    def save_account(self):
        """
        save account method saves user info in the accounts
        """

        Credentials.user_accounts.append(self)
        

    def delete_user_account(self):
        """
        delete_account  method removes the saved credentials from accounts
        """

        Credentials.user_accounts.remove(self)
    
    @classmethod
    def display_user_accounts(cls):
     return cls.user_accounts


    @classmethod
    def find_by_account_name(cls,user_accounts):

       for user in cls.user_accounts:
           if Credentials.user_accounts == user_accounts:
               return True

       else:
            for user in cls.user_accounts:
                cls.user_accounts.remove(user)
    

             