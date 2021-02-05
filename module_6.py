# n = input()
#print(True if n.isdigit() else False)



# goods = []
# features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
# analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
# num = 0
# feature_ = None
# control = None
# while True:
#     control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
#     if control == 'Q':
#         break
#     num += 1
#     if control == 'A':
#         print(f'\n Current analytics \n {"-" * 30}')
#         for key, value in analytics.items():
#             print(f'{key[:25]:>30}: {value}')
#             print("-" * 30)
#     for f in features.keys():
#         feature_ = input(f'Input feature "{f}"')
#         features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
#         analytics[f].append(features[f])
#     goods.append((num, features))
#
# '''
# goods = int(input("Введите количество товара "))
# n = 1
# my_dict = []
# my_list = []
# my_analys = {}
# while n <= goods:
#     my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
#                     'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
#     my_list.append((n, my_dict))
#     n += 1
#     my_analys = dict(
#         {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
#          'ед': my_dict.get('ед')})
# print(my_list)
# print(my_analys)



# goods = []
# features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
# analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
# num = 0
# feature_ = None
# control = None
# while True:
#     control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
#     if control == 'Q':
#         break
#     num += 1
#     if control == 'A':
#         print(f'\n Current analytics \n {"-" * 30}')
#         for key, value in analytics.items():
#             print(f'{key[:25]:>30}: {value}')
#             print("-" * 30)
#     for f in features.keys():
#         feature_ = input(f'Input feature "{f}"')
#         features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
#         analytics[f].append(features[f])
#     goods.append((num, features))
#
# goods = int(input("Введите количество товара "))
# n = 1
# my_dict = []
# my_list = []
# my_analys = {}
# while n <= goods:
#     my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
#                     'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
#     my_list.append((n, my_dict))
#     n += 1
#     my_analys = dict(
#         {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
#          'ед': my_dict.get('ед')})
# print(my_list)
# print(my_analys)
number_goods = int(input('Введите количество товара: '))
goods = []
names = []
prise = []
quantity = []
unit =[]
goods_list = []
analytic_dict = {}
n = 1

while n <= number_goods:
    goods = {'название': input('Введите название: '),'цена': input('Введите цену: '),
                       'количество': input('Введите количество: '), 'ед.изм.': input('Введите единицы измерения: ')}
    goods_list.append((n, goods))
    for i in (goods_list[0])[1]:
        names.append((goods_list[0])[1].get('название'))
        prise.append((goods_list[0])[1].get('цена'))
        quantity.append((goods_list[0])[1].get('количество'))
        unit.append((goods_list[0])[1].get('ед.изм.'))
        analytic_dict = {'Название': names, 'Цена': prise, 'Количество': quantity, 'Ед.изм.': unit}
    n +=1
print(analytic_dict)

