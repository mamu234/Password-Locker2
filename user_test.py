import unittest 
from user import  User
# import pyperclip

class TestUser(unittest.TestCase):
    
    # Setup method runs before every test
    def setUp(self):
        self.user= User("Allan", "Walker", "076563738", "allanwarker@gmail.com","1234")
 
    # Teardown method runs after every test
    def tearDown(self):
        User.clear_all()

    # Test if instance is created(The __init__ method)
    def test_instance_creates_successfully(self):
        self.assertTrue(isinstance(self.user, User))

    # Test that contact is saved successfully
    def test_save_user(self):
        self.user.save()
        self.assertEqual(len(User.userlist),1)
        self.assertEqual(User.userlist[0].first_name, self.user.first_name)

    def test_find_all_users(self):
        self.assertEqual(len(User.userlist), len(User.find_all_users()))

    # Test that contact information can be updated successfully
    def test_update_user(self):
        self.user.save()

        User.update_first_name(1, "Paulo")
        User.update_email(1, "paulowalker@gmail.com")
        User.update_last_name(1, "Samuel")
        User.update_phone_number(1, "06573467")
        User.update_password(1,"2344")

        self.assertEqual(self.user.first_name, "Paulo")
        self.assertEqual(self.user.email, "paulowalker@gmail.com")
        self.assertEqual(self.user.last_name, "Samuel")
        self.assertEqual(self.user.phone_number, "06573467")
        self.assertEqual(self.user.password, "2344")



if __name__ == '__main__':
    unittest.main()