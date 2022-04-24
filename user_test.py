import unittest 
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user= User("carolyne","Maunda","0721830476","1234", "pcmaunda@gmail.com") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"carolyne")
        self.assertEqual(self.new_user.last_name, "Maunda")
        self.assertEqual(self.new_user.phone_number,"0721830476")
        self.assertEqual(self.new_user.email,"pcmaunda@gmail.com")
        self.assertEqual(self.new_user.password,"1234")


if __name__ == '__main__':
    unittest.main()