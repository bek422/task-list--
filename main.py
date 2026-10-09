tasks = []

while True:
    print("\n--- МЕНЮ ---")
    print("1. Добавление задачи")
    print("2. Вывод списка задач")
    print("3. Удаление задачи")
    print("4. Выход из программы")
    
    choice = input("Выберите пункт меню: ")
    
    if choice == "1":
        task = input("Введите текст задачи: ")
        tasks.append(task)
        print("Задача успешно добавлена!")
    elif choice == "2":
        print("\nВаш список задач:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    elif choice == "3":
        print("Ошибка: Функция удаления ещё не реализована!")
    elif choice == "4":
        print("Выход из программы. До свидания!")
        break
    else:
        print("Неверный пункт. Выберите от 1 до 4.")
