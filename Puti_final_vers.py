print("Вас приветствует Пути!, куда отправимся сегодня?")

cities = { "Бишкек": {"Ош", "Токмок", "Нарын"}, "Ош": {"Бишкек", "Жалал-Абад"}, "Токмок": {"Бишкек", "Чуй"}, "Нарын": {"Бишкек", "Тамчы"}, "Жалал-Абад": {"Ош", "Сулюкта"}, "Сулюкта": {"Жалал-Абад", "Кара-Суу"}, "Чуй": {"Токмок", "Кара-Балта"}, "Кара-Балта": {"Чуй", "Кара-Суу"}, "Тамчы": {"Нарын", "Балыкчы"}, "Балыкчы": {"Тамчы"} }

def show_cities():
    print("\nДоступные города:")
    for city in cities.keys():
        print(city)

def append_city():
    city = input("Какой город вы хотите добавить: ").strip()
    cities[city] = set()
    num_routes = int(input("Сколько городов вы можете посетить из него? "))
    for _ in range(num_routes):
        dest = input("Введите название города назначения: ").strip()
        if dest not in cities:
            print(f"Город {dest} не найден. Добавьте его сначала.")
            continue
        cities[city].add(dest)
        cities[dest].add(city)
    print(f"Город {city} успешно добавлен с маршрутами.")

def find_shortest_path():
    print("\nВсе доступные города:", ", ".join(cities.keys()))
    start = input("Начало пути, город: ").strip()
    end = input("Конец пути, город: ").strip()
    if start not in cities or end not in cities:
        print("города не найдены.")
        return

    def bfs(graph, start, end):
        queue = [(start, [start])]
        visited = set()
        while queue:
            current, path = queue.pop(0)
            if current ==end:
                return path
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return None

    path = bfs(cities, start, end)
    if path:
        print(f"Кратчайший путь от {start} до {end}: {', потом в '.join(path)}")
    else:
        print(f"Пути от {start} до {end} не существует.")

def start_choice():
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
        print("Такого действия нет. Попробуйте снова.")
    return True

continue_program = True
while continue_program:
    continue_program = start_choice()