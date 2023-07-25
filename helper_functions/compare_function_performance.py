from time import time


def performance(fn):
    def wrapper (*args, **kwargs):
        start_time = time()
        result = fn (*args, **kwargs)
        end_time = time()
        print(f"Time taken by the function is {end_time - start_time} seconds")
        return result
    return wrapper
