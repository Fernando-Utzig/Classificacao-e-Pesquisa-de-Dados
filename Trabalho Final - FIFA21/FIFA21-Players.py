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


def polinomial_hash_id_players(word, M):
    p = 11                                          # Primeiro número primo > 10,
    hash_primario = 0
    hash_final = 0
    for i in word:
        if (i != '\n') and (i != ' '):
            num = int(i)
            hash_primario = (p * hash_primario + num)             # Calculo polinomial
            hash_final = hash_primario % M
    return hash_final


def polinomial_hash_nomes_players(word, M):
    p = 31                                          # Primeiro número primo > 26
    hash = 0
    for i in word:
        if (i != '\n') and (i != ' '):              # Tranforma as letras em int e soma elas
            num = ord(i)
            hash = (p * hash + num) % M             # Calculo polinomial
    return hash


def calculo_media(hash_rating, vet_players, M_rating, hash_players, M_players):
    for i in range(0, len(vet_players)):
        soma = 0
        count = 0
        pos_hash_calc_nome = polinomial_hash_nomes_players(vet_players[i][1], M_players)
        pos_hash_id_atual = polinomial_hash_id_players(vet_players[i][0], M_rating)
        possiveis_notas = hash_rating[pos_hash_id_atual]
        possiveis_nomes = hash_players[pos_hash_calc_nome]
        for j in range(0, len(possiveis_notas)):
            if vet_players[i][0] == possiveis_notas[j][1]:
                soma = soma + float(possiveis_notas[j][2])
                count += 1
        if count != 0:
            media = soma / count
        else:
            media = 0
        for k in range(0, len(possiveis_nomes)):
            if vet_players[i][1] == possiveis_nomes[k][1]:
                hash_players[pos_hash_calc_nome][k].append(media)
                hash_players[pos_hash_calc_nome][k].append(count)
    return hash_players


def pesquisa_por_nome(nome, hash_players):
    pos_hash = polinomial_hash_nomes_players(nome, len(hash_players))
    posiveis_nomes = hash_players[pos_hash]
    for i in range(0, len(posiveis_nomes)):
        if nome == posiveis_nomes[i][1]:
            return posiveis_nomes[i]


# Abertura do arquivo de jogadores -------------------------------------------------------------------------------------
with open('players.csv') as f:
    players2 = f.readlines()
del players2[0]

# Separa os itens a cada virgula
players = players2.copy()
for i in range(0, len(players)):
    a = players[i].split(',')
    players[i] = a

# Cria uma tabela Hash para jogadores utilizando os nomes
M_players = int(len(players) / 5)
hash_players = [[] for _ in range(0, M_players)]
for j in range(0, len(players)):
    pos_hash_players = polinomial_hash_nomes_players(players[j][1], M_players)
    players[j][len(players[j])-1] = players[j][len(players[j])-1][:-1]
    hash_players[pos_hash_players].append(players[j])
# ----------------------------------------------------------------------------------------------------------------------

# Abertura do arquivo de notas
with open('minirating.csv') as f:
    rating = f.readlines()
del(rating[0])

for i in range(0, len(rating)):
    a = rating[i].split(',')
    rating[i] = a

M_rating = int(len(rating) / 5)
hash_rating = [[] for _ in range(0, M_rating)]
for j in range(0, len(rating)):
    pos_hash_rating = polinomial_hash_id_players(rating[j][1], M_rating)
    hash_rating[pos_hash_rating].append(rating[j])
# ----------------------------------------------------------------------------------------------------------------------

hash_players_stg2 = calculo_media(hash_rating, players, M_rating, hash_players, M_players)

tr = Trie()
insert_trie(players2)


name = input("Digite um nome para pesquisar:\n")
name = name.capitalize()
pesquisa = (tr.search(name))

print('ID\t\tNOME\t\tPOS\t\tNOTA\t\tCOUNT')
for x in pesquisa:
    info = pesquisa_por_nome(x, hash_players_stg2)
    for i in range(0, len(info)):
        if i == len(info) - 1:
            print(info[i], end="\n")
        else:
            print(info[i], end="\t")

