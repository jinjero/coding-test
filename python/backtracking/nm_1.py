import sys

def select_m():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        select_m()
        s.pop()
        visited[i] = False

n, m = map(int ,sys.stdin.readline().split())
s = []
visited = [False] * (n+1)

select_m()