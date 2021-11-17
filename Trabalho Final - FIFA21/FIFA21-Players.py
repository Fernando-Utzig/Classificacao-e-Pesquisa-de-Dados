class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


# Classe que ira armazenar a funções da árvore trie.
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    # Função para inserir elementos na árvore.
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def dfs(self, node, pre):
        if node.is_end:
            self.output.append((pre + node.char))
        for child in node.children.values():
            self.dfs(child, pre + node.char)

    # Função para procurar elementos na árvore.
    def search(self, x):
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.output = []
        self.dfs(node, x[:-1])
        return self.output


def insert_trie(contents):
    for x in range(0, len(contents)):     
        test = 0                          
        string = ''                              
        for i in contents[x]:                       
            if i == ',':                      
                test += 1 
            if (test == 1) and ((i != '\n') and (i != ',')):
                string = string + i
        tr.insert(string)

            
def polinomial_hash_nomes_players(word, M):
    p = 31                                          # Primeiro número primo > 26
    hash = 0
    for i in word:
        if (i != '\n') and (i != ' '):              # Tranforma as letras em int e soma elas
            num = ord(i)
            hash = (p * hash + num) % M             # Calculo polinomial
    return hash


# Na pesquisa por nome, adiciona informações à pesquisa
def pesquisa_por_nome(nome, hash):
    pos_hash = polinomial_hash_nomes_players(nome, len(hash))
    posiveis_nomes = hash[pos_hash]
    for i in range(0, len(posiveis_nomes)):
        cursor1 = 0
        cursor2 = 0
        cont_cursor = 0
        while cursor1 != ',':                           # Pega o nome do jogador entre a primeira e segunda virgula
            cursor1 = posiveis_nomes[i][cont_cursor]
            cont_cursor += 1
        cursor_inicio = cont_cursor - 1
        while cursor2 != ',':
            cursor2 = posiveis_nomes[i][cont_cursor]
            cont_cursor += 1
        cursor_final = cont_cursor - 1
        nome_jogador = posiveis_nomes[i][cursor_inicio + 1:cursor_final]
        if nome == nome_jogador:
            return posiveis_nomes[i]
        
with open('players.csv') as f:
    players = f.readlines()
del players[0]


# Monta a tabela hash usando o nome do jogador
M = int(len(players) / 5)                               # Tamanho da tabela hash
hash_players = [[] for _ in range(0, M)]
for i in range(0, len(players)):
    cursor_inicio = 0
    cursor_final = 0
    cursor1 = 0
    cursor2 = 0
    cont_cursor = 0
    while cursor1 != ',':                               # Pega o nome do jogador entre a primeira e segunda virgula
        cursor1 = players[i][cont_cursor]
        cont_cursor += 1
    cursor_inicio = cont_cursor - 1
    while cursor2 != ',':
        cursor2 = players[i][cont_cursor]
        cont_cursor += 1
    cursor_final = cont_cursor - 1
    nome_jogador_players = players[i][cursor_inicio + 1:cursor_final]
    pos_hash = polinomial_hash_nomes_players(nome_jogador_players, M)
    hash_players[pos_hash].append(players[i])
    

tr = Trie()
insert_trie(players)

name = input("Digite um nome para pesquisar:\n")
name = name.capitalize()
pesquisa = (tr.search(name))
for x in pesquisa:
    info = pesquisa_por_nome(x, hash_players)
    print(info)

"""
import csv

with open(''minirating.csv', ‘r’) as arquivo_csv:  
    leitor = csv.reader(arquivo_csv, delimiter=’,’)    
    for coluna in leitor:        
        print(coluna)


# [‘Nome’, ‘Profissao’]
# [‘Renato’, ‘Programador’]
# [‘Ana’, ‘Faxineira’]
"""
