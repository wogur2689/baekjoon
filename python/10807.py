cnt = int(input())
data = list(map(int, input('').split()))
num = int(input())
dataisnum = 0

for i in range(0, cnt):
  if data[i] == num:
    dataisnum += 1

print(dataisnum)
