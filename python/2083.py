name = ''
while name != '#':
  name, n, m = input().split()
  if name != '#':
    if int(n) > 17 or int(m) >=80:
      print(name, 'Senior')
    else:
      print(name, 'Junior')
