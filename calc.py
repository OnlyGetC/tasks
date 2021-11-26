calc = input("Введите числа через пробел ")
while calc.count(" ") == 2:
    x, operand, y = calc.split(" ")
    x = int(x)
    y = int(y)
    if operand == "+":
        print("Ответ: " + str(x + y))
    elif operand == "-":
        print("Ответ: " + str(x - y))
    elif operand == "*":
        print("Ответ: " + str(x * y))
    elif operand == "/":
        print("Ответ: " + str(x / y))
    else:
        print("Введена неизвестная операция")
    calc = input()