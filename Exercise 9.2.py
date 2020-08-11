#What is the name that appears the most?
names_counter = dict()
names_counter['csev'] = 1
names_counter['cwen'] = 1
names_counter['csev'] = names_counter['csev'] + 1
print(names_counter)
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else: 
        counts[name] = counts[name] + 1
print(counts)

x = counts.get('csev', 0)
print(x) #2

counts = dict()
name = input("Type a name: ")
while name.upper() != 'DONE' and name.upper() != 'FIM':
    counts[name] = counts.get(name,0) + 1
    name = input("Type a name: ")

el_major = 0
major_nombre = None

for name in counts:
        if counts[name] > el_major:
            el_major = counts[name]
            major_nombre = name
print('Highest is "' + str(major_nombre) + '" with ' + str(el_major) + ' ocurrencies.')