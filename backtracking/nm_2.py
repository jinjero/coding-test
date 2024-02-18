import sys

n, m = map(int, sys.stdin.readline().split())
num = []

def select(start):
  if len(num) == m:
    print(' '.join(map(str, num)))
    return
  for i in (start, n+1):
    if i in num:
      continue
    else:
      num.append(i)
      select(i+1)
      num.pop()

select(1)
