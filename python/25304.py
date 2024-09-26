sum = int(input())
cnt = int(input())
newsum = 0

for i in range(0, cnt):
    a, b = map(int, input().split())
    newsum = newsum + (a * b)

if sum == newsum:
  print('Yes')
else:
  print('No')
