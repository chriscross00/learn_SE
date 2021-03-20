import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


num1 = 10
num2 = 5

add_result = add(num1, num2)
logging.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

subtract_result = subtract(num1, num2)
logging.debug(': {} + {} = {}'.format(num1, num2, subtract_result))
