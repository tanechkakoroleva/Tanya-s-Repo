x, y, n = map(int, input().split())
a = n * (x * 100 + y)
x = a//100
y = a%100
print(x, "руб.", y, "коп.")
