num_list = [7, 5, 4, 4, 2]
n = int(input('Введи номер рейтинга: '))
print('\nСписок рейтенгов ', num_list)

for i in range(len(num_list)):
    if num_list[-1] > n:
        num_list.append(n)
    elif num_list[0] < n:
        num_list.insert(0, n)
    elif num_list[i] > n and num_list[i+1] < n:
        num_list.insert(i+1, n)
    elif num_list[i] == n:
        num_list.insert(i + 1, n)
        break
print('Новый список рейтенгов ', num_list)
