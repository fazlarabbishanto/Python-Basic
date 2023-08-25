current_users=['araf','akhtarul','mahraf','opu','shanto']
new_users=['araf','Akhtarul','Jarin','Arnob','mehefil']
for username in new_users:
    if username.lower() in current_users :
        print(f"Hello {username.title()} .The username is already in use,please use a different one.")
    else:
        print(f"Hello {username.title()} .The username is avaiable.")
