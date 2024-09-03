data = list(map(int, input('').split()))

sum = 0
for i in range(0, 5):
  sum += (data[i] * data[i])

print(sum % 10)
