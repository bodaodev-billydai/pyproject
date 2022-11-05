
def monitor_function(*margs,**margk):
    def wrapper(fn):
        def innerwrapper(*args, **argk):
            input1 = [*args]
            if 'ignore_self' in margk and margk['ignore_self' ]:
                input1 = input1[1:]
            input2 = {**argk}
            result = fn(*args, **argk)
            print(input1, input2, result)
            return result
        return innerwrapper
    return wrapper