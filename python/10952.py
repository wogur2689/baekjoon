data = []
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0 :
    break
  data.append(a + b)

for i in data:
  print(i)
