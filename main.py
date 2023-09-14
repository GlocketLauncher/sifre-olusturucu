import random

characters = "@+-!'^$%&/(=?*1234567890qwertyuopasdfghjklşizxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
length = int(input("Şifre ne kadar uzun olsun?"))

while True:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    if not any(password[i] == password[i+1] for i in range(len(password)-1)):
        break

print(password)
