original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
final_list = [x for x in original_list if original_list.count(x) == 1]
print(final_list)
