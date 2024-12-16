import pickle

def read_schedule():
    schedule = {}
    try:
        # Открываем бинарный файл sch.dat для чтения
        with open("sch.dat", "rb") as file:
            schedule = pickle.load(file)  # Загружаем данные из бинарного файла

            # Проверяем, что формат расписания соответствует ожиданиям
            for day, data in schedule.items():
                if isinstance(data, dict):
                    if "active" not in data or "inactive" not in data:
                        raise ValueError(f"Некорректный формат для дня {day}: отсутствуют 'active' или 'inactive'.")
                elif data != "off":
                    raise ValueError(f"Некорректное значение для дня {day}: ожидается 'off' или объект с расписанием.")

    except FileNotFoundError:
        print("Ошибка: файл sch.dat не найден.")
    except pickle.UnpicklingError:
        print("Ошибка: некорректный формат данных в sch.dat.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return schedule


if __name__ == "__main__":
    schedule = read_schedule()
    print(schedule)