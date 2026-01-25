f = open('9.txt')

k = 0

for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
  
    # ЗАДАНИЕ
  
            k += 1
print(k)
