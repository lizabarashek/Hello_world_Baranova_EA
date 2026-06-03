array = [64, 34, 23, 5, 22, 27, 90]
n = len(array)
sum_ = 0
i = 0
while i < n:
    sum_ = sum_ + array[i]
    i = i + 1
sr = sum_ / n
print("Среднее арифметическое элементов массива:", sr)