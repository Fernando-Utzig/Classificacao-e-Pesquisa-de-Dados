# Laboratorio 1
# Nomes: Fernando Vieira Utzig e Thiago Leonel Rancan Bischoff
# Turma: B
import time


def shell_sort(vetor, n, ex):
    # intervalos -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,...

    # Abertura do arquivo
    # ------------------------------------------
    if ex == 1:  # Controle para escrever no arquivo certo
        with open('saida1.txt', 'a') as arquivo:
            for valor in vetor:
                arquivo.write(str(valor) + ', ')  # Escrita da string e a sequencia utilizada
            arquivo.write('SEQ = SHELL')
    # -------------------------------------------

    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo

            vetor[j] = temp

        #  Escrita, no aquivo, do vetor e do intervalo utilizado a cada passo
        # --------------------------------------------
        if ex == 1:
            with open('saida1.txt', 'a') as arquivo:
                arquivo.write('\n')
                for valor in vetor:
                    arquivo.write(str(valor) + ', ')
                arquivo.write('INCR = ')
                arquivo.write(str(intervalo))
        # ---------------------------------------------

        intervalo //= 2

    # Espaçamento entre um vetor e outro
    # ---------------------------------------------
    if ex == 1:
        with open('saida1.txt', 'a') as arquivo:
            arquivo.write('\n')
    # ---------------------------------------------


def knuth_shell_sort(vetor, n, ex):
    # intervalos -> 1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484,...

    # Abertura do arquivo
    # ------------------------------------------
    if ex == 1:  # Controle para escrever no arquivo certo
        with open('saida1.txt', 'a') as arquivo:
            for valor in vetor:
                arquivo.write(str(valor) + ', ')  # Escrita da string e a sequencia utilizada
            arquivo.write('SEQ = KNUTH')
    # -------------------------------------------

    intervalo = 1
    while intervalo < n:
        intervalo = (intervalo * 3) + 1

    while intervalo != 1:
        intervalo //= 3
        for i in range(intervalo, n):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo

            vetor[j] = temp

        #  Escrita, no aquivo, do vetor e do intervalo utilizado a cada passo
        # --------------------------------------------
        if ex == 1:
            with open('saida1.txt', 'a') as arquivo:
                arquivo.write('\n')
                for valor in vetor:
                    arquivo.write(str(valor) + ', ')
                arquivo.write('INCR = ')
                arquivo.write(str(intervalo))
        # ---------------------------------------------
        # Espaçamento entre um vetor e outro
    if ex == 1:
        with open('saida1.txt', 'a') as arquivo:
            arquivo.write('\n')
    # ---------------------------------------------


def ciura_shell_sort(vetor, n, ex):
    # intervalos -> 1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711,....

    # utilizando a sequencia pronta nesta função
    seq = [1, 4, 10, 23, 57, 132, 301, 701, 1577, 3548, 7983, 17961, 40412, 90927, 204585, 460316, 1035711]
    i = 0

    # Abertura do arquivo
    # ------------------------------------------
    if ex == 1:  # Controle para escrever no arquivo certo
        with open('saida1.txt', 'a') as arquivo:
            for valor in vetor:
                arquivo.write(str(valor) + ', ')  # Escrita da string e a sequencia utilizada
            arquivo.write('SEQ = CIURA')
    # -------------------------------------------

    while i < 20:
        if seq[i + 1] >= n:
            while i >= 0:
                for j in range(seq[i], n):
                    aux = vetor[j]
                    contador_aux = j
                    while contador_aux >= seq[i] and vetor[contador_aux - seq[i]] > aux:
                        vetor[contador_aux] = vetor[contador_aux - seq[i]]
                        contador_aux = contador_aux - seq[i]
                    vetor[contador_aux] = aux

                #  Escrita, no aquivo, do vetor e do intervalo utilizado a cada passo
                # --------------------------------------------
                if ex == 1:
                    with open('saida1.txt', 'a') as arquivo:
                        arquivo.write('\n')
                        for valor in vetor:
                            arquivo.write(str(valor) + ', ')
                        arquivo.write('INCR = ')
                        arquivo.write(str(seq[i]))
                # ---------------------------------------------

                i = i - 1

            i = 20

            # Espaçamento entre um vetor e outro
            # -----------------------------------------------
            if ex == 1:
                with open('saida1.txt', 'a') as arquivo:
                    arquivo.write('\n')
            # ---------------------------------------------
        else:
            i = i + 1


#  -------------------------- EXERCICIO 1 ----------------------------
Exercicio = 1  # Controle para escrever no arquivo certo

with open('entrada1.txt', 'r') as f:
    tam = [int(r.split()[0]) for r in f]

qtd_vetores = len(tam)  # quantidade de primeiros termos(tamanho do vetor) = quantidade de vetores

with open('entrada1.txt', 'r') as f:
    for k in range(qtd_vetores):
        data = f.readline()
        vet = [int(i) for i in data.split()]

        del vet[0]  # exluir o tamanho do vetor da string

        vet_aux = vet.copy()  # variaveis auxiliares
        vet_aux1 = vet.copy()

        shell_sort(vet, tam[k], Exercicio)
        knuth_shell_sort(vet_aux, tam[k], Exercicio)
        ciura_shell_sort(vet_aux1, tam[k], Exercicio)

        k += 1
    f.close()

#  -------------------------- EXERCICIO 2 ----------------------------

Exercicio = 2  # Controle para não escrever no arquivo errado

tam = [100, 1000, 10000, 100000, 1000000]  # tamanhos dos vetores

with open('entrada2.txt', 'r') as f:
    for k in range(5):
        data = f.readline()
        vet = [int(i) for i in data.split()]

        del vet[0]

        vet_aux = vet.copy()  # variaveis auxiliares
        vet_aux1 = vet.copy()

        inicio = time.time()  # inicio da marcação do tempo
        shell_sort(vet, tam[k], Exercicio)
        fim = time.time()  # final da marcação do tempo
        tempo = fim - inicio  # diferença =  tempo decorrido
        with open('saida2.txt', 'a') as arq:
            arq.write('SHELL, ')
            arq.write(str(tam[k]))
            arq.write(', ')
            arq.write(str(tempo))
            arq.write('\n')

        inicio = time.time()
        knuth_shell_sort(vet_aux, tam[k], Exercicio)
        fim = time.time()
        tempo = fim - inicio
        with open('saida2.txt', 'a') as arq:
            arq.write('KNUTH, ')
            arq.write(str(tam[k]))
            arq.write(', ')
            arq.write(str(tempo))
            arq.write('\n')

        inicio = time.time()
        ciura_shell_sort(vet_aux, tam[k], Exercicio)
        fim = time.time()
        tempo = fim - inicio
        with open('saida2.txt', 'a') as arq:
            arq.write('CIURA, ')
            arq.write(str(tam[k]))
            arq.write(', ')
            arq.write(str(tempo))
            arq.write('\n')

        k += 1
    f.close()
