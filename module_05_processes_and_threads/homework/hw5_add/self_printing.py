"""
Напишите код, который выводит сам себя.
Обратите внимание, что скрипт может быть расположен в любом месте.
"""

import sys

result = 0
for n in range(1, 11):
    result += n ** 2

# Secret magic code
# Выводим код, включая магический комментарий
with(open(sys.argv[0], 'r', encoding='utf-8')) as f:
    print(f.read())