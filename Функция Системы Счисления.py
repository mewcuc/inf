# Перевод в троичную систему счисления, с возвратом числа int()
def tr(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return int(s)
