import json, hashlib, os, time, sys, getpass

def login():
  username = input("Username: ")
  userhashfilename = username.encode('utf-8')
  userhashfilename = hashlib.sha512(userhashfilename).hexdigest()

  file = open(f'users/{userhashfilename}.json')
  user_dict = json.load(file)
  username = username.encode('utf-8')
  userhash = hashlib.sha512(username).hexdigest()
  if(userhash == user_dict['username']):
    password = getpass.getpass("Password: ")
    password = password.encode('utf-8')
    passhash = hashlib.sha512(password).hexdigest()
    if(passhash == user_dict['password']):
      print("Logged in...\n")
      time.sleep(0.25)
      clear()
      #call function that you want to run after login
    else:
      print("Invalid password.")
      time.sleep(1)
      clear()
      menu()
    

def new_user():
  username = input("Username: ")
  userhashfilename = username.encode('utf-8')
  userhashfilename = hashlib.sha512(userhashfilename).hexdigest()

  if(os.path.exists(f'users/{userhashfilename}.json') != True):
    password = getpass.getpass("Password: ")
    if(username != '' and password != ''):
      with open(f'users/{userhashfilename}.json', 'w+') as file:
        username = username.encode('utf-8')
        password = password.encode('utf-8')
        userhash = hashlib.sha512(username).hexdigest()
        passhash = hashlib.sha512(password).hexdigest()

        user_json = {
        'username': userhash,
        'password': passhash
        }

        file.write(json.dumps(user_json, indent=4))
        file.close()
  else:
    print("Username taken.")
    time.sleep(1)
    clear()
    menu()

def menu():
  userInput = input("Login or sign up: ")
  if(userInput.lower() == 'login'):
    login()
  elif(userInput.lower() == 'sign up'):
    new_user()

def clear():
    os.system("cls")
    
#start program
menu()
