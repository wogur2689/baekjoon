import sys
a = int(input())
res = []

for i in range(a):
  b,c = map(int, sys.stdin.readline().split())
  res.append(b + c)

for i in range(0, a):
  print(res[i])
