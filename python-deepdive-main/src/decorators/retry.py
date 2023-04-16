import random
import time
from functools import wraps

def retry(num_retries, exception_to_check, sleep_time=0):
    """
    Decorator that retries the execution of a function if it raises a specific exception.
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, num_retries+1):
                try:
                    return func(*args, **kwargs)
                except exception_to_check as e:
                    print(f"{func.__name__} raised {e.__class__.__name__}. Retrying...")
                    if i < num_retries:
                        time.sleep(sleep_time)
            # Raise the exception if the function was not successful after the specified number of retries
            raise e
        return wrapper
    return decorate

@retry(num_retries=3, exception_to_check=ValueError, sleep_time=1)
def random_value():
    value = random.randint(1, 5)
    if value == 3:
        raise ValueError("Value cannot be 3")
    return value

random_value()
# random_value raised ValueError. Retrying...
# 1

random_value()
# 5