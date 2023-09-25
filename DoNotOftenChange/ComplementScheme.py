from OftenChange import Configuration as C
from OftenChange.Recursion import Calculate, get_difference_sum, generate_content


# 羁绊补全方案
class ComplementScheme(Calculate):
    def Method(self):
        self.circulation(self.initialIndexes, 0)
        # print(self.currentOptimal)
        print(*self.currentOptimal, sep="\n")

    # 当前最优
    # currentOptimal[0]为最优解所缺失的羁绊数
    currentOptimal = [10, ]

    def advance_judge(self, nest):
        return True

    def last_step(self):
        # 去重
        if len(C.r_database) != len(set(C.r_database)):
            return 0
        # 必须羁绊筛选
        for key, value in C.must_fetter.items():
            if C.fetter_data[key] < value:
                return 0
        # 计算羁绊缺失数
        difference_sum = get_difference_sum(self.currentOptimal[0])
        # 判断是加入还是代替
        if difference_sum == self.currentOptimal[0]:
            self.currentOptimal.append(generate_content())
        else:
            if difference_sum < self.currentOptimal[0]:
                self.currentOptimal = [difference_sum, generate_content()]
