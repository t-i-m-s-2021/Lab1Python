import logging
import time

logging.basicConfig(level=logging.INFO, filename="output.txt", filemode="w")
logger = logging.getLogger("fib_logger")


def logger_func(func):
    def wrap_func(*args):
        logger.info("""Function "fib" has started""")
        start = time.time()
        time.sleep(2)
        result = func(*args)
        logger.info("Result: {}".format(result))
        logger.info("""Function "fib" has finished""")
        logger.info("Execution time " + str(time.time() - start))
        return result

    return wrap_func


@logger_func
def fib(n):
    a = b = 1
    for i in range(n):
        if i == n - 2:
            return b
        a, b = b, a + b


print(fib(100))
