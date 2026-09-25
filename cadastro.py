def cadastrar_estacao():
    print("=== Cadastro da Estação Ecológica ===")

    # codigo da estação
    while True:
        try:
            codigo = int(input("Digite o código da estação: "))

            if codigo > 0:
                break
            else:
                print("O código deve ser maior que zero.")

        except ValueError:
            print("Digite um número inteiro válido.")

    # bairro
    bairro = input("Digite o bairro da estação: ")

    while bairro == "":
        print("O bairro não pode ficar vazio.")
        bairro = input("Digite o bairro da estação: ")

    # volume de residuos
    
    while True:
        try:
            volume = float(input("Digite o volume inicial de resíduos (kg): "))

            if volume >= 0:
                break
            else:
                print("O volume não pode ser negativo.")

        except ValueError:
            print("Digite um valor numérico válido.")

    # exibiçaõ dos dados
    print("\n=== Dados da Estação ===")
    print("Código:", codigo)
    print("Bairro:", bairro)
    print("Volume inicial:", format(volume, ".2f"), "kg")


cadastrar_estacao()