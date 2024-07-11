
def busca_menor(arr):
    menor_valor = arr[0]
    menor_index = 0
    for i in range(1, len(arr)):
        if arr[i] < menor_valor:
            menor_valor = arr[i]
            menor_index = i
    return menor_index


def ordenacao_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr
    