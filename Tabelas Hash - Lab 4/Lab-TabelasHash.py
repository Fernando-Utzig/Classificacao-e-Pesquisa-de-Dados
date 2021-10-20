# Função de hash polinomial
def polinomial_hash(word, M):
    p = 31                                          # Primeiro número primo > 26
    hash = 0
    for i in word:
        if (i != '\n') and (i != ' '):              # Tranforma as letras em int e soma elas
            num = ord(i)
            hash = (p * hash + num) % M             # Calculo polinomial
    return hash


# Função que consulta os nomes
def consulta(arr, word, M):
    hash = polinomial_hash(word, M)                 # Calcula o hash para saber onde consultar
    if arr[hash] != []:                             # Checa se não tem um array vazio
        if word == arr[hash][0]:                    # Se o nome estiver na primeira posição retorna 1,
            return 1                                # pois foi o 1º a ser inserido
        else:
            for x in range(0, len(arr[hash])):      # Procura no restante do array um nome igual
                if word == arr[hash][x]:
                    return x + 1                    # Retorna o número de vezes que teve que andar para encontrar
            return len(arr[hash]) + 1               # Se não encontrou retorna o número máximo de colisões
    else:
        return len(arr[hash]) + 1

# ----------- MAIN ----------- 

M = [503, 2503, 5003, 7507]                         # Tamanhos das tabelas Hash
vet_colisoes = []
soma = 0
maior_colisao = 0

f = open('nomes_10000.txt', 'r')                    # Coloca os 10 mil nomes em nomes
nomes = f.readlines()

f = open('consultas.txt', 'r')                      # Coloca os nomes da consulta em nomes_consulta
nomes_consultas = f.readlines()

for i in range(0, 4):
    vet = [[] for _ in range(0, M[i])]              # Declara o vetor hash com o tamanho M
    for j in range(0, 10000):
        hash = polinomial_hash(nomes[j], M[i])      # Calcula o valor da posição que o nome tem que estar na tabela hash
        vet[hash].append(nomes[j])                  # Insere o nome da sua posição

    nome_arq = 'experimento' + str(M[i]) + '.txt'                         # Define o nome do arquivo a ser gerado

    for k in range(0, 50):
        aux = consulta(vet, nomes_consultas[k], M[i])                     # Chamada da função de consulta

        tam_palavra = len(nomes_consultas[k])
        vet_colisoes.append(aux)
            
        if k == 49:
            for m in range(0, 50):                  
                soma = soma + vet_colisoes[m]
            media = soma / 50

        if k == 1:
            maior_colisao = aux
        elif aux > maior_colisao:
            maior_colisao = aux

        
        with open(nome_arq, 'a') as arq:
            arq.write(f'{nomes_consultas[k][0:tam_palavra-1]} {aux}\n')     # Retira o "\n" para escrever no arquivo
        
    with open(nome_arq, 'a') as arq:    
        arq.write(f'MEDIA {media}\n')
    with open(nome_arq, 'a') as arq:    
        arq.write(f'MAXIMO {maior_colisao}\n')

    media = 0
    soma = 0
    maior_colisao = 0
    vet_colisoes.clear()

    vet.clear()                                     # Limpar o vetor depois de usar para mudar para o proximo tamanho
