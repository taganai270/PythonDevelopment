
with open('text_4.txt',) as file_4:
    trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    my_file = []
    for el in file_4:
       el = el.split(' ', 1)
       my_file.append(trans[el[0]] + ' ' + el[1])
    print(my_file)
with open('text_4_1.txt', 'w', encoding='utf-8') as file_4_1:
    file_4_1.writelines(my_file)
