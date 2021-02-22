from sys import argv


name, opening_hours, rate, prize = argv
def func_w():
    wages = (int(opening_hours) * int(rate)) + int(prize)
    return wages

func_w()
print(f'Заработная плата равна: {func_w()}')

