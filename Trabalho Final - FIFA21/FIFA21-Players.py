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

        
with open('players.csv') as f:
    players = f.readlines()
del players[0]

name = input("Digite um nome para pesquisar.")
consult = (tr.search(name))
print(consult)

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
