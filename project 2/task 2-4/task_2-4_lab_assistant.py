volume=float(input("Введите нужный объем физиологического раствора (мл):"))
salt = volume*0.009
salt_rounded = round(salt,2)
water_volume = volume
with open("recipe.txt","w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-----------------------\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {salt_rounded} г\n")
    file.write(f"Объем воды:  {water_volume} мл\n")
print(f"\nРецепт успешно сохранен в файл recipe.txt")
print(f"Для приготовления {volume} мл 0.9% физиологического раствора требуется:")
print(f"- Соль: {salt_rounded} г")
print(f"- Вода: {water_volume} мл")