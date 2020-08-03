def print_str(string_in):
    for letter in string_in:
        print(letter, end = '')

def reverse_str(string_in):
    i = len(string_in)-1
    reverse_string = [None] * len(string_in)
    for letter in string_in:
        reverse_string[i] = letter
        i = i-1
    return ''.join(reverse_string)
    
def get_first_half_of_str(string_in):
    return string_in[ 0 : int( len(string_in)/2 ) ]

def get_second_half_of_str(string_in):
    return string_in[ int( len(string_in)/2 ) : int(len(string_in)) ]

def search_in_str(searcher,searched):
    if searcher in searched: return "Found"
    else: return "Not found"

def find_in_str(finder,finded):
    return finded.find(finder)

str_in = input("Enter a String: ")
print("Here's it backwards:",reverse_str(str_in))
print("Here's the first half:",get_first_half_of_str(str_in))
print("Here's the second half:",get_second_half_of_str(str_in))
print("Here's it with only lowercases:",str_in.lower())
print("Here's it with only uppercases:",str_in.upper())
print("Here's it with no spaces in the right:",str_in.rstrip())
print("Here's it with no spaces in the left:",str_in.lstrip())
print("Here's it with no spaces in the borders:",str_in.strip())
print("Here's its type:",str(type(str_in)))
#print("Here are its methods:",str(dir(str_in)))
print(search_in_str(input("Type something to be searched inside string: "),str_in))
print("Found at position:",find_in_str(input("Type something to be found inside string: "),str_in))