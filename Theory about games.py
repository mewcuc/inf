# 19 - 21
# на одну кучу:
def f(n, m):
  if s >= 41: return m % 2 == 0
  if m == 0: return 0
  h = [f(s+2, m-1), f(s*2, m-1)]
  if m % 2 == 0: return any(h)
  else: return all(h)

print('19a', [s for s in range(1, 41) if f(s, 1)]
print('19b', [s for s in range(1, 41) if f(s, 2)]
print('20', [s for s in range(1, 41) if f(s, 3) and not(f(s, 1))]
print('21', [s for s in range(1, 41) if f(s, 4) and not(f(s, 2))]

# на две кучи, и где в 19 Петя сходил НЕУДАЧНО, и где "если количество камней в куче нечётно, то остается на 1 камень больше, чем убирается, при уменьшении кучи в 2 раза:
from math import *
def f(a, b, m):
    if a + b <= 40:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a-1, b, m-1), f(ceil(a/2) , b, m-1), f(a, b-1, m-1), f(a, ceil(b/2), m-1)]
    if m % 2 == 1:
        return any(h)
    else: return all(h)

def f19(a, b, m):
    if a + b <= 40:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a-1, b, m-1), f(ceil(a/2) , b, m-1), f(a, b-1, m-1), f(a, ceil(b/2), m-1)]
    if m % 2 == 1:
        return any(h)
    else: return any(h)

print('19:', [s for s in range(21, 20000) if f19(20, s, 2)])
print('20:', [s for s in range(21, 20000) if f(20, s, 3) and not(f(20, s, 1))])
print('21:', [s for s in range(21, 20000) if f(20, s, 4) and not(f(20, s , 2))])
