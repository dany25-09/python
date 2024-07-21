def decimalToBin(number_decimal):
    number_binary = 0
    multiplier = 1
    while number_decimal != 0:
        # se almacena el módulo en el orden correcto
        number_binary = number_binary + number_decimal % 2 * multiplier
        number_decimal //= 2
        multiplier*= 10
    return str(number_binary)



def shapeType(n):
    if n == 3: 
        return "triángulo"
    elif n == 4:
        return "cuadrilatero"
    elif n == 5:
        return "pentágono"
    elif n == 6:
        return "Hexágono"
    elif n == 7:
        return "heptágono"
    elif n == 8:
        return "octágono"
    elif n == 9:
        return "eneágono"
    elif n == 10:
        return "decágono"
        


def tiketsCost(age):
    list = [0]
    for i in age:
        if (i <= 2):
            continue

        elif (i < 13):
            list.append(14000)
            continue

        elif (i <= 61):
            list.append(25000)
            continue

        else:
            list.append(18000)
            continue

    for i in list:
        total = i

    return total


print((decimalToBin(4)))
print((decimalToBin(12)))
print((decimalToBin(22301)))

print(shapeType(3))
print(shapeType(8))
print(shapeType(10))

print(tiketsCost([2, 4, 5]))
print(tiketsCost([15, 60, 65]))
print(tiketsCost([22, 43, 55]))