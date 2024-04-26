def print_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper


@print_decorator
def hello():    
    print("Hello, World!")
    
hello()