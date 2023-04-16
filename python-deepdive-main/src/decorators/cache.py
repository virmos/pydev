from functools import wraps

def cache(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key in wrapper.cache:
            output = wrapper.cache[cache_key]
        else:
            output = function(*args)
            wrapper.cache[cache_key] = output
        return output
    wrapper.cache = dict()
    return wrapper

@cache
def heavy_processing(n):
    sleep_time = n + random.random()
    time.sleep(sleep_time)

%%time
heavy_processing(1)
# CPU times: user 446 µs, sys: 864 µs, total: 1.31 ms
# Wall time: 1.06 s

%%time
heavy_processing(1)
# CPU times: user 11 µs, sys: 0 ns, total: 11 µs
# Wall time: 13.1 µs
