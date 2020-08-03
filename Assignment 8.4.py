#8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
try:
    line_list = open(fname)
except:
    print("File not found")
    exit()

final_list = list()
for line in line_list:
    word_list = line.rstrip().split()
    for word in word_list:
        if word not in final_list:
            final_list.append(word)
final_list.sort()
print(final_list)