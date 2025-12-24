N, M = map(int, input().split())
res = list((range(1, N+1)))

for _ in range(0, M):
  i, j = map(int, input().split())
  res[i - 1], res[j - 1] = res[j - 1], res[i - 1]

for k in range(0, N):
  print(res[k], end = ' ')
