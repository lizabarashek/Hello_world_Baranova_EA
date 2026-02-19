weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

bmi = weight / (height ** 2)
print("\n--- Отчет о состоянии здоровья")
print(f"Рост\t\t{height}м")
print(f"Вес\t\t{weight}кг")
print(f"Индекс массы тела пациента: {bmi:.2f}") 