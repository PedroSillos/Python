def Count_words_in_input(line):
    counts = dict()
    words = line.split()
    print('Words:',words)

    for word in words:
        counts[word] = counts.get(word,0) + 1
    print('Counts',counts)

def Print_dictionary(dictionary):
    for key in dictionary:
        print(key, dictionary)

dicio = { 'chuck': 1, 'fred': 42, 'jan': 100 }

print( list(dicio) ) #['chuck', 'fred', 'jan']
print( list(dicio.keys() ) ) #['chuck', 'fred', 'jan']
print( list(dicio.values() ) ) #[1, 42, 100]
print( list(dicio.items() ) ) #[('chuck', 1), ('fred', 42), ('jan', 100)]

#Python3 allows 2 iteration variables
dicio = { 'chuck': 1, 'fred': 42, 'jan': 100 }
for key,value in dicio.items():
    print('key:',key,',','value:',value)



file_name = input('Enter file name:')
handle = open(file_name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
