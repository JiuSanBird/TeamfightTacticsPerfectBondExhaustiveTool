from OC import Configuration as C
from OC.Recursion import Calculate, generate_content


# 完美羁绊方案
class PerfectScheme(Calculate):
    # 在未满足8人口时就进行判决判断 耗时约36秒
    # 这将执行460万次
    # @timekeeping
    def advance_judge(self, nest):
        # tolerate:容忍度
        tolerate = (C.population - nest) << 1
        for i in range(C.fetter_n):
            # 有此羁绊
            if C.fetter_data[i] != 0:
                for l in range(1, len(C.fetter_database[i])):
                    difference = C.fetter_database[i][l] - C.fetter_data[i]
                    if difference >= 0:
                        tolerate -= difference
                        if tolerate < 0:
                            return False
                        break
        return True

    def last_step(self):
        # **双修出道
        # if 3 in C.r_database and 11 in C.r_database:
        #     return
        content = generate_content()
        self.solution.solution(content)
