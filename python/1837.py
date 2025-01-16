# 입력 받기
p, k = map(int, input().split())
bad = 0
prime_num = 0

sieve = [True] * k
sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님
for i in range(2, int(k**0.5) + 1):
  if sieve[i]:
    for j in range(i * i, k, i):
      sieve[j] = False
primes = [x for x in range(2, k) if sieve[x]]
    
for prime in primes:
  remainder = 0
  for digit in str(p):
    remainder = (remainder * 10 + int(digit)) % prime
  if remainder == 0:
      bad = 1
      prime_num = prime
      break

if bad == 1:
  print(f"BAD {prime}")
else:
  print("GOOD")
