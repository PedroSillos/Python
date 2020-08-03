def read_file_a(file_addres):
    try:
        #file handles are sequences of lines
        a_file_handle = open(file_addres)
    except:
        return 'Error 0: File not found'
    
    #"return a_file_handle.read()" could replace the next 4 lines
    file_text = ''
    for line in a_file_handle:
        file_text = file_text + line
    return file_text

print(read_file_a('c:/Users/psillosx/OneDrive - Intel Corporation/Desktop/Python/sometext.txt'))

a_file_handle = open('c:/Users/psillosx/OneDrive - Intel Corporation/Desktop/Python/sometext.txt')
for line in a_file_handle:
    line = line.rstrip()
    print(line)