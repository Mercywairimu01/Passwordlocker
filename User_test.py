import unittest #import the unittest module
from user import User #import the User class
import pyperclip


class TestUser(unittest.TestCase):
    """
    A test class that defines test cases for the User class
    """
    
    def setUp(self):
        """
         Set up method to run before each test cases.
        """
        self.new_user = User("NewUser","0000")
        
    # def tearDown(self):
    #     """
    #     Method that clears the credentials_array after every test to ensure that there is no error
    #     """
    #     Credentials.Credentials_array = [] 
        
    def test_init(self):
        """
        Test to ensure that the initialization of the User instance is done properly
        """   
        self.assertEqual(self.new_user.user_name, "NewUser")
        self.assertEqual(self.new_user.password, "0000")
    def test_save_user(self):
         """
         A test case to test if the User is saved in the User list
         """
         self.new_user.save_user()   #saving the new User
         self.assertEqual(len(User.user_list),1)
         

if __name__ == '__main__':
    unittest.main()