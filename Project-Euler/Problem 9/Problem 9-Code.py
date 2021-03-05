import math
#creates list of every number from 1-1000 squared
lst = [x**2 for x in range(1,1001)]
lsttr = []
#creates a list of pythagorean triples(each triple in a tuple) that can be made from 1st list
for i in lst:
    for x in lst:
        if math.sqrt(i+x)%1==0:
            lsttr.append((math.sqrt(i),math.sqrt(x),math.sqrt(i+x)))

#finds the one triple where the three numbers add to 1000
for i in lsttr:
    if i[0]+i[1]+i[2]==1000:
        print(i[0]*i[1]*i[2])
