import random
"""
O que falta:
-função de particionador de mediana de 3
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


def part_mediana(array, start, end):
    # Em progresso
    
 
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
def lomuto_partition(array, start, end):     # def lomuto(vet, start, end, swaps):
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

# particionador aleatorio e particionamento de Lomuto
def quick_sort_random_lomuto(array, start, end):
    if start < end:
        part_random(array, start, end)
        pi = lomuto_partition(array, start, end)

        quick_sort_random_lomuto(array, start, pi - 1)
        quick_sort_random_lomuto(array, pi + 1, end)
        
        
#MAIN
array = [10, 25, 69, 10, 7, 86, 124, 168, 984, 102, 1, 0, 754, 235]     #Array de teste
array2 = array.copy()

start = 0
end = len(array) - 1

quick_sort_random_hoare(array, start, end)
print(array)

quick_sort_random_lomuto(array2, start, end)
print(array2)
