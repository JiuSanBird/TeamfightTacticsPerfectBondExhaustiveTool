from OC import Configuration as C
from OC.Recursion import Calculate, generate_content


def get_difference_sum(tolerate):
    difference_sum = 0
    for i in range(1, len(C.fetter_data)):
        # 有此羁绊
        if C.fetter_data[i] != 0:
            for l in range(1, len(C.fetter_database[i])):
                difference = C.fetter_database[i][l] - C.fetter_data[i]
                if difference == 0:
                    break
                else:
                    if difference > 0:
                        if l == 1:
                            difference_sum += C.fetter_data[i]
                        else:
                            difference_sum += C.fetter_data[i] - C.fetter_database[i][l - 1]
                        # 已经无法容忍,直接返回
                        if difference_sum > tolerate:
                            return difference_sum
                        break
    return difference_sum


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
