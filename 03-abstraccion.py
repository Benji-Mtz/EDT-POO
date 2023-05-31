from cryptocode import encrypt, decrypt

# abstraction based class = ABC, necesary for this concept
from abc import ABC, abstractmethod

class UserBase(ABC):
    def __init__(self, name, last_name, email, password, phone):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = self.encrypt_pass(password)
        self.phone = phone

    @abstractmethod
    def encrypt_pass(self, password):
        pass
    
    @abstractmethod
    def decrypt_pass(self, password):
        pass
    
class DefiniteUser(UserBase):
    
    def encrypt_pass(self, password):
        return encrypt(password, "secret")
    
    def decrypt_pass(self, password):
        decrypt_password = decrypt(self.password, "secret") 
        # Return true or false
        return decrypt_password == password
    
    
user1 = DefiniteUser(
    name="Benji",
    last_name="Mtz",
    email="benji@gmail.com",
    password="123",
    phone="5511223344"
)

print(user1.password)
print(user1.decrypt_pass("123"))