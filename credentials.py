import string
import pyperclip
import random # Import random module

class Credentials:
    """
    Class for credentials
    """
    Credentials_array= [] #empty credentials list
    def __init__(self,account_name,account_password):
        """
        define the properties of the credentials object
        """
        self.account_name =account_name
        self.account_password =account_password
        
    def save_credentials(self):
        """
        saves a new credential instance
        """   
        Credentials.Credentials_array.append(self) 
        
    def delete_credential(self):
        """
        Function to delete a saved credential from the credential_array
        """  
        Credentials.Credentials_array.remove(self)
        
    @classmethod
    def  find_credential_account(cls,account_name):
        """
        Finds credential matching the searched account name
        Args:
            name: account_name that has a password
        Returns:
            The account_name and it's corresponding PassWord
        """

        for credential in cls.Credentials_array:
            if credential.account_name == account_name:
                return credential
            
    @classmethod
    def copy_credential(cls,account_name):
        '''
        class method that copies credential info after site name is entered
        '''
        find_credential = Credentials.find_credential_account(account_name)
        return pyperclip.copy(find_credential.account_password)  
     
    @classmethod
    def display_credentials(cls):
        """
        Method which displays all current credentials
        """
        return cls.Credentials_array
    def generate_password(self):
        """
        Generate a random password string of letters and digits and special characters
        """
        characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"
        
        password_length = 6
        
        password = "".join(random.sample(characters, password_length))
        
        return password