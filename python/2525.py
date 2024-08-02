a, b = map(int, input("").split())
oven = int(input(""))

if b + oven < 60:
  print(a, b + oven)
else:
  a = a + int((b + oven) / 60)
  b = (b + oven) % 60
  if a > 23:
    a = a - 24
  print(a, b)
