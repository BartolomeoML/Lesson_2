# Запрашиваем у пользователя целое число
number = int(input("Введите целое число: "))

# Выводим таблицу умножения
print(f"\nТаблица умножения для числа {number}:\n")

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")