# Filta o texto do arquivo 
# Apenas palavras contendo pelo menos 4 caracteres e sem numerais e símbolos
def tratar_texto(texto):
    for i in range(0, len(texto)):
        if len(texto[i]) >= 4:
            if texto[i] >= 'A' and texto[i] <= 'Z':
                texto_correto.append(texto[i])

# Função do RadixSort
# Ordena o vetor de palavras em ordem lexicográfica
def radix_sort(array, i):
    if len(array) <= 1:
        return array

    aux_pronta = []
    # Tabela ASCII: 64 até 90
    aux = [[] for x in range(64, 100)]  

    for s in array:
        if i >= len(s):
            aux_pronta.append(s)
        else:
            aux[ord(s[i]) - ord('a')].append(s)

    aux = [radix_sort(b, i + 1) for b in aux]
    return aux_pronta + [b for blist in aux for b in blist]

# Função contar_e_escrever 
# Conta o número de ocorrências de cada palavra e escreve no arquivo o vetor já ordenado
def contar_e_escrever(texto, nome_arq):
    for i in range(0, len(texto)):
        if i == 0:
            vet_palavra.append(texto[i])
        elif i == len(texto) - 1:
            count = texto.count(texto[i])
            with open(nome_arq, 'a') as arq:
                arq.write(f'{texto[i]} {count}\n')
            vet_palavra.clear()
        else:
            if texto[i] == texto[i + 1]:
                vet_palavra.append(texto[i])
            else:
                with open(nome_arq, 'a') as arq:
                    arq.write(f'{texto[i]} {len(vet_palavra) + 1}\n')
                vet_palavra.clear()

# ---------------------- Main ------------------------
texto_correto = []
vet_palavra = []
# Abre e lê o arquivo inteiro frankestein
with open('frankestein_clean.txt', 'r') as f:
    data = f.readline()
    texto = [str(i) for i in data.split()]
# Filtra o texto
tratar_texto(texto)
# Ordena o texto
texto_ordenado = radix_sort(texto_correto, 0)
# Conta as ocorrências e escreve o texto no arquivo de saída
contar_e_escrever(texto_ordenado, 'frankestein_ordenado.txt')

# Abre e lê o arquivo inteiro war and peace clean
with open('war_and_peace_clean.txt', 'r') as f:
    data = f.readline()
    texto = [str(i) for i in data.split()]
# Filtra o texto
tratar_texto(texto)
# Ordena o texto
texto_ordenado = radix_sort(texto_correto, 0)
# Conta as ocorrências e escreve o texto no arquivo de saída
contar_e_escrever(texto_ordenado, 'war_and_peace_ordenado.txt')