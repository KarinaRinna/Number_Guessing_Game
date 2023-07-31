import random

top_of_range = input("Введите число: ")
# результат "число"

if top_of_range.isdigit():  # Функция String isdigit() в Python возвращает True, если все символы в строке являются цифрами, в противном случае – False.
    top_of_range = int(top_of_range)  # переводим текст "число" в int("число"),
                                      # чтобы было число
    if top_of_range <= 0:   # если было ввведено число то проверяем больше ли оно 0
        print('Введите число больше нуля')
        quit()  # выход из программы
else:
    print('Введите цифру в следующий раз')
    quit()  # выход из программы

random_number = random.randint(11)








# https://www.youtube.com/watch?v=DLn3jOsNRVE&t=3020s