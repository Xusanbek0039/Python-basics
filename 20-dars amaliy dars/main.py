from login import login_user
from register import register_user


qiymat = input("Ro'yxatdan o'tish y, tizimga kirish x: ")
while True:
    if qiymat == "y":
        register_user()
    elif qiymat == "x":
        login_user()
    else:
        break