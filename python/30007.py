n = int(input())
for i in range(n):
  a, b, c = map(int, input().split())
  print((a * c) - (a * 1) + b)
