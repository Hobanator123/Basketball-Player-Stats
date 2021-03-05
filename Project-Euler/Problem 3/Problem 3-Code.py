primes = [2]
x = 3
while x < 30000:
    for y in primes:
        if x%y == 0:
            x +=2
            break
    else:
        primes.append(x)
        x += 2
#^creates a list of prime numbers up to 30000
n = 600851475143 
top_prim_fact = 0
for i in primes:
    while n%i == 0:
        n = n/i
        top_prim_fact = i

print(top_prim_fact)
