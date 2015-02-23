import sys

class Matrix(object):
    @classmethod
    def Create(cls, width, height):
        matrix = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(0)
            matrix.append(row)
        
        return matrix


#capacidade = int(15)        
#items = [ #VALOR, #PESO
#         (5, 3),
#         (6, 5),
#         (11, 6),
#         (12, 7)
#         ]
sys.stdin = open("dataset.txt", "r")
line = sys.stdin.readline()
capacidade = int(line)
items = []

for line in iter(sys.stdin.readline, ''):
    line = line.strip().split()
    items.append([int(item) for item in line[0:]])

# cria as matrizes de take e Values
valores = Matrix.Create(capacidade + 1, len(items) + 1)
take = Matrix.Create(capacidade + 1, len(items) + 1)

for i in range(len(items) + 1):
    
    item = items[i - 1]
    
    for w in range(capacidade + 1):
        
        if i == 0 or w == 0:
            valores[i][w] = 0
            take[i][w] = 0
        
        if i != 0 and w != 0:
            peso = item[1]
            valor = item[0]
            
            if peso > w:
                valores[i][w] = valores[i - 1][w]
                take[i][w] = 0
            else:
                maximo = max(valor + valores[i - 1][w - peso], valores[i - 1][w])
                valores[i][w] = maximo
                
                take[i][w] = 1 if maximo != valores[i - 1][w] else 0

#descobre os items
i = len(items)
w = capacidade

solucao = []
    
while i > 0:
    if take[i][w] == 1: # I want this
        solucao.append(items[i - 1])
        w -= items[i - 1][1]

    i -= 1

pesoMax = 0
valorMax = 0

print("Solucao")
for item in solucao:
    pesoMax += item[1]
    valorMax += item[0]
    
print(solucao)

print("MAXVAL -> %d\nMAXPESO -> %d" % (valorMax, pesoMax))