from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
import os
import base64
import getpass
class Authentication:
    __User_List = [
        {
            "Name": "Eric Paddler",
            "Username": "EricTheHasher",
            "Password": "ceZm8Vrgt/dBbz+Zz6NSRw==$SchJH4McbyxjawX58sWKDJB+otocJG9EPfby68kYB5Y=", #Password is Password123
            "Role": "Admin",
            "Email": "Eric.Paddler@gmail.com"
        },{
            "Name": "Ashley FuckOff",
            "Username": "ashley4707",
            "Password": "oQzLWc2wllOXm61Ve7a4sg==$LKgRKN89Mbzhqu5nCPIviNeGcANXhxWzLFq373tBZfM=", #Password is Password12345 (I think?)
            "Role": "Buyer",
            "Email": "ashley587@hotmail.ca"
        },{
            "Name": "Gabe Gabu",
            "Username": "Gabu011",
            "Password": "fuE7VSjVosTh7MNMrpdIVA==$RVfWV4RmX1QybtErhvmrVWciqQkY7LJ/1rL8vsYVVpk=", #Password is Password1234567
            "Role": "Seller",
            "Email": "SnickerGabu@yahoo.ca"
        }
    ]
    def __init__(self):
        self.Username = ""
        self.Role = ""

    @classmethod
    def __Hash_Password(self,Password, salt):
        iterations = 100000          # Number of iterations
        key_length = 32              # Desired key length in bytes (e.g., 32 for 256-bit)
        # Generate PBKDF2 hash
        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=key_length,
            salt=salt,
            iterations=iterations,
        )
        return kdf.derive(Password)
    

    def Login_Menu(self):
        Store_name = "The Night Hawk Dealer"
        print(f"Welcome to {Store_name}!")
        print(f"Please enter the following credentials to login.")
        EmailOrUsername_Input = input("Username or Email: ")
        Password = getpass.getpass(prompt="Enter your password: ")
        Username, Role = self.__class__.__Authenticate_Creds(EmailOrUsername_Input.strip(), Password)
        print(f"Successfully logged in as:\nUsername: {self.Username}\nRole: {self.Role}")
        
        self.Username = Username
        self.Role = Role
      
    @classmethod
    def __Authenticate_Creds(cls,EmailOrUsername_Input, password):
        Found = 0
        for user in cls.__User_List:
            print(user["Username"])
            if EmailOrUsername_Input == user["Username"] or EmailOrUsername_Input == user["Email"]:
                Salt_And_hash_List = user["Password"].split("$",2)
                salt = base64.b64decode(Salt_And_hash_List[0])
                Byte_password = password.encode("utf-8")
                if cls.__Hash_Password(Byte_password, salt) == (base64.b64decode(Salt_And_hash_List[1])):
                    print("MATCH!")
                    Found = 1
                    return user["Username"], user["Role"]
        if Found != 1:
            print("Credentials did not match!")
            return "Invalid", "Invalid"
          
    @property
    def Get_Info(self):
        return self.Username, self.Role
      
        #if[EmailOrUsername_Input]==[user["Username"]]or[EmailOrUsername_Input]==[user["Email"]]:print("Found user!")
        #^ Don't use this line lol. I just thought it was funny.

User1 = Authentication() #Creating an instance of authentication for User1.
User1.Login_Menu() # Calls the login GUI.
Info = User1.Get_Info #Will return 2 variables, Username, Role of instance User1.
Username = Info[0] # If you want to store the user's username.
Role = Info[1] #If you want to store the user's role.
print(Username)
print(Role)
