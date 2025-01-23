n = int(input("Введите количество интервалов: "))  
intervals = []

for i in range(n):
    start, end = map(int, input(f"Введите начало и конец интервала {i+1} через пробел: ").split())
    intervals.append([start, end])

print("\nВы ввели интервалы:")
for interval in intervals:
    print(f"Интервал: {interval[0]} -> {interval[1]}")