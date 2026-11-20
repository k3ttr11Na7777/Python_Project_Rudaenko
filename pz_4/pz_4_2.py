# Дано целое число N (>0). Если оно является степенью числа 3,
# то вывести TRUE, если не является вывести FALSE

n = input("Введите число: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")

while n > 1 and n % 3 == 0:
    n //= 3 #jjj

if n == 1:
    print("TRUE")
else:
    print("FALSE")
