#1
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "black": (0, 0, 0)
}

color = input("Введіть назву кольору: ").lower()

if color in colors:
    print("RGB код:", colors[color])
else:
    print("Колір не знайдено")

#2
students = {
    "Іваненко": 5,
    "Петренко": 3,
    "Сидоренко": 4,
    "Коваленко": 2,
    "Шевченко": 5
}

good_students = {name: grade for name, grade in students.items() if grade >= 4}

print("Учні з оцінками 4 та 5:", good_students)

#3
weather = {
    "Київ": 18,
    "Львів": 16,
    "Одеса": 22,
    "Харків": 19
}

cities_input = input("Введіть міста через кому: ")
cities = [city.strip() for city in cities_input.split(",")]

total = 0
count = 0
for city in cities:
    if city in weather:
        total += weather[city]
        count += 1

if count > 0:
    average = total / count
    print("Середня температура:", average)
else:
    print("Міста не знайдено")