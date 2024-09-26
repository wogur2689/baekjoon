m, n = map(int, input().split())

result = list(0 for i in range(m))

for p in range(n):
  i, j, k = map(int, input().split())
  for s in range(i - 1, j):
    result[s] = k

for r in result:
  print(r, end = ' ')
