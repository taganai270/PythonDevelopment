goods = []
goods_list = []
analytic_dict = {}
n = 1
number_goods = int(input('Введите количество товара: '))
while n <= number_goods:
    goods = {'название': input('Введите название: '),'цена': input('Введите цену: '),
                       'количество': input('Введите количество: '), 'ед.изм.': input('Введите единицы измерения: ')}

    goods_list.append((n, goods))
    n += 1
print(f'\n{goods_list}')
analytic_dict = {'название': [], 'цена': [], 'количество': [], 'ед.изм.': []}
for lst in goods_list:
    analytic_dict['название'].append(lst[1]['название'])
    analytic_dict['цена'].append(lst[1]['цена'])
    analytic_dict['количество'].append(lst[1]['количество'])
    analytic_dict['ед.изм.'].append(lst[1]['ед.изм.'])
print(f'\n{analytic_dict}')


