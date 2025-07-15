from operacoes import somar, dividir, multiplicar, subtrair
def interface():
    print("CalcPY".center(40, "-"))
    print("[1] SOMAR")
    print("[2] SUBTRAIR")
    print("[3] MULTIPLICAR")
    print("[4] DIVIDIR")
    

    opcao = input("Escolha uma opção!: ")

    if opcao not in {"1", "2", "3", "4"}:
        print("Opção invalida!")
        return
    
    numeros = input("Digite os números separados por espaço: ")

    try:
        conversor = [float(n) for n  in numeros.split()]
    except ValueError:
        print("Digite apenas números")
        return

    try:
        if opcao == "1":
            resultado = somar(*conversor)
        elif opcao == "2":
            resultado = subtrair(*conversor)
        elif opcao == "3":
            resultado = multiplicar(*conversor)
        elif opcao == "4":
            resultado = dividir(*conversor)

        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")

    