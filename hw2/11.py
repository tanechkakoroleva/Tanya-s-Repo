import turtle
xc = int(input("xc = "))
yc = int(input("yc = "))
r = int(input("r = "))
x = int(input("x = "))
y = int(input("y = "))


tochka_center = (x - xc)**2 + (y - yc)**2

if tochka_center < r**2:
    a = "Точка внутри окружности"
elif tochka_center == r**2:
    a = "Точка на окружности"
else:
    a = "Точка вне окружности"

print(a)

# Настройка turtle
turtle.speed(0)
turtle.hideturtle() #скрывает значок черепашки
turtle.penup() #поднимает «перо» черепашки

# Рисование окружности
# Переходим в нижнюю точку окружности, чтобы нарисовать её с центром в (xc, yc)
turtle.goto(xc, yc - r)
turtle.pendown()
turtle.circle(r)
turtle.penup()

# Рисование точки (красный кружок)
turtle.goto(x, y)
turtle.dot(10, "red")

# Вывод текста под окружностью
turtle.goto(xc, yc - r - 30)
turtle.color("red")
turtle.write(a, align="center", font=("Arial", 12, "normal"))

turtle.done()
