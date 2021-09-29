import random
import statistics
import time


# Escolhe um particionador randomizado
def part_random(array, start, end):
    n = random.randint(start, end)
    aux = array[start]
    array[start] = array[n]
    array[n] = aux

# Escolhe a mediana entre o primeiro, último e valor do meio para usar como particionador
def mediana_de_tres(array, start, end):
    meio = end // 2
    vetor_teste = [array[start], array[meio], array[end]]
    if statistics.median(vetor_teste) == array[meio]:
        aux = array[start]
        array[start] = array[meio]
        array[meio] = aux
    elif statistics.median(vetor_teste) == array[end]:
        aux = array[start]
        array[start] = array[end]
        array[end] = aux


# Particionamento de Hoare
def hoare_partition(array, start, end, swaps):
    pivot = array[start]
    i = start - 1
    j = end + 1
    while True:
        swaps[0] += 1
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


# Particionamento de Lomuto
def lomuto_partition(array, start, end, swaps):  # def lomuto(vet, start, end, swaps):
    pivo = array[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if array[j] <= pivo:
            swaps[0] += 1
            # troca vet[i] com vet[j]
            aux = array[i]
            array[i] = array[j]
            array[j] = aux
            i += 1
    aux = array[i - 1]
    array[i - 1] = array[start]
    array[start] = aux
    return i - 1


# Particionador aleatório
# Particionamento de Hoare
def quick_sort_random_hoare(array, start, end, recursao, swaps):
    if start < end:
        recursao[0] += 1
        # Particionador
        part_random(array, start, end)
        # Particionamento
        pi = hoare_partition(array, start, end, swaps)
        quick_sort_random_hoare(array, start, pi, recursao, swaps)
        quick_sort_random_hoare(array, pi + 1, end, recursao, swaps)


# Particionador mediana de 3
# Particionamento de Hoare
def quick_sort_med3hoare(array, start, end, recursao, swaps):
    if start < end:
        recursao[0] += 1
        # Particionador
        mediana_de_tres(array, start, end)
        # Particionamento
        pi = hoare_partition(array, start, end, swaps)
        quick_sort_med3hoare(array, start, pi, recursao, swaps)
        quick_sort_med3hoare(array, pi + 1, end, recursao, swaps)


# Particionador aleatório
# Particionamento de Lomuto
def quick_sort_random_lomuto(array, start, end, recursao, swaps):
    if start < end:
        recursao[0] += 1
        # Particionador
        part_random(array, start, end)
        # Particionamento
        pi = lomuto_partition(array, start, end, swaps)

        quick_sort_random_lomuto(array, start, pi - 1, recursao, swaps)
        quick_sort_random_lomuto(array, pi + 1, end, recursao, swaps)


# Particionador Mediana de 3
# Particionamento de Lomuto
def quick_sort_med3lomuto(array, start, end, recursao, swaps):
    if start < end:
        recursao[0] += 1
        # Particionador
        mediana_de_tres(array, start, end)
        # Particionamento
        pi = lomuto_partition(array, start, end, swaps)

        quick_sort_med3lomuto(array, start, pi - 1, recursao, swaps)
        quick_sort_med3lomuto(array, pi + 1, end, recursao, swaps)


# MAIN
tam = [100, 1000, 10000, 100000, 1000000]  # Tamanhos dos vetores
recursao = [-1] # Variavel que conta as recursoes
swaps = [0] # Variavel que conta os swaps

with open('entrada-quicksort.txt', 'r') as f:
    for k in range(5):
        # Lê a primeira linha do vetor
        data = f.readline()
        array = [int(i) for i in data.split()]

        # Deleta o primeiro número da linha (tamanho do vetor)
        del array[0]
        # Inicializa as variáveis start e end (inicio e final do vetor)
        start = 0
        end = len(array) - 1

        # Copia o vetor 3 vezes para usar nas 4 saídas
        array2 = array.copy()
        array3 = array.copy()
        array4 = array.copy()

        recursao[0] = -1
        swaps[0] = 0

        inicio = time.time()
        # Chamada da função do Quicksort particionador Mediana de 3 com particionamento Hoare
        quick_sort_med3hoare(array, start, end, recursao, swaps)
        fim = time.time()
        # Variável que guarda o tempo que a função levou para executar
        tempo = fim - inicio
        # Guarda no arquivo
        with open('stats-mediana-hoare.txt', 'a') as arq:
            arq.write(f'TAMANHO ENTRADA {tam[k]}\n')
            arq.write(f'SWAPS {swaps[0]}\n')
            arq.write(f'RECURSOES {recursao[0]}\n')
            arq.write(f'TEMPO {tempo} EM SEGUNDOS\n')

        recursao[0] = -1
        swaps[0] = 0

        inicio = time.time()
        # Chamada da função do Quicksort particionador Mediana de 3 com particionamento Lomuto
        quick_sort_med3lomuto(array2, start, end, recursao, swaps)
        fim = time.time()

        tempo = fim - inicio
        with open('stats-mediana-lomuto.txt', 'a') as arq:
            arq.write(f'TAMANHO ENTRADA {tam[k]}\n')
            arq.write(f'SWAPS {swaps[0]}\n')
            arq.write(f'RECURSOES {recursao[0]}\n')
            arq.write(f'TEMPO {tempo} EM SEGUNDOS\n')

        recursao[0] = -1
        swaps[0] = 0

        inicio = time.time()
        # Chamada da função do Quicksort particionador Aleatório com particionamento Hoare
        quick_sort_random_hoare(array3, start, end, recursao, swaps)
        fim = time.time()

        tempo = fim - inicio
        with open('stats-aleatorio-hoare.txt', 'a') as arq:
            arq.write(f'TAMANHO ENTRADA {tam[k]}\n')
            arq.write(f'SWAPS {swaps[0]}\n')
            arq.write(f'RECURSOES {recursao[0]}\n')
            arq.write(f'TEMPO {tempo} EM SEGUNDOS\n')

        recursao[0] = -1
        swaps[0] = 0

        inicio = time.time()
        # Chamada da função do Quicksort particionador Aleatório com particionamento Lomuto
        quick_sort_random_lomuto(array4, start, end, recursao, swaps)
        fim = time.time()

        tempo = fim - inicio
        with open('stats-aleatorio-lomuto.txt', 'a') as arq:
            arq.write(f'TAMANHO ENTRADA {tam[k]}\n')
            arq.write(f'SWAPS {swaps[0]}\n')
            arq.write(f'RECURSOES {recursao[0]}\n')
            arq.write(f'TEMPO {tempo} EM SEGUNDOS\n')
