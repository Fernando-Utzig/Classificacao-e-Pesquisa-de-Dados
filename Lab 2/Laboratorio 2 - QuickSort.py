import random
import statistics

"""
O que falta:
-contar swaps
-contar recursoes
-cronometrar o tempo
-ler arquivos de entrada
-escrever em arquivos de saída
"""

# Escolhe um particionador randomizado  (funcionando)
def part_random(array, start, end):
    n = random.randint(start, end)
    aux = array[start]
    array[start] = array[n]
    array[n] = aux


# Escolhe a mediana entre o primeiro, ultimo e valor do meio para particionador (funcionando)
def part_mediana(array, start, end):
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


# Particionamento de Hoare  (funcionando)
def hoare_partition(array, start, end):
    pivot = array[start]
    i = start - 1
    j = end + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]


# Particionamento de Lomuto  (funcionando)
def lomuto_partition(array, start, end):  # def lomuto(vet, start, end, swaps):
    pivo = array[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if array[j] <= pivo:
            # swaps[0] += 1
            # troca vet[i] com vet[j]
            aux = array[i]
            array[i] = array[j]
            array[j] = aux
            i += 1

    aux = array[i - 1]
    array[i - 1] = array[start]
    array[start] = aux
    return i - 1


# particionador aleatorio e particionamento de Hoare
def quick_sort_random_hoare(array, start, end):
    if start < end:
        part_random(array, start, end)
        pi = hoare_partition(array, start, end)

        quick_sort_random_hoare(array, start, pi)
        quick_sort_random_hoare(array, pi + 1, end)


# particionador mediana de 3 e particionamento de Hoare
def quick_sort_part3_hoare(array, start, end):
    if start < end:
        part_mediana(array, start, end)
        pi = hoare_partition(array, start, end)

        quick_sort_random_hoare(array, start, pi)
        quick_sort_random_hoare(array, pi + 1, end)


# particionador aleatorio e particionamento de Lomuto
def quick_sort_random_lomuto(array, start, end):
    if start < end:
        part_random(array, start, end)
        pi = lomuto_partition(array, start, end)

        quick_sort_random_lomuto(array, start, pi - 1)
        quick_sort_random_lomuto(array, pi + 1, end)


# particionador mediana de 3 e particionamento de Lomuto
def quick_sort_part3_lomuto(array, start, end):
    if start < end:
        part_mediana(array, start, end)
        pi = lomuto_partition(array, start, end)

        quick_sort_random_lomuto(array, start, pi - 1)
        quick_sort_random_lomuto(array, pi + 1, end)


# MAIN
# MAIN

tam = [100, 1000, 10000, 100000, 1000000]  # tamanhos dos vetores

with open('entrada2.txt', 'r') as f:
    for k in range(5):
        data = f.readline()
        array = [int(i) for i in data.split()]

        del array[0]

        start = 0
        end = len(array) - 1

        array2 = array.copy()
        array3 = array.copy()
        array4 = array.copy()

        inicio = time.time()
        quick_sort_part3_hoare(array, start, end)
        fim = time.time()
        tempo = fim - inicio
        with open('stats-mediana-hoare.txt', 'a') as arq:
            arq.write(f'TAMANHO ENTRADA {tam[k]}\n')
            arq.write(f'TEMPO {tempo} EM SEGUNDOS\n')

        inicio = time.time()
        quick_sort_part3_lomuto(array2, start, end)
        fim = time.time()
        tempo = fim - inicio
        with open('stats-mediana-lomuto.txt', 'a') as arq:
            arq.write(f'TAMANHO ENTRADA {tam[k]}\n')
            arq.write(f'TEMPO {tempo} EM SEGUNDOS\n')

        inicio = time.time()
        quick_sort_random_hoare(array3, start, end)
        fim = time.time()
        tempo = fim - inicio
        with open('stats-aleatorio-hoare.txt', 'a') as arq:
            arq.write(f'TAMANHO ENTRADA {tam[k]}\n')
            arq.write(f'TEMPO {tempo} EM SEGUNDOS\n')

        inicio = time.time()
        quick_sort_random_lomuto(array4, start, end)
        fim = time.time()
        tempo = fim - inicio
        with open('stats-aleatorio-lomuto.txt', 'a') as arq:
            arq.write(f'TAMANHO ENTRADA {tam[k]}\n')
            arq.write(f'TEMPO {tempo} EM SEGUNDOS\n')

