sum = 0
arrays1 = [int(input()) for i in range(4)]
arrays1.remove(min(arrays1))

arrays2 = [int(input()) for i in range(2)]
arrays2.remove(min(arrays2))

arrays1.extend(arrays2)

for i in arrays1:
  sum += i

print(sum)
