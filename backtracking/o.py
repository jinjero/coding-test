import sys

input = sys.stdin.readline
n = int(input())
w = [list() for _ in range(n)]

for i in range(n):
    dests = list(map(int, input().split()))
    for j in range(n):
        if dests[j] == 0:
            if i != j:
                w[i].append(1e9)
        w[i].append(dests[j])

print(w)

start = 0
cost = 0
min_cost = 1e9
visited = [0 for _ in range(n)]

def back(node):
    global cost
    global min_cost
    visited[node] = 1
    if node == start and cost != 0:
        if min_cost > cost:
            min_cost = cost
        return
    for i in range(n):
        if i == node:
            continue
        if w[node][i] == 1e9:
            continue
        if not visited:
            cost += w[node][i]
            back(i)
            visited[i] = 0
            cost -= w[node][i]

back(0)
print(min_cost)
    