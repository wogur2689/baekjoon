a, b, c = map(int, input("").split())

if a == b and a == c:
  print(10000 + a * 1000)
elif a == b and a != c:
  print(1000 + a * 100)
elif a != b and b == c:
  print(1000 + b * 100)
elif c == a and c != b:
  print(1000 + c * 100)
else:
  if a > b:
    if a > c:
      print(a * 100)
    else:
      print(c * 100)
  else:
    if b > c:
      print(b * 100)
    else:
      print(c * 100)
