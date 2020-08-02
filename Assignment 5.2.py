count = 0
tot=0.0
while True:
    str_in = input("Enter a number:")
    if str_in == 'Done' or str_in == 'done':
        break
    try:
        number = float(str_in)
    except:
        print("Invalid input")
        continue
    count = count + 1
    tot = tot + number
print("Reached 'break'")
try:
    print(tot,count,tot/count)
except:
    print("Cant divide by 0")




count = 0
maximum = None
minimum = None
while True:
    str_in = input("Enter a number:")
    if str_in == 'Done' or str_in == 'done':
        break
    
    try:
        number = int(str_in)
    except:
        print("Invalid input")
        continue

    if maximum is None:
        maximum = number
    elif number>maximum:
        maximum = number
    if minimum is None:
        minimum = number
    elif number<minimum:
        minimum = number

print("Maximum is",maximum)
print("Minimum is",minimum)