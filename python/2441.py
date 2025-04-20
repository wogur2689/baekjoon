s = int(input())

for i in range(0, s):
  for j in range(0, i):
    print(' ', end = '')
  for j in range(i, s):
    print('*', end = '')
  print(' ')
