from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open( "key.key" , "wb" ) as key_file:
        key_file.write(key)

write_key()
'''


def load_key():
    file = open( "key.key" , "rb" )
    key = file.read()
    file.close
    return key



master_pwd = input(" What is your Master Password ? ")

#  master_pwd == "456":

key = load_key() + master_pwd.encode()
fer = Fernet(key)
   


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")

            print( "User : " , user , "| Password :" ,
                    fer.decrypt(passw.encode()).decode() )
            

            #  ALSO A WAY : 
            # decrypted_passw = fer.decrypt(passw.encode()).decode()
            # print("User:", user, ", Password:", decrypted_passw)


def add():
    name = input( " Account Name : " )
    password = input( " Password : " )

    with open('passwords.txt', 'a') as f:
        f.write(name + " | "  + fer.encrypt(password.encode()).decode() + "\n")




if master_pwd == "456":
    while True:
    
        mode = input( " Would you like to Add and new password or View the existing ones ( view , add )? Press 'q' to quit. ").lower()

        if mode == "q":
            break


        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print(" Invalid Mode. ")
            continue

else:
    print("Wrong Password!")        