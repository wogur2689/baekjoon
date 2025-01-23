import sys
n = int(input())
sum = 0

for i in range(n):
  k = int(sys.stdin.readline())
  sum += k - 1

print(sum+1)
