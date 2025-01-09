n, k = map(int, input().split())
g = list(map(int, input().split()))
p = []

for i in range(k):
  p.append(int(g[i] * 100 / n))

t = [4, 11, 23, 40, 60, 77, 89, 96, 100]

# 반복문으로 등급 찾기
for i in p:
    grade = 0
    if i <= 4:
        grade = 1
    elif i <= 11:
        grade = 2
    elif i <= 23:
        grade = 3
    elif i <= 40:
        grade = 4
    elif i <= 60:
        grade = 5
    elif i <= 77:
        grade = 6
    elif i <= 89:
        grade = 7
    elif i <= 96:
        grade = 8
    else:
        grade = 9
    print(grade, end = ' ')
