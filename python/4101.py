a = 1
while a != 0:
  n, s = map(int, input().split())
  if n == 0 & s == 0:
    break
  if n > s :
    print("Yes")
  else:
    print("No")
