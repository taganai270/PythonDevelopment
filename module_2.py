list_1 = list(input('Наполните список различными символами: '))
j = 0

for i in range(int(len(list_1)) // 2):
    list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
    j += 2
print(list_1)

