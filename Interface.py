from operacoes import somar, dividir, multiplicar, subtrair, fatorial
def interface():
    print("CalcPY".center(40, "-"))
    print("[1] SOMAR")
    print("[2] SUBTRAIR")
    print("[3] MULTIPLICAR")
    print("[4] DIVIDIR")
    print("[5] FATORIAL")
    

    opcao = input("Escolha uma opção!: ")

    if opcao not in {"1", "2", "3", "4", "5"}:
        print("Opção invalida!")
        return
    
    numeros = input("Digite os números separados por espaço: ")

    try:
        if opcao == "5":
            conversor = [int(n) for n in numeros.split()]
        else:
            conversor = [float(n) for n  in numeros.split()]
    except ValueError:
        print("Digite apenas números")
        return

    try:
        if opcao == "1":
            resultado = somar(*conversor)
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            resultado = subtrair(*conversor)
            print(f"Resultado: {resultado}")
        elif opcao == "3":
            resultado = multiplicar(*conversor)
            print(f"Resultado: {resultado}")
        elif opcao == "4":
            resultado = dividir(*conversor)
            print(f"Resultado: {resultado}")
        elif opcao == "5":
            resultado = fatorial(*conversor)
            print("Resultado: ")
            for i, res in zip(conversor, resultado):
                print(f"{i}! = {res}")

    except ValueError as e:
        print(f"Erro: {e}")

    