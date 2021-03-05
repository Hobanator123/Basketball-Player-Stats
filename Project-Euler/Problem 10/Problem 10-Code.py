primes = [2]
x = 3
i = 0
while primes[-1] < 2000000:
    for y in primes: 
        if x%y == 0:
            x +=2
            break
    else:
        i += primes[-1]
        primes.append(x)
        print(primes[-1])
        x += 2

print(i)
