with open('text_1.txt') as file_2:
    lines_f = 0
    list_f = []

    for line in file_2:
        for word in line.split():
            list_f.append(word)
        lines_f += 1

print(f'Количество строк в файле "{file_2.name}" - {lines_f}')
print(f'Количество слов в файле "{file_2.name}" - {len(list_f)}')
