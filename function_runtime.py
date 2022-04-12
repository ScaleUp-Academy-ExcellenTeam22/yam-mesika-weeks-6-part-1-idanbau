import time


def timer(f, *args):
    start_time = time.time()
    f(args)
    function_execution_time = (time.time() - start_time)
    return function_execution_time
