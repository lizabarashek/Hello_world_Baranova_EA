array = [64, 34, 23, 5, 22, 27, 90]
n = len(array)
sum_ = 0
i = 0          
count = 0
while i < n:
    if i % 2 == 0:              
        sum_ = sum_ + array[i] 
        count = count + 1
    i = i + 1

if count > 0:
    sr = sum_ / count
else:
    sr = 0

print("Среднее арифметическое элементов с чётными индексами:", sr)