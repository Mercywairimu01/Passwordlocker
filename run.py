#!/usr/bin/env python3.9

import random
from user import User #import the User class
from credentials import Credentials #import the Credentials class
import pyperclip

def function():
	print("               ____                        _                       _    __ ")
	print("              |  _ \                      | |                     | |  / / ")
	print("              | |_) )  ____  ___   ___    | |     _____    _____  | | / /  ")
	print("              |  __/  / _  |/ __  / __    | |    / __  \  |  ___| | |/ /   ")
	print("              | |    / (_| |\__ \ \__ \   | |___(  (_)  ) | (___  | | \ \  ")
	print("              |_|    \_____| ___/  ___/   |_____|\_____/  |_____| |_|  \_\ ")
function()


def new_user_account(user_name,password):
    """
    create a new user account
    """
    new_user = User(user_name,password)
    return new_user

def save_user(User):
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
def save_credential(credential):
    '''
    function to save a newly created credential
    '''
    credential.save_credentials() 

def display_credentials():
    """
    Function which displays all saved credentials
    """
    return Credentials.display_credentials()

def find_credential(account_name):
    """
    Method that checks whether a particular account and its credentials exist based on searched account_name
    """
    return Credentials.find_credential_account(account_name)

def delete_credential(Credentials):
    """
    Method that deletes credentials
    """
    return Credentials.delete_credential(Credentials)    
    
def copy_credential(account_name):  
    """
    function to copy a credential details to the clipboard
    """
    return Credentials.copy_credential(account_name)
    
    
def generate_password(): 
    """
    Function to generate a password automatically
    """ 
    gen_pass = Credentials.generate_password()
    return gen_pass  
    
def main():

    while True:
        print("Welcome to PassWord Locker.")
        print('\n')
        print("Use these short codes to navigate through: Create New User use 'cu': Login to your account use 'lg' or 'ex' to exit password locker")
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
            print('\n')

            
        while True:
            print("Select an option below to continue: Enter cc -to create a new credential,dc -to display credentials,cp -to copy credentials,ex-exit")
            short_code = input().lower()
        
            if short_code == 'ex':               
                print(f'Goobye 😢 {entered_username}')

                break
            elif short_code =='cc':
                    
                    print("Enter credential details")
                    account_name =input("Enter name of account ")
                    account_password =input("Enter your account password")
                    
                    
                
                    while True:
                        print('Please choose an option for entering a password: ep-enter password, gp-generate password, ex-exit')
                        pwd_choice = input().lower()
                        if pwd_choice == 'ep':
                            print(" ")
                            account_password = input('Enter your password: ')
                            break
                        elif pwd_choice == 'gp':
                            account_password = generate_password(Credentials)
                            break
                        elif pwd_choice  == 'ex':
                            break
                        else:
                            print('Oops! wrong option entered. Try again.')
                        save_credential(create_new_credential(account_name,account_password))
                        print(f'Your credential has been created: Site name: {account_name}  -Password: {account_password}')
                        
                    
               
if __name__ == '__main__':
    main()