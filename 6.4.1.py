rivers={
    'nile':'egypt',
    'ganga':'india',
    'jamuna':'bangladesh',
    }
for name,country in rivers.items():

    print(f"The {name.title()} runs through {country.title()}")
    for river,country in rivers.items():
    print(f"\nRiver:{river.title()}")
    print(f"Country:{country.title()}")
    
