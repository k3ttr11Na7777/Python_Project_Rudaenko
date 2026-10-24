#1. Дано трехзначное число. Проверить истинность высказывания: «Все цифры данного
#числа различны».
while True:
    try:
        number = int(input("Введите техзначное число:"))

        if 100 <= number <= 999:
            break
        else:
            print("Число должно быть техзначным!")
    except ValueError:
        print("не соотв условию введите целое число")

a = number // 100
b = (number // 10) % 10
c = number % 10

if a != b and a != c and b != c:
    print("все числа различны")
else:
    print("не все числа различны")