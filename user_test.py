import unittest 
from user import  User
# import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user= User("carolyne","Maunda","0721830476","pcmaunda@gmail.com","1234") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"carolyne")
        self.assertEqual(self.new_user.last_name, "Maunda")
        self.assertEqual(self.new_user.phone_number,"0721830476")
        self.assertEqual(self.new_user.email,"pcmaunda@gmail.com")
        self.assertEqual(self.new_user.password,"1234")
   
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.userlist),1)


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.userlist = []

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple users
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0721830476","pcmaunda@gmai.com","1234") # new contact
            test_user.save_user()
            self.assertEqual(len(User.userlist),2)
        
    def test_delete_user(self):
            '''
            test_delete_user tests if we can remove a user from our userlist
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0721830476","pcmaunda@gmail.com","1234") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.userlist),1)

#     def test_find_user_by_number(self):
#         '''
#         test to check if we can find a contact by phone number and display information
#         '''

#         self.new_user.save_user()
#         test_user = User("Test","user","0721830476","pcmaunda@gmail.com","1234") # new user
#         test_user.save_user()

#         found_user = User.find_by_number("0721830476")

#         self.assertEqual(found_user,test_user.phone_number)


#     def test_user_exists(self):
#         '''
#         test to check if we can return a Boolean  if we cannot find the cuser.
#         '''

#         self.new_user.save_user()
#         test_user = User("Test","user","0721830476","pcmaunda@gmail.com","1234")
#         test_user.save_user()
#         user_exists = User.save_user("0721830476")
#         self.assertTrue(user_exists)
    
    
#     def test_display_all_users(self):
#         '''
#         method that returns a list of all users saved
#         '''

#         self.assertEqual(User.display_users(),User.userlist)

#     def copy_email(self):
#         '''
#         Test to confirm that we are copying the email address from a found user
#         '''

#         self.new_user.save_user()
#         User.copy_email("0721830476")

#         self.assertEqual(self.new_user.email,pyperclip.paste())
    
#     @classmethod
#     def copy_email(cls,number):
#         contact_found = User.find_by_number(number)
#         pyperclip.copy(contact_found.email)


# class TestCredentials(unittest.TestCase):
#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_credential= Credentials("carolyne","Maunda","12345","pcmaunda@gmail.com") # create credential object


#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properly
#         '''

#         self.assertEqual(self.new_credential.account_username,"carolyne")
#         self.assertEqual(self.new_credential.account_name, "Maunda")
#         self.assertEqual(self.new_credential.account_password,"12345")
#         self.assertEqual(self.new_credential.email,"pcmaunda@gmail.com")
       
    
#     def test_save_credentials(self):
#         '''
#         test_save_credential  test case to test if the credential object is saved into
#          the  accountlist
#         '''
#         self.new_credential.save_credentials() 
#         self.assertEqual(len(Credentials.save_credentials),1)


#     def tearDown(self):
#             '''
#             tearDown method that does clean up after each test case has  run.
#             '''
#             Credentials.credentials_list = []

#     def test_save_multiple_credentials(self):
#             '''
#             test_save_multiple_credentials to check if we can save multiple crdentials
#             objects to our user_accounts
#             '''
#             self.new_credential.credentials_list()
#             test_credential = Credentials("Test","credential","carolyne","maunda")
#             test_credential.credentials_list()
#             self.assertEqual(len(Credentials.credentials_list),2)
        
#     def test_delete_credential(self):
#             '''
#             test_delete_credential tests if we can remove a  credential  from our user_accounts
#             '''
#             self.new_credential.credentials_list()
#             test_credential = Credentials("Test","credential","carolyne","maunda")
#             test_credential.credentials_list()

#             self.new_credential.delete_credentials()# Deleting a user object
#             self.assertEqual(len(Credentials.credentials_list),1)

   
#     def test_credential_exists(self):
#         '''
#         test to check if we can return a Boolean  if we cannot find the account.
#         '''

#         self.new_credential.credentials_list()
#         test_credential = Credentials("Test","credential","carolyne","maunda")
#         test_credential.credentials_list()

#         credential_exists = Credentials.credentials_list("carolyne")

#         self.assertTrue(credential_exists)
    
    
#     def test_display_all_credentials(self):
#         '''
#         method that returns a list of all accounts saved
#         '''

#         self.assertEqual(Credentials.display_all_credentials(),Credentials.credentials_list)

#     def test_copy_email(self):
#         '''
#         Test to confirm that we are copying the email address from a found account
#         '''


#         self.assertEqual(self.new_credential.email,pyperclip.paste())
    
#     @classmethod
#     def copy_email(cls,number):
#         credential_found = Credentials.find_by_number(number)
#         pyperclip.copy(credential_found.email)



if __name__ == '__main__':
    unittest.main()