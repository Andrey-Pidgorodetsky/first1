from time import time
from functools import wraps


def speed_test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time=time()
        result=function(*args,**kwargs)
        end_time=time()-start_time
        print(f'Time of code execution {end_time}')
        return result
    return wrapper


@speed_test
def sum_list():
    return sum([number for number in range(100000)])
print(sum_list())

@speed_test
def sum_generator():
    return sum(number for number in range(100000))
print(sum_generator())