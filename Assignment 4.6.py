def computepay(hours,rate):
    if(hours<=40.0):
        return hours * rate
    else:
        extra = hours - 40.0
        return 40.0 * rate + extra * rate * 1.5

hours_in = input("Enter worked hours")
try:
    hours = float(hours_in)
except:
    print("Number of hours must be in digits")
    quit()

rate_in = input("Enter rate per hour")
try:
    rate = float(rate_in)
except:
    print("Rate per hour must be in digits")
    quit()

pay = computepay(hours,rate)
print("Pay",str(pay))