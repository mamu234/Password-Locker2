

class User:

    userlist = []
    def __init__(self, first_name, last_name, phone_number, email,password):
      self.first_name = first_name
      self.last_name = last_name
      self.phone_number = phone_number
      self.email = email
      self.password = password
    

    def save_user(self):

      self.userlist.append(self)
    
    @classmethod
    def delete_user(cls):
        for user in cls.userlist:
            if user == user:
                cls.userlist.remove(user)
                return True
            else: return False


 
    
   
             

    


    
  


   
    

             