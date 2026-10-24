#2. Даны два числа. Вывести порядковый номер меньшего из них.

number1 = input("введите первое число")
while type(number1) != int:
    try:
        number1 = int(number1)
    except:
        print("неправильно ввели")
        number1 = input("введите первое число")
number2 = input("введите второе число")
while type(number2) != int:
    try:
        number2 = int(number2)
    except:
        print("неправильно ввели. введите число")
        number2 = input("введите второе число")



if number1 < number2:
    print("меньшее первое число")
elif number2 < number1:
    print("меньшее второе число")
else:
    print("числа равны"

