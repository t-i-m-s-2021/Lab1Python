import os
import numpy as np
import pprint
from helpers import get_random_sym_from_str

print("Текущее имя системы: {}".format(os.name))
print("Текущее имя системы: {}".format(os.environ["OS"]))

pprint.pprint(list(os.environ.items()))

print("Текущее имя пользователя: {}".format(os.environ["USERNAME"]))
print("Текущее имя пользователя: {}".format(os.getlogin()))

for elem in os.walk(os.getcwd()):
    print("В папке(абсолютный путь)", elem[0])
    print("Содержатся папки:", *elem[1], sep=" ")
    print("Содержатся файлы:", *elem[2], sep=" ")

a = np.random.randint(0, 10, (3, 3))
print(a)
print(a.transpose())
print(get_random_sym_from_str("Hello!"))
