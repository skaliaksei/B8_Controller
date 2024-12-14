import modules as auto
import file_working
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
import json

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

# Настраиваем планировщик
scheduler = BackgroundScheduler()


# Функция для обновления заданий в планировщике
def update_jobs():
    # Чтение расписания из файла:
    schedule = file_working.read_schedule()

    # Удаляем существующие задания
    scheduler.remove_all_jobs()

    # Добавляем новые задания на основе расписания
    for day, data in schedule.items():
        if data == "off":
            print(f"{day}: Вентсистема выключена на весь день.")
            continue

        active_time = list(map(int, data["active"].split(':')))
        inactive_time = list(map(int, data["inactive"].split(':')))

        # Задание на включение системы
        scheduler.add_job(
            start_B8,
            'cron',
            day_of_week=day,
            hour=active_time[0],
            minute=active_time[1],
            second=0,
        )
        print(f"Добавлено задание start_B8 для {day}: {data['active']}")

        # Задание на выключение системы
        scheduler.add_job(
            stop_B8,
            'cron',
            day_of_week=day,
            hour=inactive_time[0],
            minute=inactive_time[1],
            second=0,
        )
        print(f"Добавлено задание stop_B8 для {day}: {data['inactive']}")


# Первоначальная настройка заданий
update_jobs()

# Запуск планировщика
scheduler.start()

print("Планировщик запущен. Ожидание...")
try:
    # Поддерживаем работу программы
    while True:
        time.sleep(300)  # Проверяем расписание каждые 5 минут
        update_jobs()  # Обновляем задания, если файл изменился
except (KeyboardInterrupt, SystemExit):
    # Корректная остановка планировщика
    scheduler.shutdown()
    print("Планировщик остановлен.")