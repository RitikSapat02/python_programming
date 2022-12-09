class user(object):
    def sign_in(self):
        print("Logged in")
    
class wizard(user,object):
    pass

class Archer(user):
    pass

wizard1 = wizard()
wizard1.sign_in()

print(isinstance(wizard1,user))
print(isinstance(wizard1,object))