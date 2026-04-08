people = [    #1
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Alice", "age": 22},
    {"name": "Charlie", "age": 30}
]

sorted_people = sorted(people, key=lambda x: (x["name"], -x["age"]))

print(sorted_people)


import random  #2

numbers = [random.randint(5, 20) for _ in range(10)]
print("Список чисел:", numbers)

if all(n > 10 for n in numbers):
    sorted_numbers = sorted(numbers)
    print("Всі числа > 10, відсортований список:", sorted_numbers)
else:
    print("Не всі числа > 10")