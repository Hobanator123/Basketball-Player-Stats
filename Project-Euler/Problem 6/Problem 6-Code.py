lst1 = [x**2 for x in range(1,101)]
lst2 = [x for x in range(1,101)]

soq = sum(lst1)
qos = (sum(lst2))**2

print(qos-soq)
