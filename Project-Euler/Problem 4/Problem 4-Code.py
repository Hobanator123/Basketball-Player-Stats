def palind(s):
    return s == s[::-1]

a = 100
b = 100
biggest_palind = 0

while a <= 999:
    while b <= 999:
        result = a*b
        if result > biggest_palind and palind(str(result)):
            biggest_palind = result
        b+=1
    b = 100
    a+=1
