a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = input()
cnt = 0

for i in a:
  for j in s:
    if i == j:
      cnt += 1
  print(cnt, end = ' ')
  cnt = 0
