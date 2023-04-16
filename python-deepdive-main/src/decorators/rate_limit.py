import time
from functools import wraps

def rate_limited(max_per_second):
    min_interval = 1.0 / float(max_per_second)
    def decorate(func):
        last_time_called = 0.0
        @wraps(func)
        def rate_limited_function(*args, **kargs):
            elapsed = time.perf_counter() - last_time_called
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kargs)
            last_time_called = time.perf_counter()
            return ret
        return rate_limited_function
    return decorate


from ratelimit import limits

import requests

FIFTEEN_MINUTES = 900

@sleep_and_retry
@limits(calls=15, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response
