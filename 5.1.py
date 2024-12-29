# Ввод количества собранных килограммов
x = float(input("Введите количество собранных килограммов: "))

# Рассчёт заработка в зависимости от количества собранного урожая
if x <= 50:
    salary = x * 0.30
elif 50 < x <= 75:
    salary = x * 0.50
elif 75 < x <= 90:
    salary = x * 0.65
else:
    salary = x * 0.70 + 20  # Премия 20 рублей за сбор свыше 90 кг

# Вывод заработка
print(f"Заработок студента: {salary:.2f} руб.")