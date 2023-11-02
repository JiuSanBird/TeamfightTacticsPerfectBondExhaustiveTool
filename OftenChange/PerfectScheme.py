from DoNotOftenChange.Decorator import timekeeping
from OftenChange import Configuration as C
from OftenChange.Recursion import Calculate, generate_content, get_difference_sum


# 完美羁绊方案
class PerfectScheme(Calculate):
    # 在未满足8人口时就进行判决判断 耗时约89秒
    # 效率提高85%
    # 击毙了约99.93%的情况
    def advance_judge(self, nest):
        # return True
        # *** 至高天
        # if fetter_data[26] != 0:
        #     return True
        # else:
        # (nest == (C.population - 6) and self.advance_judge_method(nest)) or \ # 468.44秒
        # (nest == (C.population - 5) and self.advance_judge_method(nest)) or \ # 430.34秒
        # (nest == (C.population - 4) and self.advance_judge_method(nest)) or \ # 458.05秒
        # (nest == (C.population - 3) and self.advance_judge_method(nest)) or \ # 422.98
        # (nest == (C.population - 2) and self.advance_judge_method(nest)) or \ # 513.93
        return nest < (C.population - 3) or \
            (nest == (C.population - 3) and self.advance_judge_method(nest)) or \
            (nest == (C.population - 2) and self.advance_judge_method(nest)) or \
            (nest == (C.population - 1) and self.advance_judge_method(nest))

    @timekeeping
    def advance_judge_method(self, nest):
        tolerate = (C.population - nest) * 3
        return get_difference_sum(tolerate) <= tolerate

    def last_step(self):
        # 初步排查掉羁绊浪费的阵容
        for i in range(1, len(C.fetter_data), 1):
            if C.fetter_data[i] != 0:
                # 有此羁绊时
                if C.fetter_data[i] not in C.fetter_database[i]:
                    return 0
        content = generate_content()
        self.solution.solution(content)
