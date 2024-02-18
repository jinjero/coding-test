import sys

def select_m():
    if len(num) == m:
        print(' '.join(map(str, num)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        num.append(i)
        select_m()
        num.pop()
        visited[i] = False

n, m = map(int ,sys.stdin.readline().split())
num = []
visited = [False] * (n+1)

select_m()
