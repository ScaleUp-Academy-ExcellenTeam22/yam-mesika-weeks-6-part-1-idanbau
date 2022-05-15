import time


def timer(function: callable, *args: tuple) -> float:
    """
    :param function:function to calculate the time on execute
    :param args:args to pass to the function which we would like to check
    :return:time it takes for the function to work
    """
    start_time = time.time()
    function(args)
    function_execution_time = (time.time() - start_time)
    return function_execution_time
