a, b = map(int, input("").split())

if b - 45 >= 0:
  print(a, b - 45)
else:
  if a > 0:
    a = a - 1
  else: 
    a = 23
  b = 60 + (b - 45)
  print(a, b)
