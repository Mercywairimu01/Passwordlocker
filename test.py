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
