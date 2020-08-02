print("***Before***")
largest_number = -1
for number in [9, 42, 20, 3, 74, 15]:
    print(number)
    if number > largest_number:
        print("New largest is:",number)
        largest_number = number
print("***After***")
print("Largest is:",largest_number)

count = 0
print("***Start***",count)
for number in [67, 3333, 34568, 34, 13456]:
    count+=1
    print(count,number)
print("***End***",count)

total = 0
print("***Start***",total)
for number in [67, 33, 468, 34, 156]:
    total+=number
    print(total,number)
print("***End***",total)

total = 0
count = 0
print("***Start***",total)
for number in [67, 33, 468, 34, 156]:
    total+=number
    count+=1
    print(total,number)
print("***End***",total,count,total/count)

import numpy as np

total = 0
count = 0
#Here None is a flag value
maximum = None
minumum = None
numbers = np.random.randint(-100000,100000, size=4000000)
print("***LETS GO ORIGINAL***")
for number in numbers:
    total+=number
    count+=1
    if maximum is None:
        maximum = number
    elif number>maximum:
        maximum = number
    if minumum is None:
        minumum = number
    elif number<minumum:
        minumum = number

print("Count:",count)
print("Total:",total)
print("Average:",total/count)
print("Max:",maximum)
print("Min:",minumum)
print("***End***")

i=0
positive_count=0
negative_count=0
while i<100:
    total = 0
    count = 0
    maximum = None
    minumum = None
    numbers = np.random.randint(-100000,100000, size=1000000)
    for number in numbers:
        total+=number
        count+=1
        if maximum is None:
            maximum = number
        elif number>maximum:
            maximum = number
        if minumum is None:
            minumum = number
        elif number<minumum:
            minumum = number
    print("*** LETS GO",i,"***")
    print("Total:",total)
    #print("Count:",count)
    #print("Average:",total/count)
    #print("Max:",maximum)
    #print("Min:",minumum)

    if total>=0: positive_count+=1
    else: negative_count+=1
    
    print("***End of",i,"***")
    i+=1

print("positive_count:",positive_count)
print("negative_count:",negative_count)
