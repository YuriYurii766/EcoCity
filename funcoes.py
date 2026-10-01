# ==========-----========== (QUESTÃO A) ==========-----==========

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

# ==========-----========== (QUESTÃO B) ==========-----==========

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

# ==========-----=========== NOTIFICAÇÕES DAS ESTAÇÕES (QUESTÃO C) ==========-----==========

def analisar_limites_descarte (lista_descartes, limite_alerta, limite_tolerancia):
    print("\n=== Auditoria de Descartes ===")

    while True:
        try:
            limite_alerta = float(input("Digite o limite de alerta (kg): "))
            limite_tolerancia = float(input("Digite o limite de tolerância operacional (kg): "))
            break
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

    for i in range(len(lista_descartes)):
        quantidade = lista_descartes[i]

        if quantidade >= limite_tolerancia:
            print(f"CRÍTICO: No dia {i + 1}, o descarte de {quantidade}kg excedeu a tolerância operacional de {limite_tolerancia}kg!")
        elif quantidade >= limite_alerta:
            print(f"Alerta: No dia {i + 1}, o descarte de {quantidade}kg excedeu o limite de alerta de {limite_alerta}kg.")

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

def filtrar_estacoes_por_eficiencia(base_dados):
    print("\n=== Filtro de Eficiência das Estações ===")

    while True:
        try:
            criterio_corte = float(input("Digite o critério mínimo de eficiência: "))
            break
        except ValueError:
            print("Digite um valor númerico válido.")

    estacoes_aprovadas = {}

    for codigo, indice in base_dados.items():
        if indice >= criterio_corte:
            estacoes_aprovadas[codigo] = indice

    print("Foram encontradas", len(estacoes_aprovadas), "estações dentro do critério.")

    return estacoes_aprovadas

# ==========-----========== MENU INTERATIVO (QUESTÃO G) ==========-----==========