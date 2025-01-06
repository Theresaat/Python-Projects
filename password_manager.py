main_pwd= input("What is the master password? ")
def view():
    pass
def add():
    name = input("Account Name: ")
    pwd = input("password: ")

    with open("passwords.txt", "a") as f:
        f.write(name +" | " +pwd + "\n")

while True: 
    mode = input("Would you like to add a new password or view existing ones (view, add)? ") 
    if mode == "view":
        pass