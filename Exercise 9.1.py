#Dictionaries - key and values
#In perl or php: associative arrays
#Map or HashMap in Java
#Property Bag - C# / .NET

purse = dict()
purse['money'] = 100
purse['candy'] = 4
purse['tissues'] = 20

print(purse)

for item in purse:
    print(item)

print(purse['money'])

purse['money'] = purse['money'] + 10000000000 #lava-jato

print(purse)

print(purse['money'])

#see lists_vs_dictionaries.png