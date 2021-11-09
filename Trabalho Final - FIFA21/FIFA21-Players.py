import csv

with open(''minirating.csv', ‘r’) as arquivo_csv:  
    leitor = csv.reader(arquivo_csv, delimiter=’,’)    
    for coluna in leitor:        
        print(coluna)


# [‘Nome’, ‘Profissao’]
# [‘Renato’, ‘Programador’]
# [‘Ana’, ‘Faxineira’]