with open('text_5.txt', 'w+', encoding='utf-8') as file_5:
    file_5.write('44 21 2 78 339')
    file_5.seek(0)
    num_f = list(file_5.readline().split())
print(sum(map(int, num_f)))
