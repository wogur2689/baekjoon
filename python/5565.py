total = int(input())
sumPrice = 0

for i in range(9):
  book = int(input())
  sumPrice += book

print(total - sumPrice)
