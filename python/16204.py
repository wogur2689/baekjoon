n, m, k = map(int, input().split())

frontX = n - m 
backX = n - k

count1 = min(m, k)
count2 = min(frontX, backX)

print(count1 + count2)
