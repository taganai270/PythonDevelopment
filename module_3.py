
with open('text_3.txt', 'r', encoding='utf-8') as file_3:
    emp = []
    wage = []
    list_f = file_3.read().split('\n')
    for en in list_f:
        en = en.split()
        if float(en[1]) < 20000:
            emp.append(en[0])
        wage.append(en[1])
    print(f'Оклад меньше 20000 у сотрудников -  {emp}, средний оклад {sum(map(float, wage)) / len(wage)}')



