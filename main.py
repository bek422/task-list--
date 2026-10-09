tasks = []  # Список для хранения задач

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
        if not tasks:
            print("Список пуст.")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
            
    elif choice == "3":
        if not tasks:
            print("Список задач пуст, удалять нечего.")
            continue
        try:
            num = int(input("Введите номер задачи для удаления: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Задача '{removed}' успешно удалена!")
            else:
                print("Задачи с таким номером нет в списке.")
        except ValueError:
            print("Пожалуйста, введите число (номер задачи).")
            
    elif choice == "4":
        print("Выход из программы. До свидания!")
        break
    else:
        print("Неверный пункт. Выберите от 1 до 4.")
