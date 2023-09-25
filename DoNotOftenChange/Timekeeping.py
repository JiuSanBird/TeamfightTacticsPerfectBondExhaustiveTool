import time
from DoNotOftenChange.Agency import Agency


# 计时
class Timekeeping(Agency):
    def __init__(self, next):
        self.next = next

    def Method(self):
        start_time = time.time()
        self.next.Method()
        end_time = time.time()
        # 8238.46秒 4142.29秒 3164.75秒 2637.47秒 2510.47秒 585.15秒 220.16秒 135.24秒 123.77秒 92.38秒
        print("\n总耗时: {:.2f}秒".format(end_time - start_time))
