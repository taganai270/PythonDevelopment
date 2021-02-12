lst_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
if lst_1[0] > lst_1[1]:
    lst_1.remove(lst_1[0])
new_list = [x for i, x in enumerate(lst_1) if lst_1[i-1] < lst_1[i]]
print(new_list)