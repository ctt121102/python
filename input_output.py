with open('input.inp', 'r', encoding='utf8') as Fileinp:
    data = Fileinp.readlines()
    print(data)
    string = ' '.join(data).replace('\n', '')

    list = string.split()
    string = ' '.join(list)
print(string)
Fileout = open('output.out', 'wb')
Fileout.write(string.encode('utf8'))

