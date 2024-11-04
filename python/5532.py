s = list()
for i in range(5):
  k = int(input())
  s.append(k)

a = 0
b = 0
if s[1] % s[3] != 0:
  a = s[1] / s[3] + 1
else:
  a = s[1] / s[3]

if s[2] % s[4] != 0:
  b = s[2] / s[4] + 1
else:
  b = s[2] / s[4]

if a > b:
  print(s[0] - int(a))
else:
  print(s[0] - int(b))
