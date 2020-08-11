name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    try:
        if words[0] == 'From':
            counts[ words[1] ] = counts.get( words[1] ,0) + 1
    except:
        continue

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)