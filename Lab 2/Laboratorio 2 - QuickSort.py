def lomuto(vet, start, end, swaps):   #Particionamento de Lomuto
    pivo = vet[start]
    i = start + 1
    for j in range(start + 1 , end + 1):
        if vet[j] <= pivo:
            swaps[0] += 1
            # troca vet[i] com vet[j]
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux
            i += 1
    
    # Troca vet[i + 1] com o particionador
    aux = vet[i - 1]
    vet[i - 1] = vet[start]
    vet[start] = aux
    return i - 1
