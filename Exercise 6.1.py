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

str_in = input("Enter a String: ")
print("Here's it backwards:",reverse_str(str_in))
print("Here's the first half:",get_first_half_of_str(str_in))
print("Here's the second half:",get_second_half_of_str(str_in))