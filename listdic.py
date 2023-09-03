favorite_language={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskel'],
 }
for name,languages in favorite_language.items():
    print(f"\n{name.title()}'s favorite laguage is")
    for language in languages:
        print(f"\t{language.title()}")