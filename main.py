import modules as auto
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

# Первая функция START
def start_B8():
    print(f"START выполнен | Время: {datetime.now()}")
    auto.activate_window("Station")
    auto.activate_login_window(31, 35, 54, 92)
    auto.login(980, 529, 931, 559, "12345")
    auto.move_to_P8(1083, 60)
    auto.start_P8(1290, 240)
    auto.move_to_main(516, 61)
    auto.move_away(800, 600)
    auto.activate_login_window(31, 35, 54, 92)

# Вторая функция STOP
def stop_B8():
    print(f"STOP выполнен | Время: {datetime.now()}")
    auto.activate_window("Station")
    auto.activate_login_window(31, 35, 54, 92)
    auto.login(980, 529, 931, 559, "12345")
    auto.move_to_P8(1083, 60)
    auto.stop_P8(1290, 267)
    auto.move_to_main(516, 61)
    auto.move_away(800, 600)
    auto.activate_login_window(31, 35, 54, 92)

# Чтение расписания из файла
def read_schedule():
    schedule = {}
    try:
        with open("schedule.txt", "r") as file:
            for line in file:
                task, time_value = line.strip().split(": ")
                schedule[task] = [int(x) for x in time_value.split(":")]
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return schedule


# Настраиваем планировщик
scheduler = BackgroundScheduler()


# Функция для обновления заданий в планировщике
def update_jobs():
    schedule = read_schedule()

    # Удаляем существующие задания
    scheduler.remove_all_jobs()

    # Добавляем новые задания из файла
    if "Active" in schedule:
        scheduler.add_job(
            start_B8,
            'cron',
            day_of_week='mon-fri',
            hour=schedule["Active"][0],
            minute=schedule["Active"][1],
            second=schedule["Active"][2],
        )
        print(f"Добавлено задание start_B8: {schedule['Active']}")

    if "Inactive" in schedule:
        scheduler.add_job(
            stop_B8,
            'cron',
            day_of_week='mon-fri',
            hour=schedule["Inactive"][0],
            minute=schedule["Inactive"][1],
            second=schedule["Inactive"][2],
        )
        print(f"Добавлено задание stop_B8: {schedule['Inactive']}")


# Первоначальная настройка заданий
update_jobs()

# Запуск планировщика
scheduler.start()

print("Планировщик запущен. Ожидание...")
try:
    # Поддерживаем работу программы
    while True:
        time.sleep(360)  # Проверяем расписание каждые 60 секунд
        update_jobs()  # Обновляем задания, если файл изменился
except (KeyboardInterrupt, SystemExit):
    # Корректная остановка планировщика
    scheduler.shutdown()
    print("Планировщик остановлен.")