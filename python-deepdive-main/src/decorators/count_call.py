from functools import wraps

def countcall(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'{func.__name__} has been called {wrapper.count} times')
        return result
    wrapper.count = 0
    return wrapper

@countcall
def process_data():
    pass

process_data()
process_data has been called 1 times
process_data()
process_data has been called 2 times
process_data()
process_data has been called 3 times
