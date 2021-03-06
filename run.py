
from collections import UserList
from numpy import number, str_
from user import User


def create_user(first_name,last_name,phone_number,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,phone_number,email,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''

def del_user(user):
    '''
    Function to delete a user
    '''
   

def find_all_users(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_all_users()


def check_existing_users(user):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.update_first_name()


def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.update_phone_number()
  

def main():
    print("Hello Welcome to your userlist. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list ")

        short_code = input().lower()

        if short_code == 'cc':
         print("New Users")
         print("-"*10)

         print ("First name ....")
         first_name = input()

         print("Last name ...")
         last_name = input()

         print("Phone number ...")
         phone_number = input()

         print("Email address ...")
         email = input()
        
         print("Password ...")
         password = input()
        
         save_user(create_user(first_name,last_name,phone_number,email,password)) # create and save new user
         print ('\n')
         print(f"New User {first_name} {last_name} {phone_number} {email} {password} created")
         print ('\n')
        
        elif short_code == 'dc':

                if find_all_users(UserList):
                        print("Here is a list of all your users")
                        print('\n')

                        for user in display_users(user):
                         print(f"{user.first_name} {user.last_name}....{user.phone_number}")

                         print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any users saved yet")
                        print('\n')

        elif short_code == 'fc':

               print("Enter the number you want to search for")

               check_existing_users = input()
               if check_existing_users ():
                        search_user = check_existing_users()
                        print(f"{search_user.first_name} {search_user.last_name}")
                        print('-' * 20)

                        print(f"Phone number.......{search_user.phone_number}")
                        print(f"Email address.......{search_user.email}")
               else:
                        print("That user does not exist")

        elif short_code == "ex":
                    print("Bye .......")
                    break
        else:
            print("I really didn't get that. Please use the short codes")
    
if __name__ == '__main__':

    main()

   