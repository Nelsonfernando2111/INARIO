import heapq

# --- Funções auxiliares ---
def teste_objetivo(estado, objetivo):
    return estado == objetivo

def sucessores(estado):
    suc = []
    pos = estado.index(0)
    linha, coluna = divmod(pos, 3)
    movimentos = [
        ('cima', -1, 0),
        ('baixo', 1, 0),
        ('esquerda', 0, -1),
        ('direita', 0, 1)
    ]
    for acao, dl, dc in movimentos:
        nova_linha = linha + dl
        nova_coluna = coluna + dc
        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            nova_pos = nova_linha*3 + nova_coluna
            novo_estado = estado.copy()
            novo_estado[pos], novo_estado[nova_pos] = novo_estado[nova_pos], novo_estado[pos]
            suc.append((acao, novo_estado, 1))  # custo de 1 por movimento
    return suc

def heuristica(estado, objetivo):
    distancia = 0
    for i, valor in enumerate(estado):
        if valor != 0:
            pos_objetivo = objetivo.index(valor)
            linha_atual, col_atual = divmod(i, 3)
            linha_obj, col_obj = divmod(pos_objetivo, 3)
            distancia += abs(linha_atual - linha_obj) + abs(col_atual - col_obj)
    return distancia

# --- A* ---
def a_estrela(estado_inicial, objetivo):
    heap = [(heuristica(estado_inicial, objetivo), 0, estado_inicial, [])]  # (f, g, estado, caminho)
    visitados = set()

    while heap:
        f, g, estado, caminho = heapq.heappop(heap)
        estado_tuple = tuple(estado)
        if estado_tuple in visitados:
            continue
        visitados.add(estado_tuple)

        if teste_objetivo(estado, objetivo):
            return caminho, g  # retorna também o custo

        for acao, novo_estado, custo in sucessores(estado):
            if tuple(novo_estado) not in visitados:
                novo_g = g + custo
                novo_f = novo_g + heuristica(novo_estado, objetivo)
                heapq.heappush(heap, (novo_f, novo_g, novo_estado, caminho + [acao]))

    return None, None

# --- Mostrar tabuleiro ---
def mostrar_tabuleiro(estado):
    for i in range(0, 9, 3):
        print(estado[i:i+3])
    print()

# --- Jogar ---
def main():
    print("Digite o estado inicial (0 representa o espaço vazio):")
    entrada = input("Exemplo: 1 2 3 4 0 5 6 7 8\n")
    estado_inicial = [int(x) for x in entrada.split()]

    print("\nDigite o estado final desejado (ou pressione Enter para usar o padrão 1 2 3 4 5 6 7 8 0):")
    entrada_final = input()
    if entrada_final.strip() == "":
        objetivo = [1,2,3,4,5,6,7,8,0]
    else:
        objetivo = [int(x) for x in entrada_final.split()]

    # validação
    if len(estado_inicial) != 9 or 0 not in estado_inicial:
        print("Entrada inválida! Digite 9 números de 0 a 8, incluindo o 0.")
        return
    if len(objetivo) != 9 or 0 not in objetivo:
        print("Objetivo inválido! Digite 9 números de 0 a 8, incluindo o 0.")
        return

    print("\nCalculando solução com A*...")
    caminho, custo = a_estrela(estado_inicial, objetivo)

    if caminho:
        print(f"Solução encontrada em {len(caminho)} movimentos (custo total = {custo}):")
        print(" -> ".join(caminho))

        # Mostrar passo a passo
        print("\nResolução passo a passo:")
        estado = estado_inicial[:]
        mostrar_tabuleiro(estado)
        for acao in caminho:
            for a, novo_estado, _ in sucessores(estado):
                if a == acao:
                    estado = novo_estado
                    break
            print(f"Movimento: {acao}")
            mostrar_tabuleiro(estado)
    else:
        print("Não foi possível encontrar solução.")

if __name__ == "__main__":
    main()
