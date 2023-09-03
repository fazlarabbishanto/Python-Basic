#make a empty list for storing aliens.
aliens=[]

#make 30 green aliens.
for alien_number in range(30):
     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
     aliens.append(new_alien)
#changing there characteristics
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15
#show the fisrt 5 alien:
for alien in aliens[:10]:
    print(alien)
print("...")
