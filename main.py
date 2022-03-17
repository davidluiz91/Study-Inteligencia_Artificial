from ag import AlgoritmoGenetico

dados = [
    {'item': '1', 'peso': 4, 'valor': 6},
    {'item': '2', 'peso': 3, 'valor': 5},
    {'item': '3', 'peso': 2, 'valor': 2},
    {'item': '4', 'peso': 8, 'valor': 10},
    {'item': '5', 'peso': 4, 'valor': 3},
    {'item': '6', 'peso': 12, 'valor': 11},
    {'item': '7', 'peso': 5, 'valor': 2},
    {'item': '8', 'peso': 13, 'valor': 7},
    {'item': '9', 'peso': 3, 'valor': 4},
    {'item': '10', 'peso': 9, 'valor': 7},

]

def funFitness(genes, dados):
    peso = 0
    valor = 0
    
    for i in range(len(genes)):
        #Adiciona os itens na bolsa
        if (genes[i]==1):
            peso += dados[i]['peso']
            valor += dados[i]['valor']
    
    if (peso > 20):
        return 0
    return valor

ag = AlgoritmoGenetico(dados,tamPopulacao=100, limGeracoes=1000 ,probMutacao=100,funcaoFitness=funFitness)
ag.executa()
print(ag.melhorResultado())

