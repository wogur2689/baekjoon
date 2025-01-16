n = int(input())
gong = 1
for i in range(n):
  x, y = map(int, input().split())
  if x == gong:
    gong = y
  elif y == gong:
    gong = x

print(gong)
