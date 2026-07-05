# создаем словарь
contacts = {}

# Цикл управления телефонной книгой
while True:
    command = input("Команда (добавить/показать/найти/удалить/выход): ").lower()

    if command == "выход": # обработка 'выход'
        print("Пока!")
        break # останавливаем цикл

    elif command == "добавить": # обрабатка 'добавить'
        add_name = input("Введите имя контакта: ") # запрашиваем имя
        if add_name in contacts.keys(): # проверяем наличие имени
            print(f"Имя '{add_name}' занято, попробуйте другое.")
        else:
            contacts[add_name] = input("Введите номер: ")
            print(f"Контакт '{add_name}' сохранен.")

    elif command == "показать": # обработка 'показать'
        if len(contacts) == 0: # проверяем, есть ли данные в словаре
            print("Телефонная книга пуста.")
        else:
            # перебераем ключи и значения в словаре и выводим на экран
            print("Список контактов:")
            for key, value in contacts.items():
                print(f"{key} - {value}")

    elif command == "найти": # обработка 'найти'
        if len(contacts) == 0: # проверяем, есть ли данные в словаре
            print("Телефонная книга пуста.")
        else:
            search_name = input("Введите имя для поиска: ") # запрашиваем имя для поиска
            print(contacts.get(search_name, "Контакт не найден.")) # получаем значение по ключу

    elif command == "удалить": # обработка 'удалить'
        if len(contacts) == 0: # проверяем, есть ли данные в словаре
            print("Телефонная книга пуста.")
        else:
            # перебераем ключи и значения в словаре и выводим на экран
            print("Список контактов:")
            for key, value in contacts.items():
                print(f"{key} - {value}")
            print()
            del_name = input("Введите имя контакта, который хотите удалить: ") # запрашиваем имя для удаления
            if del_name not in contacts.keys(): # проверка имени
                print("Имя не существует.")
            else:
                phone = contacts.pop(del_name)
                print(f"Контакт '{del_name}' с номером '{phone}' удален.")
                
    else:
        print("Неверная команда.")
            