Para cada nome recebido do arquivo "nomes_10000.txt" a função "polinomial_hash" transforma as letras
do nome atual em números inteiros conforme a tabela ascii e utilizando tais números, calcula pelo
método polinomial a posição que o nome atual tem que estar na tabela hash. 
Quando um nome tem um valor calculado que já foi calculado antes, a função ".append" cria um vetor na posição 
da tabela correspondente.
Na hora da consulta, percorre-se o vetor que está na posição n até encontrar o nome procurado, ou seja, cada 
posição percorrida nesse vetor caracteriza uma colisão.
