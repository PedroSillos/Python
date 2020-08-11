#Write a program to read through the mbox-short.txt and figure out
# the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hour_count = dict()

for line in handle:
    words = line.split()
    try:
        if words[0].upper() == 'FROM':
            hour_min_sec = words[5].split(':')
            hour = hour_min_sec[0]
            hour_count[hour] = hour_count.get(hour,0) + 1
    except:
        continue

sorted_hours = sorted(hour_count.items())
for k,v in sorted_hours:
    print(k,v)