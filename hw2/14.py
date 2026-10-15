n = int(input())
s = n//29
n %= 29
g = s//17
s %= 17

if g != 0: print(g, 'галлеонов')
if s != 0: print(s, 'сиклей')
if n != 0: print(n, 'кнатов')
