# обычное нахождение делителей у числа, оптимизированным способом
def f(n):
    res = []
    for d in range(2, int((n**0.5)+1)):
        if n % d == 0:
            res.append(d)
            res.append(n//d)

    return list(set(res))

#vvvvvvvvvvv Проверка на простое число vvvvvvvv

def pr(n):
    if len(f(n)) == 0:
        return True
    else:
        return False
'''..................................................'''

def prime(n):
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return n > 1

for i in range(1, 20):
    if prime(i):
        print(i)

# либо вот такой вариант еще
def sigma(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n**0.5) + 1))
