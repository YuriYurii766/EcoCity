def cadastrar_estacao():
    print("=== Cadastro da Estação Ecológica ===")

    # codigo da estação
    while True:
        try:
            codigo = int(input("Digite o código da estação: "))

            # o código tem que ser positivo

            if codigo > 0:
                break
            else:
                print("O código deve ser maior que zero.")

        # se digitar texto, evita erro
        except ValueError:
            print("Digite um número inteiro válido.")

    # bairro
    bairro = input("Digite o bairro da estação: ")

    # não permite deixar o bairro vazio
    while bairro == "":
        print("O bairro não pode ficar vazio.")
        bairro = input("Digite o bairro da estação: ")

    # volume de resíduos
    
    while True:
        try:
            volume = float(input("Digite o volume inicial de resíduos (kg): "))

            # volume pode ser zero mas nao pode ser negativo
            if volume >= 0:
                break
            else:
                print("O volume não pode ser negativo.")

        # evita erro se digitar algo que nao seja número
        except ValueError:
            print("Digite um valor numérico válido.")

    # exibição dos dados
    print("\n=== Dados da Estação ===")
    print("Código:", codigo)
    print("Bairro:", bairro)
    print("Volume inicial:", format(volume, ".2f"), "kg")

cadastrar_estacao()