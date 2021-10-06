# Напишите декоратор, замеряющий время выполнения функции. Декоратор должен вывести на экран время выполнения задекорированной функции
import time

def my_decorator(outer_func):
    def the_wrapper():
        print('Кусок кода до функции')
        start_time = time.time()
        outer_func()
        print('Кусок кода после функции')
        print(f'function executed for  {time.time() - start_time} seconds')
    return the_wrapper()
@my_decorator
def outer_func():
    for i in range(100000):
        print('Hello, Teacher')

