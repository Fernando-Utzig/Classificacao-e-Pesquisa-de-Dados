import time


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


# Insere nome na Trie
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


# Calculo hash usando o id do jogador ou do user
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


# Calculo hash usando o nome do jogador
def polinomial_hash_nomes_players(word, M):
    p = 31                                          # Primeiro número primo > 26
    hash = 0
    for i in word:
        if (i != '\n') and (i != ' '):              # Tranforma as letras em int e soma elas
            num = ord(i)
            hash = (p * hash + num) % M             # Calculo polinomial
    return hash


# Função que calcula a media das notas
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


# Pega informações da pesquisa_por_user e acha os nomes dos jogadores
def pesquisa_por_user0(hash_player_id, id_e_nota):
    nomes_jogadores = []
    for i in range(0, len(id_e_nota)):
        pos_hash_jogador = polinomial_hash_id_players(id_e_nota[i][0], len(hash_player_id))
        possiveis_jogadores = hash_player_id[pos_hash_jogador]
        for j in range(0, len(possiveis_jogadores)):
            if id_e_nota[i][0] == possiveis_jogadores[j][0]:
                nomes_jogadores.append(possiveis_jogadores[j][1])
                nomes_jogadores.append(id_e_nota[i][1])
    return nomes_jogadores


# Pega o id do jogador e manda para pesquisa_por_user0 para ela achar os nomes dos jogadores
def pesquisa_por_user(user, hash_user, hash_player_id):
    id_e_nota = []
    pos_hash_users = polinomial_hash_id_players(user, len(hash_user))
    possiveis_id = hash_user[pos_hash_users]
    for i in range(0, len(possiveis_id)):
        if user == possiveis_id[i][0]:
            id_e_nota.append(possiveis_id[i][1:3])
    nomes_e_notas = pesquisa_por_user0(hash_player_id, id_e_nota)
    return nomes_e_notas


inicio = time.time()

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
hash_players_id = hash_players.copy()
for j in range(0, len(players)):
    pos_hash_players = polinomial_hash_nomes_players(players[j][1], M_players)
    pos_hash_players_id = polinomial_hash_id_players(players[j][0], M_players)

    players[j][len(players[j])-1] = players[j][len(players[j])-1][:-1]

    hash_players[pos_hash_players].append(players[j])
    hash_players_id[pos_hash_players_id].append(players[j])
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
# ----------------------------------------------------------------------------------------------------------------------

M_users = M_rating
hash_users = [[] for _ in range(0, M_users)]
for j in range(0, len(rating)):
    pos_hash_users = polinomial_hash_id_players(rating[j][0], M_users)
    hash_users[pos_hash_users].append(rating[j])

tr = Trie()
insert_trie(players2)

fim = time.time()
tempo = fim - inicio
print(f'Tempo para carregamento de dados: {tempo} segundos')

while True:
    comando = input("Digite um comando: ")
    if comando.lower() == "quit":
        break
    else:
        comando = comando.split(' ')
        if comando[0] == 'player':
            name = comando[1]
            name = name.capitalize()
            pesquisa = (tr.search(name))
            print('ID\t\tNOME\t\tPOS\t\tNOTA\t\tCOUNT')
            for x in pesquisa:
                info = pesquisa_por_nome(x, hash_players_stg2)
                for i in range(0, len(info)):
                    if i == len(info) - 1:
                        print(info[i], end="\n")
                    elif len(info) - 3 > i > 1:
                        print(info[i], end=",")
                    else:
                        print(info[i], end="\t")

        elif comando[0] == 'user':
            user = comando[1]
            nomes_players_avaliados = pesquisa_por_user(str(user), hash_users, hash_players_id)
            print('ID\t\tNOME\t\tPOS\t\tNOTA_GOLBAL\t\tCOUNT\t\tNOTA')
            for y in range(0, len(nomes_players_avaliados)):
                if (y % 2) == 0:
                    info = pesquisa_por_nome(nomes_players_avaliados[y], hash_players_stg2)
                    for i in range(0, len(info)):
                        if len(info) - 3 > i > 1:
                            print(info[i], end=",")
                        else:
                            print(info[i], end="\t\t")
                else:
                    nomes_players_avaliados[y] = nomes_players_avaliados[y].replace('\n', '')
                    print(nomes_players_avaliados[y])
        else:
            print('comando invalido')
        continue
