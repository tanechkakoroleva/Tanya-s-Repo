a, b = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))
def fits(x, y, a, b):
    return (x <= a and y <= b) or (x <= b and y <= a)

if fits(c, d, a, b) or fits(c, e, a, b) or fits(d, e, a, b):
    print("Да")
else:
    print("Нет")
