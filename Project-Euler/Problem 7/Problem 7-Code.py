primes = [2]
x = 3
    
while len(primes) < 10001:
    for y in primes: 
        if x%y == 0:
            x +=2
            break
    else:
        primes.append(x)
        x += 2
        
print(primes[-1])
