# *************************WELLCOME USER **********************************

Operation=input("Login or Sign up : ")

#login page 
def login():
    login=input("Enter Name: ")
    if login=="admin123":
        print("Valid admin")
    else:
       print("wrong admin!!")
    password=input("Password: ")
    if password=="hey":
      print("Access Granted")
      print("Wellcome back....")
    else:
      print("Not granted!!")
# sign up page 
def sign_up():
    sign=input("Create name: ")
    if len(sign)>3:
        print("Welcome",sign)
    else:
        print("Please keep letter above 3")
    password1=int(input("Create password: "))
    if password1>6:
        print("welcome",sign)
    else:
        print("Password is too short")
if Operation=="login":
    print(login())
elif  Operation=="sign up":
    print(sign_up())
else:
    print("Atleast choose one option!!!")