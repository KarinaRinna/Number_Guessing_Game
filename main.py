import random

top_of_range = input("Введите число: ")
# результат "число"

if top_of_range.isdigit():  # Функция String isdigit() в Python возвращает True, если все символы в строке являются цифрами, в противном случае – False.
    top_of_range = int(top_of_range)  # переводим текст "число" в int("число"),
                                      # чтобы было число
    if top_of_range <= 0:   # если было ввведено число то проверяем больше ли оно 0
        print('Введите число больше нуля')
        quit()  # выход из программы
else:  # если же было введено не число
    print('Введите цифру в следующий раз')
    quit()  # выход из программы

random_number = random.randint(0, top_of_range) # диапозон от 0 до числа которое названо
guesses = 0         # попытки угадать число

while True:
    guesses += 1
    user_guess = input('сделать предположение: ')
    if user_guess.isdigit():  # Функция String isdigit() в Python возвращает True, если все символы в строке являются цифрами, в противном случае – False.
        user_guess = int(user_guess)  # переводим текст "число" в int("число"),
                                      # чтобы было число
    else:           # если же было введено не число
        print('Введите цифру в следующий раз')
        continue    # возврат к началу цикла

    if user_guess == random_number:
        print('Ты угадал!!!')
        break       # если угадал то останавливаем цикл
    else:
        if user_guess > random_number:
            print('Число меньше')
        else:
            print('Число больше')


print('У тебя получилось, ты угадал с', guesses, 'раз')







# https://www.youtube.com/watch?v=DLn3jOsNRVE&t=3020s
# 33:10