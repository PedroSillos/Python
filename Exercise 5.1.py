#i is the iteration variable
i = 5
while i >= 0 :
    print(i)
    i = i - 0.5
print("While became false")

i = 1
while i > 0 :
    print(i)
    if i == 3:
        break
    i = i+1
print("Reached break")

#for each
for palavra in ["Máquina","de","Sexo","eu","transo","igual","animal"]:
    print(palavra)

print("while True:")
while True :
    i = input("Type something")
    if i == 'quit()' or i == 'exit()' or i == 'leave()' or i == 'close()':
        print('bye')
        break
    if i[0] == '#':
        continue
    else:
        print(i)