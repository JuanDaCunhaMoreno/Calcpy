#Algumas opreções

def somar(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total


def subtracao(*numeros):
    if not numeros:
        return 0
    total = numeros[0]
    for n in numeros[1:]:
        total -= n
    return total


def multiplicar(*numeros):
    total = 1
    for n in numeros:
        total *= n
    return total


def dividir(*numeros):
    if not numeros:
        return None
    total = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            raise ValueError("Divisão por zero não é permitida!")
        total /= n
    return total
        