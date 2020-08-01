def greet(lang):
    if lang == 'es-la':
        return 'Hola'
    elif lang == 'en-us':
        return 'Hello'
    elif lang == 'pt-br':
        return 'Salve'
    else:
        print("We do not speak this language :(")
        exit()

user_lang = input("Enter your language")
user_name = input("Enter your name")

print(greet(user_lang),user_name)

def greet_with_name(lang,name):
    if lang == 'es-la':
        return 'Hola '+name
    elif lang == 'en-us':
        return 'Hello '+name
    elif lang == 'pt-br':
        return 'Salve '+name
    else:
        print("We do not speak this language :(")
        exit()

user_lang = input("Enter your language")
user_name = input("Enter your name")

print(greet_with_name(user_lang,user_name))