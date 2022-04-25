import pyperclip

from credentials import Credentials
class User:
    """
    Class that generates new instance of users.
    """  
    user_list = []   #empty users list
    
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        
    def save_user(self):
        '''
        Function to save a newly created user instance
        '''
        User.user_list.append(self)
   
   