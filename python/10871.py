n, x = map(int, input('').split())
data = list(map(int, input('').split()))
result = []

for i in range(0, n):
  if data[i] < x:
    result.append(data[i])

for j in result:
  print(j, end = ' ')
