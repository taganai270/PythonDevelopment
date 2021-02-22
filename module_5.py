from functools import reduce
num_list = [x for x in range(100, 1001) if x % 2 == 0]
sum_list = reduce(lambda x, y: x + y, num_list)
print(sum_list)