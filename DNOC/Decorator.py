import time

# 装饰器
# 使用方法:
# 1.在想要计时的方法上添加依赖@timekeeping
# 2.打开is_Timekeeping = True
# 注意,计时行为同样也耗时,所以在结束计时后请撤回以上操作

# 是否计时
is_Timekeeping = False
# 统计时间
statisticalTime = {}


# 计时
def timekeeping(func):
    def method(*args, **kwargs):
        if is_Timekeeping:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            if func.__name__ not in statisticalTime:
                statisticalTime[func.__name__] = 0
            statisticalTime[func.__name__] += end_time - start_time
            return result
        return func(*args, **kwargs)
    return method


# 输出所有统计时间
def print_statistical_time():
    for key, value in statisticalTime.items():
        print(key + "耗时:" + str(value))
