def int_func(*args):
    text = input("Введите текст через пробел:  ").split()
    for i in range(len(text)):
        new_text = text[i].capitalize()
        print(new_text)
    return

int_func()

