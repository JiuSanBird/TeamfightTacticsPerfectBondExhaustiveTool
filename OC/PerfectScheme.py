from DNOC.Decorator import timekeeping
from OC import Configuration as C
from OC.Recursion import Calculate, generate_content, get_difference_sum


# 完美羁绊方案
class PerfectScheme(Calculate):
    # 在未满足8人口时就进行判决判断 耗时约89秒
    # 效率提高85%
    # 击毙了约99.93%的情况
    def advance_judge(self, nest):
        # *** 至高天
        # if fetter_data[26] != 0:
        #     return True
        # else:

        # 59组合数量(长度为6): 45057474(4千万)
        # 59组合数量(长度为7): 341149446(3亿)
        # 59组合数量(长度为8): 2217471399(22亿)
        # 6 468.44秒          5 430.34秒 4 458.05秒
        # 3 422.98秒 540.15秒 2 513.93秒 1 2829.21秒
        return nest < (C.population - 3) or \
            (nest == (C.population - 3) and self.advance_judge_method(nest)) or \
            (nest == (C.population - 2) and self.advance_judge_method(nest)) or \
            (nest == (C.population - 1) and self.advance_judge_method(nest))

    # 提前预判
    @timekeeping
    def advance_judge_method(self, nest):
        tolerate = (C.population - nest) * 3
        return get_difference_sum(tolerate) <= tolerate

    def last_step(self):
        # 初步排查掉羁绊浪费的阵容
        for i in range(1, len(C.fetter_data)):
            if C.fetter_data[i] != 0:
                # 有此羁绊时
                if C.fetter_data[i] not in C.fetter_database[i]:
                    return 0
        content = generate_content()
        self.solution.solution(content)
