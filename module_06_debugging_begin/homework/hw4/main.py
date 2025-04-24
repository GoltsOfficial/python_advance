"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
import json
from typing import Dict, Counter


def load_logs(file_path='skillbox_json_messages.log') -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        return [json.loads(line) for line in file]

def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    logs = load_logs()
    level_counter = Counter(log['level'] for log in logs)
    return dict(level_counter)


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    logs = load_logs()
    hours = [log['time'] for log in logs]
    hour_counter = Counter(hours)
    most_common = hour_counter.most_common[1][0][0]
    return int(most_common)


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    logs = load_logs()
    critical_logs = [log['critical'] for log in logs if log['level'] == 'CRITICAL']
    critical_counter_in_period = sum(5 <= int(log['time'][:2]) < 6
                           and log['time'][3:5] <= '20'
                           for log in critical_logs)
    return int(critical_counter_in_period)


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    pass


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    pass


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
