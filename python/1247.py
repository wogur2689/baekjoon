for i in range(3):
  n = int(input())
  sum = 0

  for j in range(n):
    k = int(input())
    sum += k

  if sum == 0:
    print(0)
  elif sum > 0:
    print("+")
  else:
    print("-")
