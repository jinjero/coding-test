import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

choice = 0
favor = [[True for _ in range(n)] for _ in range(n)]

for _ in range(m):
  bad, taste = map(int, input().split())
  favor[bad - 1][taste - 1] = False
  favor[taste - 1][bad - 1] = False

for i in combinations(range(n), 3): 
  if favor[i[0]][i[1]] and favor[i[1]][i[2]] and favor[i[2]][i[0]]:
    choice += 1
  
print(choice)
