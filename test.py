import unittest #import the unittest module
from user import User #import the User class
from credentials import Credentials #import the Credentials class
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
        
    def tearDown(self):
        """
        Method that clears the credentials_array after every test to ensure that there is no error
        """
        Credentials.Credentials_array = [] 
        
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
         
class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the Credentials class behavior
    """     
       
    def setUp(self):
         """
         Set up method to run before each Credentials' test case 
         """ 
         self.new_credential =Credentials("Facebook","0000")
         
    def tearDown(self):
        """
        Method that clears the credentials_array after every test to ensure that there is no error
        """
        Credentials.Credentials_array = []      
    def test__init(self):
        """
        test to check if initialization of the Credentials class is properly done
        """
        self.assertEqual(self.new_credential.account_name,"Facebook")
        self.assertEqual(self.new_credential.account_password,"0000")
     
    def test_save_credentials(self):
        '''
        test case to test if the credential is saved into the credentials array
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.Credentials_array),1)
        
    def test_save_more_credentials(self):
        """
        test to check if a new credentials will be saved in the credentials array
        """ 
        self.new_credential.save_credentials()
        twitterCredential=Credentials("Twitter","1234")
        twitterCredential.save_credentials()
        self.assertEqual(len(Credentials.Credentials_array),2)
        
    def test_find_credential_account (self):
        """
        Test to see if we can find credential by account name
        """  
        self.new_credential.save_credentials() 
        twitterCredential=Credentials("Twitter","1234")
        twitterCredential.save_credentials()
        find_credential =Credentials.find_credential_account("Twitter")
        self.assertEqual(find_credential.account_name, twitterCredential.account_name)
        self.assertTrue(find_credential)
        
    def test_delete_credential(self):
        """
        test to check whether we can remove a credential from the list
        """
       
        self.new_credential.save_credentials()
        twitterCredential = Credentials("Twitter","1234")
        twitterCredential.save_credentials()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.Credentials_array),1)
        
    def test_copy_credential(self):
        '''
        Test to check if the copy credential method works
        '''
        self.new_credential.save_credentials()   
        twitterCredential=Credentials("Twitter","1234")
        twitterCredential.save_credentials()
        find_credential = None
        
        for credential in Credentials.Credentials_array:
            find_credential = Credentials.find_credential_account(credential.account_name)
            return pyperclip.copy(find_credential.account_password)
        Credentials.copy_credential(self.new_credential.account_name)
        self.assertEqual("1234",pyperclip.paste())
        print(pyperclip.paste())
        
    def test_display_all_credentials(self):
        """
        TestCase to test whether all contacts can be displayed
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.Credentials_array)    
        
if __name__ == '__main__':
    unittest.main()