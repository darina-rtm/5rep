def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Пример использования
n = int(input("Введите натуральное число: "))
divisors = get_divisors(n)

print(f"Делители числа {n}: {divisors}")
