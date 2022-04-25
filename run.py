from user import User


def create_user(first_name,last_name,phone_number,email):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,phone_number,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_users()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)

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
        first__name = input()

        print("Last name ...")
        last_name = input()

        print("Phone number ...")
        phone_number = input()

        print("Email address ...")
        e_address = input()
        
        save_users(create_user(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
    

   