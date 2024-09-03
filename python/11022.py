a = int(input(''))
res = []
cal = []

for i in range(0, a):
    b, c = map(int, input('').split())
    cal.append(f'{b} + {c}')
    res.append(b + c)

for i in range(0, a):
    idx = i + 1
    rs = res[i]
    ss = cal[i]
    print(f"Case #{idx}: {ss} = {rs}")
