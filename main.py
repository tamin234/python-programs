from getpass import getpass
import doctor
import manager
import os

def login():
    while True:
        os.system('clear')
        username = input("Username: ")
        password = getpass("Password: ")
        with open('database/users.txt', 'r') as f:
            for line in f:
                x=line.strip()
                if x:
                    u, p, role = x.split(',')
                    if u == username and p == password:
                        if role=="doctor":
                            os.system("clear")
                            doctor.menu()
                        elif role=="manager":
                            os.system("clear")
                            manager.menu()
        print("Wrong! Try again...")
        input("Press Enter...")
        
    
if __name__=="__main__":
    print(login())