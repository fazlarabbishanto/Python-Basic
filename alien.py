print("What is about your speed ?Is it slow,medium or fast?")
alien={'x_position':0,'y_position':25,'speed':input()}
print(f"Orginal position:{alien['x_position']}")
#Move the alien to right
#Determine how far to move the alien based on its current  speed.
if alien['speed']=='slow':
    x_increment=1
elif alien['speed']=='medium':
    x_increment=2
else:
    #This must be  fast alien.
    x_increment=3
#This new position is the oldd position  plus  the increment.
alien['x_position']=alien['x_position']+x_increment

print(f"New position:{alien['x_position']}")