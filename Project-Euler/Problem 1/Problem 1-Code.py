lst = [x for x in range(1,1000)]
num = 0
sum_list = []
for i in lst:
    if i%3==0 or i%5==0:
        sum_list.append(i)
print(sum(sum_list))
