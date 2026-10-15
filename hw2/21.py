s1, s2 = input().split('-')

c = abs(ord(s1[0]) - ord(s2[0]))
r = abs(int(s1[1]) - int(s2[1]))

if c*r == 2: print('верно')
else: print('ошибка')
