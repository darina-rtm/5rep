def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

# Пример использования
x = int(input("Введите первое число (x): "))
y = int(input("Введите второе число (y): "))

if is_divisible(x, y):
    print(f"{x} делится на {y} нацело.")
else:
    print(f"{x} не делится на {y} нацело.")
