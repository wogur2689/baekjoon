while True:
  n = input()
  if int(n) == 0:
    break
  sum = 1
  for i in n:
    k = int(i)
    if k == 1:
      sum += 2
    elif k == 0:
      sum += 4
    else:
      sum += 3
    sum += 1
  print(sum)
  
