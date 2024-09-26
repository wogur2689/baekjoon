n = int(input())
byte = []

for i in range(0, n):
  if i % 4 == 0:
    byte.append('long ')

byte.append('int')
print("".join(byte))
