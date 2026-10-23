file = open('numbers.txt')
result = open('result.txt', 'w')
numbers = []
for num in file:
    try:
        numbers.append(int(num))
    except ValueError:
        pass

if numbers:
    result.write(f'Минимальное значение: {min(numbers)}\n')
    result.write(f'Максимальное значение: {max(numbers)}\n')
    result.write(f'Среднее арифметическое: {sum(numbers)/len(numbers)}\n')
else:
    result.write('В файле нет чисел')