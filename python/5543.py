berger = [int(input()) for _ in range(3)]
tansan = [int(input()) for _ in range(2)]
min = 2000

for i in berger:
  for j in tansan:
    if i + j < min:
      min = i + j

print(min - 50)
