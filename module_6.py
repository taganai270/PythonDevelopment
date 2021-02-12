
import itertools
#
# #а) итератор, генерирующий целые числа, начиная с указанного
# num = int(input('Первое число в списке: '))
# for x in itertools.count(num):
#     if x > num * 10:
#         break
#     else:
#         print(x)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее
l1 = ['***\n___']
l2 = itertools.cycle(l1)
count = 0

for i in l2:
    if count > 10:
        break
    else:
        print (i)
        count += 1


