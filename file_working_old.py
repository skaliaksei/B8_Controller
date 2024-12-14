import json

def read_schedule():
    schedule = {}
    try:
        # Открываем файл sch.json для чтения
        with open("sch.json", "r") as file:
            schedule = json.load(file)  # Загружаем данные из JSON файла

            # Проверяем, что формат расписания соответствует ожиданиям
            for day, data in schedule.items():
                if isinstance(data, dict):
                    if "active" not in data or "inactive" not in data:
                        raise ValueError(f"Некорректный формат для дня {day}: отсутствуют 'active' или 'inactive'.")
                elif data != "off":
                    raise ValueError(f"Некорректное значение для дня {day}: ожидается 'off' или объект с расписанием.")

    except FileNotFoundError:
        print("Ошибка: файл sch.json не найден.")
    except json.JSONDecodeError:
        print("Ошибка: некорректный JSON в sch.json.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return schedule

if __name__ == "__main__":
    schedule = read_schedule()
    print(schedule)