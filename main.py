import random
import string


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
password = []

length = int(input("Input your password length: "))

random.shuffle(characters)

for i in range(length):
    password.append(random.choice(characters))

password_result = "".join(password)

print(password_result)