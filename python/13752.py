n = int(input())
arrays = []

for i in range(n):
  j = int(input())
  arrays.append(j)

for s in range(n):
  for p in range(arrays[s]):
    print('=', end ='')
  print()
