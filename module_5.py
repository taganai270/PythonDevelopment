
def str_num():
    sum_total = 0
    ex = False
    while ex == False:
        number = input('Введите числа через пробел, или "q" - для выхода: ').split()

        n = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                ex = True
                break
            else:
                n = n + int(number[i])
        sum_total = sum_total + n
        print(f'Сумма равна  {sum_total}')
    print(f'Общая сумма равна  {sum_total}')

str_num()























#
#
# print(func_1())




# def convert_item(item: str) -> (int, float):
#     """
#     Преобразование строки в число
#     :param item: строковое представление числа
#     :return: число
#     """
#     try:
#         float_item = float(item)
#         int_item = int(item.split('.')[0])
#     except ValueError:
#         raise
#
#     if float_item == int_item:
#         return int_item
#     else:
#         return float_item
#
#
# if __name__ == '__main__':
#     while stop_index is None:
#         data = input('Пожалуйста введите числа разделённые\n'
#                      'пробелами (допускаются int, float): ').split()
#
#         try:
#             stop_index = data.index('q')
#             data = data[:stop_index]
#         except ValueError:
#             pass
#
#         try:
#             data = [convert_item(i) for i in data]
#         except ValueError:
#             print("Введенные данные содержат неверный тип")
#             continue
#
#         result += my_sum(data)
#
#         print(result)
# def man():
# input_array = list(map(int, input().split()))
# print(input_array, type(input_array))#print(input_array[0] + input_array(len(input_array[-1])))
# # for i in range(1, len(input_array)):
# #     print((input_array[i-1]+input_array[i]))
#            return