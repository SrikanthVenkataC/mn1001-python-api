def login(username, pwd):
    if username == pwd:
        return True 
    else:
        return False

print(login("sachin","sachin"))
print(login("sachin","tendulkar"))