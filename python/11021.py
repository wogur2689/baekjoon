a = int(input(''))
res = []

for i in range(0, a):
  b, c = map(int, input('').split())
  res.append(b + c)

for i in range(0, a):
  idx = i + 1
  rs = res[i]
  print(f"Case #{idx}: {rs}")
