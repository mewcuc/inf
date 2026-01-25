# обычное нахождение делителей у числа, оптимизированным способом
def f(n):
    res = []
    for i in range(2, int((n**0.5)+1)):
        if n % i == 0:
            res.append(i)
            res.append(n//i)

    return list(set(res))

#vvvvvvvvvvv Проверка на простое число vvvvvvvv

def pr(n):
    if len(f(n)) == 0:
        return True
    else:
        return False
