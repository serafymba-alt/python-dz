import csv
import numpy as np
import matplotlib.pyplot as plt
import os

csv_filename = 'data_files.csv'

if not os.path.exists(csv_filename):
    print(f"Помилка: файл '{csv_filename}' не знайдено в папці {os.getcwd()}")
    exit()


months = []
sales = []

with open(csv_filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        months.append(row['Month'])
        sales.append(float(row['Sales']))

# ====== Статистика ======
sales_array = np.array(sales)
mean_val = np.mean(sales_array)
median_val = np.median(sales_array)
max_val = np.max(sales_array)
min_val = np.min(sales_array)
std_val = np.std(sales_array)

print("Середнє:", mean_val)
print("Медіана:", median_val)
print("Максимум:", max_val)
print("Мінімум:", min_val)
print("Стандартне відхилення:", std_val)

# ====== Висновки ======
print("\nВисновки:")
print(f"Середнє показує, що в середньому продажі складають {mean_val:.2f} одиниць.")
print(f"Медіана {median_val:.2f} показує типовий рівень продажів без впливу аномалій.")
print(f"Різниця між мінімумом ({min_val}) і максимумом ({max_val}) показує коливання продажів.")
print(f"Стандартне відхилення {std_val:.2f} говорить про стабільність продажів.")

# ====== Графік ======
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title("Продажі по місяцях")
plt.xlabel("Місяць")
plt.ylabel("Продажі")
plt.grid(True)
plt.show() 
 
