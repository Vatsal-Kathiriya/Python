import logging

def log_function_decorator(func):
    def wrapper(*args , **kwargs):
        logging.info(f"Calling {func.__name__} with {args} and {kwargs}")
        # print(logging.info(f"Calling {func.__name__} with {args} and {kwargs}"))
        result = func(*args , **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        # print(logging.info(f"{func.__name__} returned {result}"))
        return result
    return wrapper

@log_function_decorator
def my_func(a , b):
    return a + b

s = my_func(1 , 2)
print(s)
print(__name__)