ves = float(input())
rost = float(input())
imt = ves / (rost ** 2) * 703

if imt < 16:
    print("выраженный дефицит массы тела")
elif imt < 18.5:
    print("недостаточная масса тела")
elif imt < 25:
    print("норма")
elif imt < 30:
    print("избыточная масса тела")
elif imt < 35:
    print("ожирение первой степени")
elif imt < 40:
    print("ожирение второй степени")
else:
    print("ожирение третьей степени")
