# создаем список задач
tasks = []

# Цикл управления списком
while True:
    command = input("Команда (добавить/показать/удалить/выход): ").lower()

    if command == "выход":
        print("Пока.")
        break # выходим из цикла
    elif command == "добавить":
        tasks.append(input("Какую задачу хотите добавить? ")) # добавляем задачу ввенденую пользователем
    elif command == "удалить":
        number = int(input("Введите номер задачи для удаления: ")) # запрашиваем номер задачи
        removed = tasks.pop(number - 1)
        print(f"Задача '{removed}' удалена!")
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