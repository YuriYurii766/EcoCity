# ==========-----========== (QUESTÃO A) ==========-----==========
estacoes = {}

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
    bairro = input("Digite o bairro da estação: ").strip()

    while bairro == "":
        print("O bairro não pode ficar vazio.")
        bairro = input("Digite o bairro da estação: ").strip()

    while True:
        try:
            volume = float(input("Digite o volume inicial de resíduos (kg): "))
            if volume >= 0:
                break
            else:
                print("O volume não pode ser negativo.")
        except ValueError:
            print("Digite um valor numérico válido.")

    estacoes[codigo] = {
        "bairro": bairro,
        "volume": volume
    }

    print("\n=== Estação cadastrada ===")
    print("Código:", codigo)
    print("Bairro:", bairro)
    print("Volume inicial de resíduos:", format(volume, ".2f"), "kg")

# ==========-----========== (QUESTÃO B) ==========-----==========

CREDITO_POR_KG = 0.05        # créditos de carbono gerados por kg reciclado
LIMITE_MODERADO = 50         # a partir daqui: Sustentabilidade Moderada
LIMITE_AVANCADO = 200        # a partir daqui: Polo Verde Avançado

def calcular_creditos_carbono():
    print("\n=== Cálculo de Créditos de Carbono ===")

    while True:
        try:
            peso = float(input("Digite o peso de material reciclável coletado (kg): "))
            if peso >= 0:
                break
            else:
                print("O peso não pode ser negativo.")
        except ValueError:
            print("Digite um valor numérico válido.")

    creditos = peso * CREDITO_POR_KG

    if creditos < LIMITE_MODERADO:
        categoria = "Baixo Impacto"
    elif creditos < LIMITE_AVANCADO:
        categoria = "Sustentabilidade Moderada"
    else:
        categoria = "Polo Verde Avançado"

    print("Créditos de carbono gerados:", format(creditos, ".2f"))
    print("Classificação:", categoria)



# ==========-----=========== NOTIFICAÇÕES DAS ESTAÇÕES (QUESTÃO C) ==========-----==========

def analisar_limites_descarte():
    print("\n=== Auditoria de Descartes ===")

    while True:
        try:
            limite_alerta = float(input("Digite o limite de alerta (kg): "))
            limite_tolerancia = float(input("Digite o limite de tolerância operacional (kg): "))
            if limite_alerta >= 0 and limite_tolerancia >= limite_alerta:
                break
            else:
                print("Os limites não podem ser negativos e a tolerância deve ser maior ou igual ao alerta.")
        except ValueError:
            print("Digite um valor numérico válido.")

    lista_descartes = []
    print("\n--- Registro dos últimos 10 dias ---")

    for i in range(10):
        while True:
            try:
                quantidade = float(input(f"Digite a quantidade de plástico descartado no dia {i + 1} (kg): "))
                if quantidade >= 0:
                    lista_descartes.append(quantidade)
                    break
                else:
                    print("A quantidade não pode ser negativa.")
            except ValueError:
                print("Digite um valor numérico válido.")

    print("\n--- Resultado da Auditoria ---")

    ocorrencias = 0

    for i in range(len(lista_descartes)):
        quantidade = lista_descartes[i]

        if quantidade > limite_tolerancia:
            print(f"CRÍTICO: No dia {i + 1}, o descarte de {quantidade}kg excedeu a tolerância operacional de {limite_tolerancia}kg!")
            ocorrencias = ocorrencias + 1
        elif quantidade > limite_alerta:
            print(f"Alerta: No dia {i + 1}, o descarte de {quantidade}kg excedeu o limite de alerta de {limite_alerta}kg.")
            ocorrencias = ocorrencias + 1

    if ocorrencias == 0:
        print("Nenhum limite foi excedido nos últimos 10 dias.")

# ==========-----========== (QUESTÃO D) ==========-----==========

def acompanhar_cacambas():
    print("\n=== Acompanhamento das Caçambas Inteligentes ===")

    capacidades = []
    volumes = []
    temperaturas = []

    # pede os dados das 4 caçambas
    for i in range(4):
        print("\nCaçamba", i + 1)

        while True:
            try:
                capacidade = float(input("Capacidade máxima (L): "))
                if capacidade > 0:
                    break
                else:
                    print("A capacidade deve ser maior que zero.")
            except ValueError:
                print("Digite um valor numérico válido.")

        while True:
            try:
                volume = float(input("Volume ocupado (L): "))
                # o volume nao pode passar da capacidade
                if volume >= 0 and volume <= capacidade:
                    break
                else:
                    print("O volume deve estar entre 0 e a capacidade.")
            except ValueError:
                print("Digite um valor numérico válido.")

        while True:
            try:
                temperatura = float(input("Temperatura interna (°C): "))
                break
            except ValueError:
                print("Digite um valor numérico válido.")

        capacidades.append(capacidade)
        volumes.append(volume)
        temperaturas.append(temperatura)

    # relatório
    print("\n=== Relatório Consolidado ===")
    print("Caçamba | Capacidade | Ocupado | Temperatura | Ocupação")

    for i in range(4):
        taxa = volumes[i] / capacidades[i] * 100
        print(i + 1, "|", capacidades[i], "L |", volumes[i], "L |", temperaturas[i], "°C |", format(taxa, ".1f"), "%")
# ==========-----========== (QUESTÃO E) ==========-----==========

def analisar_coleta_mensal(meta):
    print("\n=== Coleta de Lixo Orgânico do Mês ===")
    print("Digite o peso de cada dia (digite -1 para encerrar)")

    pesos = []

    while True:
        try:
            peso = float(input("Peso do dia " + str(len(pesos) + 1) + " (kg): "))
            if peso == -1:
                break
            elif peso >= 0:
                pesos.append(peso)
            else:
                print("O peso não pode ser negativo.")
        except ValueError:
            print("Digite um valor numérico válido.")

    # evita erro de divisão por zero
    if len(pesos) == 0:
        print("Nenhum dado foi informado.")
        return

    maior = pesos[0]
    menor = pesos[0]
    dia_maior = 1
    dia_menor = 1
    soma = 0
    qtd_meta = 0

    for i in range(len(pesos)):
        soma = soma + pesos[i]

        if pesos[i] > maior:
            maior = pesos[i]
            dia_maior = i + 1

        if pesos[i] < menor:
            menor = pesos[i]
            dia_menor = i + 1

        if pesos[i] >= meta:
            qtd_meta = qtd_meta + 1

    media = soma / len(pesos)

    print("\n=== Indicadores ===")
    print("Dia de maior volume: dia", dia_maior, "com", format(maior, ".2f"), "kg")
    print("Dia de menor volume: dia", dia_menor, "com", format(menor, ".2f"), "kg")
    print("Média diária:", format(media, ".2f"), "kg")
    print("Coletas que atingiram a meta de", meta, "kg:", qtd_meta)

# ==========-----========== REGISTROS DE DESEMPENHO DAS ESTAÇÕES (QUESTÃO F) ==========-----==========

def filtrar_estacoes_por_eficiencia(base_dados, criterio_corte):
    estacoes_aprovadas = {}

    for codigo, indice in base_dados.items():
        if indice >= criterio_corte:
            estacoes_aprovadas[codigo] = indice

    return estacoes_aprovadas

# ==========-----========== MENU INTERATIVO (QUESTÃO G) ==========-----==========
# ==========-----========== MENU INTERATIVO (QUESTÃO G) ==========-----==========

def main():
    while True:
        print("\n========== EcoCity ==========")
        print("1 - Cadastrar estação")
        print("2 - Calcular créditos de carbono")
        print("3 - Auditar descartes")
        print("4 - Acompanhar caçambas")
        print("5 - Analisar coleta mensal")
        print("6 - Filtrar estações por eficiência")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_estacao()

        elif opcao == "2":
            calcular_creditos_carbono()

        elif opcao == "3":
            analisar_limites_descarte()

        elif opcao == "4":
            acompanhar_cacambas()

        elif opcao == "5":
            analisar_coleta_mensal(50)

        elif opcao == "6":
            base_dados = {
                1: 80,
                2: 65,
                3: 90,
                4: 40
            }

            criterio_corte = 60

            resultado = filtrar_estacoes_por_eficiencia(
                base_dados,
                criterio_corte
            )

            print("\n=== Estações aprovadas ===")
            print(resultado)

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()