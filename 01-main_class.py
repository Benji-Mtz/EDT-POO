# Example of class

class Usuario():
    def __init__(self, name, last_name, email, password, phone):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone

    def hash_password(self):
        return "Hashing..."

    def verify_password(self):
        return "Verify pass"


# Instance of the class
user1 = Usuario(
    name="Benji",
    last_name="Mtz",
    email="benji@gmail.com",
    password="123",
    phone="5511223344"
)

print(user1.name)
print(user1.last_name)