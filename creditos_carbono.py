def calcular_creditos_carbono():
    print("\n=== Cálculo de Créditos de Carbono ===")

    # peso material reciclável
    while True:
        try:
            peso = float(input("Digite o peso de material reciclável coletado (kg): "))

            # aceita zero ou valores positivos
            if peso >= 0:
                break
            else:
                print("O peso não pode ser negativo.")

        # evita caso seja digitado texto
        except ValueError:
            print("Digite um valor numérico válido.")