# ==========-----========== (QUESTÃO A) ==========-----==========


# ==========-----========== (QUESTÃO B) ==========-----==========


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


# ==========-----========== (QUESTÃO E) ==========-----==========


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