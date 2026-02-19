dna = input("Введите последовательность ДНК:")
DNA = dna.upper()

count_A = DNA.count("A")
count_T = DNA.count("T")
count_G = DNA.count("G")
count_C = DNA.count("C")

total_length = len(DNA)

print("Подсчёт нуклеотидов:")
print(f"A: {count_A}")  

print(f"T: {count_T}")

print(f"G: {count_G}")

print(f"C: {count_C}")

print(f"Общая длина: {total_length} нуклеотидов")

print("\nПроцентное содержание:")
print(f"A: {(count_A / total_length * 100):.1f}%")
print(f"T: {(count_T / total_length * 100):.1f}%")
print(f"G: {(count_G / total_length * 100):.1f}%")
print(f"C: {(count_C / total_length * 100):.1f}%")