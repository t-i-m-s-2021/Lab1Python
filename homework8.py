import logging
from abc import abstractmethod
import time


class Animals:
    def __init__(self, weight, height, age, gender):
        self.weight = weight
        self.height = height
        self.gender = gender
        self.age = age
        self.has_systems_of_organs = True
        self.can_breathing = True
        self.can_move = True
        self.is_heterotroph = True


class Mammals(Animals):
    def __init__(self, weight, height, age, gender):
        super().__init__(weight, height, age, gender)
        self.has_auricles = True
        self.has_wool = True
        self.fed_with_milk = True
        self.has_glands = True

    @abstractmethod
    def make_sound(self):
        """
        Метод должен возвращать звук.
        :returns: sound(str) - звук животного
        """


class Human(Mammals):
    def __init__(self, weight, height, age, gender, name, surname):
        super().__init__(weight, height, age, gender)
        self.name = name
        self.surname = surname
        self.has_mind = True
        self.breathing_with_lungs = True
        self.sound = "SUUUUI"

    def make_sound(self):
        return self.sound


class Cat(Mammals):
    def __init__(self, weight, height, age, gender, nickname):
        super().__init__(weight, height, age, gender)
        self.nickname = nickname
        self.count_legs = 4
        self.has_moustache = True
        self.can_meow_meow = True
        self.__sound = "Meow-Meow"

    def make_sound(self):
        return self.__sound


class Dog(Mammals):
    def __init__(self, weight, height, age, gender, nickname):
        super().__init__(weight, height, age, gender)
        self.nickname = nickname
        self.count_legs = 4
        self.has_moustache = True
        self.can_gav_gav = True
        self.can_execute_commands = True
        self.__sound = "Gav-Gav"

    def make_sound(self):
        return self.__sound


class Student(Human):
    logging.basicConfig(filename="output.txt", level=logging.INFO, filemode="w")

    def __init__(self, weight, height, age, gender, name, surname):
        super().__init__(weight, height, age, gender, name, surname)
        self.count_completed_homeworks = 0

 

    def __eq__(self, other):
        return self.count_completed_homeworks == other.count_completed_homeworks

    def __ne__(self, other):
        return self.count_completed_homeworks != other.count_completed_homeworks

    def __lt__(self, other):
        return self.count_completed_homeworks < other.count_completed_homeworks

    def __le__(self, other):
        return self.count_completed_homeworks <= other.count_completed_homeworks

    def __gt__(self, other):
        return self.count_completed_homeworks > other.count_completed_homeworks

    def __ge__(self, other):
        return self.count_completed_homeworks >= other.count_completed_homeworks
    
    def fib(self, n):
        start = time.time()
        logging.info("""Function "fib" has started""")
        a = b = 1
        for i in range(n):
            if i == n - 2:
                logging.info("""Function "fib" has finished""")
                logging.info("Execution time " + str(time.time() - start))
                return b
            a, b = b, a + b


a = Student(1, 1, 1, 1, 1, 1)
print(a.fib(100000))
