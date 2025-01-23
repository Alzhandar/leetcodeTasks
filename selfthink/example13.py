l = list(map(int, input().split()))
gold = 'Gold Medal'
silver = 'Silver Medal'
bronze = 'Bronze Medal'

# Создадим список индексов, отсортированных по значению из списка l (по убыванию)
sorted_indices = sorted(range(len(l)), key=lambda i: l[i], reverse=True)

# Присвоим медали
medals = [''] * len(l)
if len(sorted_indices) > 0:
    medals[sorted_indices[0]] = gold  # Золотая медаль
if len(sorted_indices) > 1:
    medals[sorted_indices[1]] = silver  # Серебряная медаль
if len(sorted_indices) > 2:
    medals[sorted_indices[2]] = bronze  # Бронзовая медаль

# Вывод результатов
print("Список медалей:", medals)