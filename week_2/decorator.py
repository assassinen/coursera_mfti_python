import functools

# декоратор это функция, которая получает функцию и возвращает функцию

def decorator(func):
    @functools.wraps(func)
    def new_func():
        print("buy")
    return new_func

@decorator
def decorated():
    print("Hello")


decorated()
print(decorated.__name__)
# decorated = decorator(decorated)
# decorated()

