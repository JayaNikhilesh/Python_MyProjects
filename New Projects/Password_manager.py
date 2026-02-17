from cryptography.fernet import Fernet

'''
def key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
key() 
'''

def load():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

pwd = input("what is the master password? ")
key = load() + pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user , "\nPassword:", fer.decrypt(passw.encode()).decode())
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open ('password.txt','a') as f:         #file = open('password.txt','a')    file.close()
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add new password or view existing password (view , add, q to quit)? ").lower()

    if mode == "q":
        quit()

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("invalid mode")