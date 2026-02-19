number_of_capsules=float(input("Введите общее количество произведенных капсул:"))
capsules_per_pack=float(input("Введите количество капсул в одной упаковке:"))

full_packs=number_of_capsules//capsules_per_pack
remaining_capsules=number_of_capsules%capsules_per_pack

print("\n")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t{remaining_capsules}")