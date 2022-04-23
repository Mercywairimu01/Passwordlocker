from typing_extensions import Self


class User:
    """
    Class that generates new instance of users.
    """
    
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
    