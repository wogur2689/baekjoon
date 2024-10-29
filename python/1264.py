mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
s = ''

while s != '#':
  s = input()
  if s == '#':
    break
  sum = 0
  for i in range(len(s)):
    for j in range(len(mo)):
      if s[i] == mo[j]:
        sum += 1
  print(sum)
