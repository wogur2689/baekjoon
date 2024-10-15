n = int(input())
logicA = n * 0.22
logicB = n * 0.2
a = n - logicA
b = logicB - (logicB * 0.22)
c = n * 0.8 + b
print(int(a), int(c), end = '') 
