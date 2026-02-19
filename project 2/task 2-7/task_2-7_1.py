files = ["seq1", "seq2", "seq3", "seq4"]
date = "02.12.2026" 

for name in files:

   new_name = name + "_" + date + ".fasta"

   print(f"{new_name}")
