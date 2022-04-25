#!/usr/bin/env python3.9

import random
from user import User #import the User class
from credentials import Credentials #import the Credentials class
import pyperclip

def function():
	print("               ____                        _                       _    __ ")
	print("              |  _ \                      | |                     | |  / / ")
	print("              | |_) )  ____  ___   ___    | |     _____    _____  | | / /  ")
	print("              |  __/  / _  |/ __  / __    | |    / __  \  /  ___| | |/ /   ")
	print("              | |    / (_| |\__ \ \__ \   | |___(  (_)  )|  (___  | | \ \  ")
	print("              |_|    \_____| ___/  ___/   |_____|\_____/  \_____| |_|  \_\ ")
function()


def new_user_account(user_name,password):
    """
    create a new user account
    """
    new_user = User(user_name,password)
    return new_user

def save_user():
    """
    Function to save a new user account
    """
    User.save_user()
    
def create_new_credential(account_name, account_password):
    """
    Function to create a new account and its credentials
    """
    new_credential = Credentials(account_name, account_password)
    return new_credential
def save_credentials(self):
    '''
    function to save a newly created credential
    '''
    return Credentials.save_credentials(self) 

def display_credentials():
    """
    Function which displays all saved credentials
    """
    return Credentials.display_credentials()

def  find_credential_account(account_name):
    """
    Method that checks whether a particular account and its credentials exist based on searched account_name
    """
    return Credentials.find_credential_account(account_name)

def delete_credential(self):
    """
    Method that deletes credentials
    """
    return Credentials.delete_credential(self)    
    
def copy_credential(account_name):  
    """
    function to copy a credential details to the clipboard
    """
    return Credentials.copy_credential(account_name)
    
    
# def generate_password(): 
#     """
#     Function to generate a password automatically
#     """ 
#     gen_pass = Credentials.generate_password()
#     return gen_pass  
    
def main():

    while True:
        print("Welcome to PassWord Locker.")
        print('\n')
        print("Use these short codes to navigate through: Create New User use 'cu' & 'ex' to exit password locker")
        short_code = input().lower()
        print('\n')
        
        if short_code == 'cu':
        
            print("Create your Username:")
            entered_user_name = input()
            
            print("Create your Password")
            entered_user_password = input()
            
            print("Confirm your Password")
            confirm_password = input()
            
            while confirm_password != entered_user_password:
                print("Sorry your passwords did not match!")
                print("Enter a password")
                entered_user_password  = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {entered_user_name}! You have created your new account.")
                print('\n')
                print("Proceed to Log In to your Account")
                print("Username")
                entered_username = input()
                print("Your Password")
                entered_password = input()
            while entered_username != entered_user_name or entered_password != entered_user_password:
                print("Invalid username or password")
                print("Username")
                entered_username = input()
                print("Your Password")
                entered_password = input()
            else:
                print(f"Welcome: {entered_username} to your Account")
                print(f'Your password is {entered_password}')
                print('\n')

                
            while True:
                print("Select an option below to continue: Enter cc -to create a new credential,dc -to display credentials,cp -to copy credentials,del -to delete credentials,ex-exit")
                short_code = input().lower()
            
                if short_code == 'ex':               
                    print(f'Goobye 😢 {entered_username}')

                    break
                elif short_code =='cc':
                        
                        print("Enter credential details")
                        account_name1 =input("Enter name of account ")
                        print('\n')
                        # account_password =input("Enter your account password")
        
                        while True:
                            print('Please choose an option for entering a password: ep-enter password, gp-generate password')
                            pwd_choice = input().lower()
                            if pwd_choice == 'ep':
                                print(" ")
                                account_password1 = input('Enter your password: ')
                                print('\n')
                                
                                break
                            elif pwd_choice == 'gp':
                                account_password1 = Credentials.generate_password(6)
                                print(f"Generated password is: {account_password1} ")
                                print('\n')
                                
                                break
                            
                            else:
                                print('Oops! wrong option entered. Try again.')
                        save_credentials(create_new_credential(account_name1,account_password1))
                        print('Your credential has been created:')
                        print(f'Site name: {account_name1}') 
                        print(f'Site name: {account_password1}')
                        
                    
                elif short_code =='dc':
                      
                           
                        if display_credentials():
                            print("Here is a list of all your credentials")
                            for Credentials in display_credentials():
                                print(f'Site name: {Credentials.account_name}')
                                print(f'Site password: {Credentials.account_password}')
                        else:
                                print("you dont have any credentials saved yet 🥵")
                                
                elif short_code == 'cp':
                    chosen_site = input('Enter site name for the credential password to copy: ')
                    copy_credential(chosen_site)
                    
                elif short_code =='del':
                    print("Search for credential account to delete")

                    account_name = input()

                    if find_credential_account(account_name):
                        search_credential = find_credential_account(account_name)
                    print(f"ACCOUNT NAME: {search_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                    print("Delete? y/n")
                    sure = input().lower()
                    if sure == 'y':
                        delete_credential(search_credential)
                        print("Account SUCCESSFULLY deleted")
                        break
                    elif sure == 'n':
                        continue

                    else:
                        print("That Credential does not exist")
                        break 
        elif short_code == 'ex':               
            print('Goobye 😢 You have exited the Password locker')

            break
        else:
           print("Please Enter a valid code to continue")                  
               
if __name__ == '__main__':
    main()