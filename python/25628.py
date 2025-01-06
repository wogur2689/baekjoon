a, b = map(int, input().split())
count = 0
for i in range(a):
  if a > 1 and b > 0:
    a -= 2
    b -= 1
    count += 1

print(count)
