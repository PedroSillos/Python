a_string = "There are all these dimensions, worlds, alternate realities, and they're all right on top of each other."
a_list = a_string.split()
print(a_string)
print(a_list)
print(len(a_string))
print(len(a_list))

a_string = "There are all these                     dimensions                   , worlds, alternate realities, and they're all right on top of each other."
a_list = a_string.split()
print(a_string)
print(a_list)

a_string = "There are all these                     dimensions                   , worlds, alternate realities, and they're all right on top of each other."
a_string = a_string.replace(",","")
a_list = a_string.split()
dimensions = a_list[4]
print(a_string)
print(a_list)
print(dimensions.upper())
dime = dimensions.split("n")
print(dime[0].upper())
a_list.sort()
print(a_list)
