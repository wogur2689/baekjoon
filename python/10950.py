a = int(input(''))
res = []

for i in range(0, a):
  b, c = map(int, input('').split())
  res.append(b + c)

for i in range(0, a):
  print(res[i])
