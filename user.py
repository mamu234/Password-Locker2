import pyperclip


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
   def copy_email(cls,number):
    contact_found = User.find_by_number(number)
    pyperclip.copy(contact_found.email)

   @classmethod
   def find_by_number(cls,number):

       for user in cls.userlist:
           if user.phone_number == number:
               return user

             

       else:
            for user in cls.userlist:
                cls.userlist.remove(user)

class Credentials:
    """
    this class generates new instance of Credentials
    """

    credentials_list =[]
    def __init__(self,account_username,account_name,account_password,email):
        """
        init methos helps define properties of the object
        """

        self.account_username = account_username
        self.account_name = account_name
        self.account_password = account_password
        self.email = email
        
    def save_credentials(self):
        """
        save account method saves user info in the accounts
        """

        Credentials.credentials_list.append(self)
    
        

    def delete_user_account(self):
        """
        delete_account  method removes the saved credentials from accounts

        """
    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found user
        '''
    def test_display_all_credentials(self):
        '''
        method that returns a list of all accounts saved
        '''
    def test_save_multiple_credentials(self):
        


        Credentials.credentials_list.remove(self)
    
    @classmethod
    def display_user_accounts(cls):
     return cls.credentials_list


    @classmethod
    def find_by_account_name(cls,number):

       for user in cls.credentials_list:
           if Credentials.credentials_list == number:
               return True

       else:
            for user in cls.credentials_list:
                cls.credentials_list.remove(user)
    

             