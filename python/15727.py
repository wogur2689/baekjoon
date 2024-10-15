n = int(input())
sum = 0
a = int(n / 5)
if n % 5 == 0:
  sum += a
else:
  sum += a + 1
print(sum)
