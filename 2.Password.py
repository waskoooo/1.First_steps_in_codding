username = input()
user_password = input()

data = input()
while data != user_password:
    data = input()
print(f"Welcome {username}!")