print("Привет!")
name = input("Как тебя зовут? ")
color = input("Какой твой любимый цвет? ")
number = input("Какое твое любимое число? ")

print()
print(f"Твой обычный никнейм: {name}_{color}_{number}")

print()
print(f"Сверх-секретный никнейм: {name}_{color}_{int(number) * 2}")