# создаем список задач
tasks = []

# Цикл управления списком
while True:
    command = input("Команда (добавить/показать/удалить/выход): ").lower()

    if command == "выход":
        print("Пока.")
        break # выходим из цикла
    elif command == "добавить":
        added = input("Какую задачу хотите добавить? ") # запрашиваем задачу, которую необходимо добавит
        tasks.append(added) # добавляем задачу
        print(f"Задача '{added}' добавлена!")
    elif command == "удалить":
        if len(tasks) == 0: # проверяем, есть ли данные в списке
            print("Список пуст.")
        else:
            # показываем список
            for index, item in enumerate(tasks):
                print(f"{index + 1}. {item}")
            
            print()
            number = int(input("Введите номер задачи для удаления: ")) # запрашиваем номер задачи
            
            if number < 1 or number > len(tasks): # проверяем наличе номера задачи
                print("Задачи с таким номером нет.")
            else:
                removed = tasks.pop(number - 1) # удаляем значение и присваеваем его переменной
                print(f"Задача '{removed}' удалена!") # выводим удаленное значение
    elif command == "показать":
        if len(tasks) == 0:
            print("Список пуст.")
        else:
            print("Список задач: ")
            # перебераем список задач
            for index, item in enumerate(tasks):
                print(f"{index + 1}. {item}") 
    else:
        print(f"Команды {command} не существует")