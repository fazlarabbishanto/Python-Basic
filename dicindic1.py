users={
       'frabbi':{
           'first':'fazla',
           'last':'rabbi',
           'location':'khulna',
            },
       'mrahman':{
           'first':'mazedur',
           'last':'rahman',
           'location':'dhaka',
       },

}
for user,user_info in users.items():
    print(f"\nUsername:{user}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=f"{user_info['location']}"
    print(f"\tFull name is: {full_name.title()}")
    print(f"\tLocation is :{location.title()}")