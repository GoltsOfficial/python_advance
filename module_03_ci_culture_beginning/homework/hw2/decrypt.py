# decrypt.py

"""
Модуль для расшифровки строки, в которой используется точка как разделитель.
Функция decrypt удаляет последовательности из двух точек, которые следуют подряд.
"""

import sys


def decrypt(encryption: str) -> str:
    """
    Функция принимает строку, содержащую зашифрованный текст, и возвращает расшифрованный текст.
    Последовательности из двух точек удаляются.

    :param encryption: зашифрованный текст
    :return: расшифрованный текст
    """
    result: list = []
    dots: int = 0
    for symbol in encryption:
        if symbol != '.':
            result.append(symbol)
            dots = 0
            continue

        dots += 1
        if dots == 2 and result:
            result.pop()
            dots = 0

    return ''.join(result)


if __name__ == '__main__':
    data: str = sys.stdin.read()
    decryption: str = decrypt(data)
    print(decryption)
