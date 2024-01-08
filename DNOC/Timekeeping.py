import time
from DNOC.Agency import Agency


# 计时
class Timekeeping(Agency):
    def __init__(self, next):
        self.next = next

    def Method(self):
        start_time = time.time()
        self.next.Method()
        end_time = time.time()
        # 单循环C(59,8)就要124秒,所以必须要剪枝
        # C(59,8): 2217471399(22亿)
        # 8238.46秒 4142.29秒 3164.75秒 2637.47秒 2510.47秒 585.15秒 220.16秒 135.24秒 123.77秒 92.38秒 37.18秒 31.87秒 26.04秒
        print("\n总耗时: {:.2f}秒".format(end_time - start_time))
