#a list is a type of collection that stores many values in a single variable
friends = ['Ross','Chandler','Monica','Phoebe','Rachel','Joe']
print(friends)
#lists can have different types inside, even lists
print( [ 1,990004,'Gunther', 0.3, friends, [] ] )

other_list = [ 1,990004,'Gunther', 0.3, friends, [] ]
i = 1
for element in other_list:
    print("Element number "+str(i)+": "+str(element))
    i = i +1




str_fruit = 'banana'
list_fruit = ['b','a','n','a','n','a']

#We can read a string index, but can´t overwrite it:
print(str_fruit[0])
try:
    str_fruit[0] = '1'
    print(str_fruit[0])
except:
    print("We can read a string index, but can´t overwrite it!")

#We can read a list index, and we CAN overwrite it:
print(list_fruit[0])
try:
    list_fruit[0] = '1'
    print(list_fruit[0])
    print("We can read a string index, and we CAN overwrite it")
except:
    exit()

print(len(str_fruit))
print(len(list_fruit))

print( list(range(4)) )

print( list( range( len(str_fruit) ) ) )

print(list_fruit+list_fruit)
print(str_fruit+str_fruit)

print( list_fruit[0:10] )
print( list_fruit[3:10] )

a_list = list()
print(type(a_list))
#print(dir(a_list))

print("A list: ",a_list)
a_list.append('alall')
a_list.append('123')
a_list.append('132')
a_list.append('213')
a_list.append('231')
a_list.append('312')
a_list.append('321')
print("A list: ",a_list)

print("123 in list:",123 in a_list)
print("'123' in list:",'123' in a_list)

print(len(a_list))
print(max(a_list))
print(min(a_list))

a_list = [1,2,3,4,5,6,7,8,9]
print(sum(a_list))
print(sum(a_list)/len(a_list))