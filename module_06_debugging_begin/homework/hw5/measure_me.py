"""
Каждый лог содержит в себе метку времени, а значит, правильно организовав логирование,
можно отследить, сколько времени выполняется функция.

Программа, которую вы видите, по умолчанию пишет логи в stdout. Внутри неё есть функция measure_me,
в начале и в конце которой пишется "Enter measure_me" и "Leave measure_me".
Сконфигурируйте логгер, запустите программу, соберите логи и посчитайте среднее время выполнения функции measure_me.
"""
import logging
import random
import time
from typing import List
from datetime import datetime

logger = logging.getLogger(__name__)

def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")

def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(f"Appended {[nums[i], nums[left], nums[right]]} to result")
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1

    logger.debug("Leave measure_me")
    return results


if __name__ == "__main__":
    # Конфигурация логгера с метками времени до миллисекунд
    logging.basicConfig(
        filename="measure_me.log",
        filemode="w",
        encoding="utf-8",
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d - %(message)s",  # Формат с миллисекундами
        datefmt="%Y-%m-%d %H:%M:%S",  # Формат даты и времени
    )

    for it in range(3):
        data_line = get_data_line(10 ** 3)
        measure_me(data_line)


    def parse_log_file(file_path):
        start_times = []
        end_times = []

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if "Enter measure_me" in line:
                    start_time_str = line.split(' - ')[0]
                    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S.%f")
                    start_times.append(start_time)
                elif "Leave measure_me" in line:
                    end_time_str = line.split(' - ')[0]
                    end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S.%f")
                    end_times.append(end_time)

        durations = [(end - start).total_seconds() for start, end in zip(start_times, end_times)]
        average_duration = sum(durations) / len(durations) if durations else 0
        print(f"Среднее время выполнения функции measure_me: {average_duration:.6f} секунд")

    parse_log_file("measure_me.log")