import sys


def encode_msg(data):
    return [elem.encode() for elem in data if elem]


def decode_msg(data):
    return [elem.decode() for elem in data if elem]


def encode_ord(word, code):
    return " ".join([str(ord(elem) ^ code) for elem in word])


def task1():
    print("Введите информацию для кодирования")

    input_data = [line.strip() for line in sys.stdin.readlines() if line != "\n"]

    if input_data:
        input_data_byte = encode_msg(input_data)
        print("Закодированная информация:", *input_data_byte, sep="\n")
        print("Декодированная обратно информация:", *decode_msg(input_data_byte), sep="\n")
    else:
        print("Вы ничего не ввели!")


def task2():
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
        count_moleculs = 0

        while True:
            if carbon - 2 >= 0 and hydrogen - 6 >= 0 and oxygen - 1 >= 0:
                carbon -= 2
                hydrogen -= 6
                oxygen -= 1
                count_moleculs += 1
            else:
                break

        f.write(str(count_moleculs))


def task3():

    # в первой строке файла должен лежать ключ, со следующей строки текст
    try:
        with open("input.txt", mode="r", encoding="UTF-8") as f:
            key = f.readline()
            key_byte = int("".join([str(ord(elem)) for elem in key]))
            result = [encode_ord(elem_line, key_byte) for line in f.readlines() for elem_line in line.strip().split()]
    except FileNotFoundError:
        print("Файл не найден!")
        return

    with open("output.txt", mode="w", encoding="UTF-8") as f:
        for msg in result:
            f.write(msg)
            f.write("\n")


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
