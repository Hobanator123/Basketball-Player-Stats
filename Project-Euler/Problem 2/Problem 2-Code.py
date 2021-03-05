fibb = [1,1]
fibbeven = []
while fibb[-1]<4000000:
        fibb.append(fibb[-1]+fibb[-2])
for i in range(len(fibb)):
    if fibb[i]%2==0:
        fibbeven.append(fibb[i])
print(sum(fibbeven))
