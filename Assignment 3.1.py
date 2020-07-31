str_hours = input("Enter Hours")
str_rate = input("Enter rate per hour")
try:
    hours = float(str_hours)
    rate = float(str_rate)
except:
    print("Error, not a number")
    quit()
    
if hours <= 40.0 :
    pay = hours * rate
else :
    pay = (40.0 * rate) + ((hours-40)*rate*1.5)
print("pay:", pay)