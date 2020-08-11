#tuples are immutable lists - not sortable, no appending, etc

tuply = ('Glenn','Sally',2)
print(tuply)
print(tuply[0])

tuply = ( 3/2, 4/3, 5/4 )
print(max(tuply))

try:
    tuply[0] = 1.5
except:
    print("'tuple' object does not support item assignment")

for item in tuply:
    print(item)

#print( dir() ) #doesnt have to deal with tuples, but I think its nice
print( str( dir(tuply) ) )

(x, y) = ('1','2')
print(x,y)

print( (1,9,9) < (2,0,0) )
print( (9,9,1) == (9,9,1) )
print( (9,9,1) == (9,9,1) )
print( (1,9,9) < (1,9,0) )
print( ('Pepa','Mali') == ('Mali','Pepa') )

dicio = { 'c':3, 'a':1, 'b':2 }
sorty = sorted( dicio.items() )

for k,v in sorty:
    print(k,v)

#sort values instead of keys
dicio = { 'c':3, 'a':1, 'b':2 }
listy = list()
for k,v in dicio.items():
    listy.append( (v,k) )

print('not sorted',listy)
sorty = sorted(listy)
print('asc sorted',sorty)
sorty = sorted(listy, reverse=True)
print('desc sorted',sorty)

#10 most common words in a file:
fhand = open('filename.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

listy = list()
for key, val in counts.items():
    newtuply = (val,key)
    listy.append(newtuply)

listy = sorted(listy, reverse=True)

for val, key in listy[:10]:
    print(key,val)

#really short version of lines 57 to 65
counts = {'banana': 42, 'apple': 23, 'grape': 10000}

print( sorted( [ (v,k) for k,v in counts.items() ] ) )