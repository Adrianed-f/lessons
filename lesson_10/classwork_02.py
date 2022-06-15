"""
Создать функцию при помощи регулярных выражений для проверки, что строка является валидным телефонным номером в формате
+375 (29) 299-29-29.
"""

import re


def is_mobile_phone(string):
    return re.search(r"^\+\d{3}\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$", string)


def main():
    for item in ("+375 (29) 299-29-29", "+375 (29) 299-29-29"):
        assert is_mobile_phone(item) is not None

    for item in ("(29) 299-29-29", "+375(29)2992929"):
        assert is_mobile_phone(item) is None


if __name__ == "__main__":
    main()
