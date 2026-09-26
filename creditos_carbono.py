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

    # calcula os créditos com base no peso coletado
    creditos = peso * 0.5

    # classifica de acordo com a quantidade de créditos
    if creditos < 50:
        categoria = "Baixo Impacto"
    elif creditos < 150:
        categoria = "Sustentabilidade Moderada"
    else:
        categoria = "Polo Verde Avançado"

    print("\n=== Resultado ===")
    print("Peso coletado:", format(peso, ".2f"), "kg")
    print("Créditos de carbono:", format(creditos, ".2f"))
    print("Classificação:", categoria)

calcular_creditos_carbono()