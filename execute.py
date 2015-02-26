import sys
from Knapsack01 import Knapsack01

sys.stdin = open("dataset.txt", "r")

line = sys.stdin.readline()
capacidade = int(line)
items = []

for line in iter(sys.stdin.readline, ''):
    line = line.strip().split()
    items.append([int(item) for item in line[0:]])

knapsack = Knapsack01(capacidade, len(items), items)
ans = knapsack.solve()
print(ans)

for solution in ans[2]:
    print(solution) 