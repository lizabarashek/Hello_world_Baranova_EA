number = 1  
sum_even = 0  

while number <= 15:
    if number % 2 == 0:
        sum_even += number
    number += 1
print(f"Сумма всех чётных чисел от 1 до 15: {sum_even}")