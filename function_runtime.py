import time


def timer(f, *args):
    """
    :param f:function to calculate the time on execute
    :param args:args to pass to the function which we would like to check
    :return:time it takes for the function to work
    """
    start_time = time.time()
    f(args)
    function_execution_time = (time.time() - start_time)
    return function_execution_time
