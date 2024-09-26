arrayData = list()

for i in range(0, 9):
  data = int(input())
  arrayData.append(data)

max = arrayData[0]
sortnum = 0

for i in range(0, 9):
  if max < arrayData[i]:
    max = arrayData[i]
    sortnum = i

print(max)
print(sortnum + 1)
