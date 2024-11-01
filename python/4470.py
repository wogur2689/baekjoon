n = int(input())
s = list()
for i in range(n):
  name = input()
  s.append(name)

for j in range(n):
  print(f"{j + 1}. {s[j]}")
