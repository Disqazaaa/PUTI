print("Вас приветствует Пути!, куда отправимся сегодня?")

cities = { "Бишкек": {"Ош": 600, "Токмок": 60, "Нарын": 150}, "Ош": {"Бишкек": 600, "Жалал-Абад": 100}, "Токмок": {"Бишкек": 60, "Чуй": 50}, "Нарын": {"Бишкек": 150, "Тамчы": 200}, "Жалал-Абад": {"Ош": 100, "Сулюкта": 80}, "Сулюкта": {"Жалал-Абад": 80, "Кара-Суу": 40}, "Чуй": {"Токмок": 50, "Кара-Балта": 50}, "Кара-Балта": {"Чуй": 50, "Кара-Суу": 90}, "Тамчы": {"Нарын": 200, "Балыкчы": 60}, "Балыкчы": {"Тамчы": 60} }

def show_cities():
    print("\nДоступные города:")
    for city in cities.keys():
        print(city)

def append_city():
    city = input("Какой город вы хотите добавить: ")
    cities[city] = {}
    num_routes = int(input("Сколько городов вы можете посетить из него? "))
    for i in range(num_routes):
        route_data = input("Введите название города назначения и расстояние через двоеточие: ").split(':')
        if len(route_data) != 2:
            print("Что-то пошло не так. Попробуйте снова.")
            continue
        dest, dist = route_data[0], int(route_data[1])
        if dest not in cities:
            print(f"Город {dest} не найден. Добавьте его сначала.")
            continue
        cities[city][dest] = dist
        cities[dest][city] = dist
    print(f"Город {city} успешно добавлен с маршрутами.")

def find_shortest_path():
    print("\nВсе доступные города:", ", ".join(cities.keys()))
    start = input("Введите начальный город: ").strip()
    end = input("Введите конечный город: ").strip()
    if start not in cities or end not in cities:
        print("Один или оба города не найдены.")
        return
    def dfs(graph, start, end, path, visited):
        visited.add(start)
        if start == end:
            return path
        for neighbor in graph[start]:
            if neighbor not in visited:
                new_path = dfs(graph, neighbor, end, path + [neighbor], visited)
                if new_path:
                    return new_path
        return None
    path = dfs(cities, start, end, [start], set())
    if path:
        print(f"Путь от {start} до {end}: {', потом в  '.join(path)}")
    else:
        print(f"Пути от {start} до {end} не существует.")

def start_choise():
    print("\nВыберите действие:")
    print("1  Выход")
    print("2  Отобразить города")
    print("3  Добавить город и маршруты")
    print("4  Найти кратчайший маршрут")
    num = input("Введите номер действия: ")
    if num == "1":
        print("До свидания!")
        return False
    elif num == "2":
        show_cities()
    elif num == "3":
        append_city()
    elif num == "4":
        find_shortest_path()
    else:
        print("Такого нет. Попробуйте снова.")
    return True


continue_program = True
while continue_program:
    continue_program = start_choise()
