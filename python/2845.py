n, m = map(int, input().split())
abc = list(map(int, input().split()))

for i in range(len(abc)):
  if n*m != i:
    abc[i] -= n*m

print(*abc)
