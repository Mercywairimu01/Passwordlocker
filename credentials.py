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