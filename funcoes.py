# ==========-----========== (QUESTÃO A) ==========-----==========


# ==========-----========== (QUESTÃO B) ==========-----==========


# ==========-----=========== NOTIFICAÇÕES DAS ESTAÇÕES (QUESTÃO C) ==========-----==========
def analisar_limites_descarte (lista_descartes, limite_alerta, limite_tolerancia):
    for i in range(len(lista_descartes)):
        quantidade = lista_descartes[i]

        if quantidade > limite_tolerancia:
            print(f"Alerta! No dia {i + 1}, o descarte de {quantidade}kg excedeu a tolerância operacional de {limite_tolerancia}kg!")

# ==========-----========== (QUESTÃO D) ==========-----==========

# ==========-----========== (QUESTÃO E) ==========-----==========


# ==========-----========== REGISTROS DE DESEMPENHO DAS ESTAÇÕES (QUESTÃO F) ==========-----==========
def filtrar_estacoes_por_eficiencia(base_dados, criterio_corte):
    estacoes_aprovadas = {}

    for codigo, indice in base_dados.items():
        if indice >= criterio_corte:
            estacoes_aprovadas[codigo] = indice

    return estacoes_aprovadas

# ==========-----========== MENU INTERATIVO (QUESTÃO G) ==========-----==========