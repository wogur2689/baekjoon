a, b = map(int, input().split())
if a - b < 0:
  res = (a - b) * -1
  print(res)
else :
  print(a - b)
