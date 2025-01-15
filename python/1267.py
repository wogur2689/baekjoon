n = int(input())
s = list(map(int, input().split()))
y, m = 0, 0

for i in range(n):
  y += int(s[i] // 30 + 1) * 10

  m += int(s[i] // 60 + 1) * 15

if y>m:
    print(f"M {m}")
elif y<m:
    print(f"Y {y}")
else :
    print(f"Y M {m}")
