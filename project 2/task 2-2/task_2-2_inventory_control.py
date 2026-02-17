# Запрос названия реактива 
reactant_name = input("Введите название нового реактива: ")

# Запрос количества реактива
reactant_quantity = int(input("Введите количество реактива (целое число): "))

# Вывод отчета
print(f"Реактив {reactant_name} поступил на склад в количестве {reactant_quantity} шт.")

# запись отчета в файл
file = open("inventory.txt", "w", encoding="utf-8")
file.write(f"Реактив {reactant_name} поступил на склад в количестве {reactant_quantity} шт.")
file.close()

print("Отчет также сохранен в файл inventory.txt")