from Interface import interface

def main():
    while True:
        interface()
        continuar = input("Quer fazer outra operação? [S/N] ").strip().upper()
        if continuar != "S":
            print("Obrigado por usar o CalcPY")
            break


if __name__ == "__main__":
    main()