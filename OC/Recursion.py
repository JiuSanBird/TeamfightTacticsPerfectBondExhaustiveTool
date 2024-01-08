import abc

import OC.MemberAccessAndExit as M
from DNOC.Agency import Agency
from OC import Configuration as C


# 生成内容
# 耗时0.02秒
# @timekeeping
def generate_content():
    # 完成度     key(索引) value(达成数)
    completeness = {}
    for i in range(1, len(C.fetter_data)):
        if C.fetter_data[i] != 0:
            for l in range(1, len(C.fetter_database[i])):
                if C.fetter_data[i] >= C.fetter_database[i][l]:
                    completeness[i] = C.fetter_database[i][l]
                else:
                    break
    # 羁绊
    fetter = ""
    for key, value in completeness.items():
        fetter += str(value) + C.fetter_database[key][0] + " "
    # 将数据注入文本
    content = [0] * (C.population + 1)
    content[0] = fetter
    # 阵容
    for i in range(0, C.population):
        # *** 巨像的阴影
        # if C.r_database[i] != -1:
        content[i + 1] = C.hero_database[C.r_database[i]][0]
    # print(content, end='\n')
    return content


# 计算
class Calculate(Agency):
    #                  初始索引
    def __init__(self, initial_indexes):
        self.initialIndexes = initial_indexes

    def Method(self):
        self.circulation(self.initialIndexes, 0)

    #   循环              成员数 - 1 起始值
    # 这种循环无法解决重复和去重情况
    def circulation(self, nest, start_value):
        # 最后一个成员已加入，开始判断
        if nest == C.population:
            self.last_step()
            return
        #                           英雄数 + 成员数 - 人口数
        for i in range(start_value, C.hero_n + nest - C.population + 1):
            nest = M.member_access(nest, i)
            # 成员不够，继续加入
            if self.advance_judge(nest):
                self.circulation(nest, i + 1)
            nest = M.member_exit(nest, i)

    # 解决办法
    solution = None

    @abc.abstractmethod
    def advance_judge(self, nest):
        pass

    # 最后一步
    @abc.abstractmethod
    def last_step(self):
        pass
