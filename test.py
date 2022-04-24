import unittest #import the unittest module
from user import User #import the User class
from credentials import Credentials #import the Credentials class

class TestUser(unittest.TestCase):
    """
    A test class that defines test cases for the User class
    """
    
    def setUp(self) :
        """
         Set up method to run before each test cases.
        """
        self.new_user = User("NewUser","0000")
        
    def test_init(self):
        """
        Test to ensure that the initialization of the User instance is done properly
        """   
        self.assertEqual(self.new_user.user_name, "NewUser")
        self.assertEqual(self.new_user.password, "0000")

         
if __name__ == '__main__':
    unittest.main()