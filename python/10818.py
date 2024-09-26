cnt = int(input())
data = list(map(int, input('').split()))
min, max = data[0], data[0]

for i in range(1, cnt):
  if min > data[i]:
     min = data[i]
  if max < data[i]:
     max = data[i]

print(min, max)
