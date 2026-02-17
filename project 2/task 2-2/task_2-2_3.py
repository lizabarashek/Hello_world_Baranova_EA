device_name = "Микроскоп цифровой"
inventory_number = "INV-2024-156"
is_operational = True
quantity = 3
print("Название прибора\tИнвентарный номер\tСостояние\tКоличество")
print(f"{device_name}\t\t{inventory_number}\t\t{'Исправен' if is_operational else 'Неисправен'}\t{quantity}")