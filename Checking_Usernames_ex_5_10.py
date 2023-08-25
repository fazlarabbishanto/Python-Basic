current_users=['araf','akhtarul','mahraf','opu','shanto']
new_users=['araf','akhtarul','jarin','arnob','mehefil']
for username in new_users:
    if username in current_users:
        print(f"Hello {username.title()}.The username is already in use,please use a different one.")
    else:
        print("The username is avaiable.")
