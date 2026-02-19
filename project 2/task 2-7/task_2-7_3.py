seq = ["ATATACGCGTA", "CTTCGGNGGA"]

for a, sequence in enumerate(seq, 1):
    print(f"\nПоследовательность {a} целиком: {sequence}")
    print("Построчно:")
    
    for b, nucleotide in enumerate(sequence, 1):
        print(f"Позиция {b}: {nucleotide}")
    
    print("-" * 30)

print("Цикл выполнен")