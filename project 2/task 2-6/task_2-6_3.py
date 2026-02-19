phenotype_donor = input("Введите фенотип группы крови (A, B, AB, O): ").strip().upper()
phenotype_recepient = input("Введите фенотип группы крови (A, B, AB, O):").strip().upper()
if phenotype_donor == phenotype_recepient or phenotype_donor == "O":
    print("Разрешено переливание")
else:
    print("Переливание запрещено")