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
array = [10, 25, 69, 10, 7, 86, 50, 168, 984, 102, 1, 0, 754, 235]  # Array de teste
array2 = array.copy()
array3 = array.copy()
array4 = array.copy()

start = 0
end = len(array) - 1

print("Random Hoare")
quick_sort_random_hoare(array, start, end)
print(array)

print("Part3 Hoare")
quick_sort_part3_hoare(array2, start, end)
print(array2)

print("Random Lomuto")
quick_sort_random_lomuto(array3, start, end)
print(array3)

print("Part3 Lomuto")
quick_sort_random_lomuto(array4, start, end)
print(array4)
