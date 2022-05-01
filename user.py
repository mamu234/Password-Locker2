

class User:

    userlist = []
   

    def __init__(self, first_name, last_name, phone_number, email,password):
      self.first_name = first_name
      self.last_name = last_name
      self.phone_number = phone_number
      self.email = email
      self.password = password
    

    def save_user(self):
     User.userlist.append(self)
    

    @property
    def full_name(self):
     return "{} {}".format(self.first_name, self.last_name)
    


    @classmethod
    def delete_user(cls, id):
        for user in cls.userlist:
            if user.id == id:
                cls.userlist.remove(user)
                return True
            else: return False

    # Here we print all contacts in the list as a dictionary
    # The @classmethod decorator tells python that this method belongs to the class
    @classmethod
    def print_users(cls):
        for user in cls.userlist:
            print(user.__dict__)
            
    # This method allows us to clear the whole list
    @classmethod
    def clear_all(cls):
        if(len(cls.userlist) == 0):
                return "Empty"
        else:
            for user in cls.userlist:
                cls.userlist.remove(user)
    
    @classmethod
    def delete_user(cls):
        for user in cls.userlist:
            if user == user:
                cls.userlist.remove(user)
                return True
            else: return False


    @classmethod
    def find_all_users(cls):
        return cls.userlist

    # We can use this method to update first_name after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its first name
    @classmethod
    def update_first_name(cls, id, name):
        for user in cls.userlist:
            if user.id == id:
                user.first_name = name

    # We can use this method to update last_name after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its last name
    @classmethod
    def update_last_name(cls, id, name):
        for user in cls.userlist:
            if user.id == id:
                user.last_name = name

    # We can use this method to update phone_number after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its phone_number
    @classmethod
    def update_phone_number(cls, id, phone_number):
        for user in cls.userlist:
            if user.id == id:
                user.phone_number = phone_number

    # We can use this method to update email after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its email
    @classmethod
    def update_email(cls, id, email):
        for user in cls.userlist:
            if user.id == id:
                user.email = email
    @classmethod
    def update_password(cls, id, password):
        for user in cls.userlist:
            if user.id == id:
                user.password = password
    
   
             

    
class Credentials:

    credentialslist = []
    id = 0

    def __init__(self, first_name, last_name, phone_number, email,password):
      self.first_name = first_name
      self.last_name = last_name
      self.phone_number = phone_number
      self.email = email
      self.password = password
    

    def save(self):
        if len(Credentials.credentialslist) == 0:
            self.id = 1
            Credentials.id  = 1
            self.credentialslist.append(self)
        else:
            Credentials.id += 1
            self.id = Credentials.id
            self.credentialslist.append(self)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    


    @classmethod
    def delete_credential(cls, id):
        for user in cls.credentialslist:
            if user.id == id:
                cls.credentialslist.remove(user)
                return True
            else: return False

    # Here we print all contacts in the list as a dictionary
    # The @classmethod decorator tells python that this method belongs to the class
    @classmethod
    def print_credentials(cls):
        for credential in cls.credentialslist:
            print(credential.__dict__)
            
    # This method allows us to clear the whole list
    @classmethod
    def clear_all(cls):
        if(len(cls.credentialslist) == 0):
                return "Empty"
        else:
            for credential in cls.credentialslist:
                cls.credentialslist.remove(credential)
    
    @classmethod
    def delete_credential(cls):
        for credential in cls.credentialslist:
            if credential == credential:
                cls.credentialslist.remove(credential)
                return True
            else: return False


    @classmethod
    def find_all_credentials(cls):
        return cls.credentialslist

    # We can use this method to update first_name after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its first name
    @classmethod
    def update_first_name(cls, id, name):
        for credential in cls.credentialslist:
            if credential.id == id:
                credential.first_name = name

    # We can use this method to update last_name after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its last name
    @classmethod
    def update_last_name(cls, id, name):
        for credential in cls.credentialslist:
            if credential.id == id:
                credential.last_name = name

    # We can use this method to update phone_number after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its phone_number
    @classmethod
    def update_phone_number(cls, id, phone_number):
        for credential in cls.credentialslist:
            if credential.id == id:
                credential.phone_number = phone_number

    # We can use this method to update email after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its email
    @classmethod
    def update_email(cls, id, email):
        for credential in cls.credentialslist:
            if credential .id == id:
                credential .email = email
    @classmethod
    def update_password(cls, id, password):
        for credential  in cls.credentialslist:
            if credential .id == id:
                credential .password = password


    
  


   
    

             