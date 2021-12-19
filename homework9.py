def delete_duplicates(data: list) -> list:
    """
    Функция удаляет повторяющиеся элементы в списке.
    :param data: список с данными
    :return: список с данными без дублей
    """
    if not data:
        return []

    return list(set(data))


def count_chars(s: str) -> dict:
    """
    Считает вхождение каждого элемента в строку.
    :param s: входная строка
    :return: словарь с подсчетом каждого элемента в строке
    """
    return {elem: s.count(elem) for elem in s}


def check_molecules() -> None:
    try:
        with open("input.txt", mode="r", encoding="UTF-8") as f:
            try:
                carbon, hydrogen, oxygen = [int(elem) for elem in f.read().split()]
            except ValueError:
                print("Некорректный ввод из файла!")
                return
    except FileNotFoundError:
        print("Файл не найден!")
        return

    with open("output.txt", mode="w", encoding="UTF-8") as f:
        count_molecules = 0

        while True:
            if carbon - 2 >= 0 and hydrogen - 6 >= 0 and oxygen - 1 >= 0:
                carbon -= 2
                hydrogen -= 6
                oxygen -= 1
                count_molecules += 1
            else:
                break

        f.write(str(count_molecules) if count_molecules else "Impossible")
