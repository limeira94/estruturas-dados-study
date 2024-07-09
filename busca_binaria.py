"""
 1 2 3 4 5 6 7 8 9 10
 Primeiro chute 5
 
"""

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    count = 0
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            count += 1
            return meio
        if chute > item:
            alto = meio - 1
            count += 1
        else:
            baixo = meio + 1
            count += 1
    return None

if __name__ == '__main__':
    print(pesquisa_binaria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))