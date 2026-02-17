reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество реактива (шт.): "))

report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."
print(report)

with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Отчет также сохранен в файл inventory.txt")
