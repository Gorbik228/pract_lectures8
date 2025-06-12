def vich(a,b):
    y =(((a + b)**3)/(a-b)**2)
    return round(y,4)


a = float(input("Введите число: "))
b = float(input("Введите число: "))
if a == b:
    print("Деление на ноль")
else:
    x =(((a + b)**3)/(a-b)**2)
    if x >= 0:
        y = x ** 0.5
        print("Решение", vich(a,b))
    else:
        print("Под корнем отрицательное выражение")

















