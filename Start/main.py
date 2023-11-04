# -*- coding = utf-8 -*-
# 写于2020年10月 8日
# 终于2020年10月18日
"""
如版本更迭,请更新以下数据
英雄数 职业数 种族数 职业最大羁绊组成次数 种族最大羁绊组成次数
以及以 *** 为开头的注释提及的内容
"""
from DNOC.Decorator import is_Timekeeping, print_statistical_time
from DNOC.DirectOutput import DirectOutput
from DNOC.FileDispose import FileDispose
from DNOC.Timekeeping import Timekeeping
from OC import Configuration as C, GettingData
from OC import MemberAccessAndExit as M
from OC.PerfectScheme import PerfectScheme

GettingData.execute()


def print_list(list):
    for i in range(0, len(list), 1):
        if i % 5 == 0:
            print(i, list[i], end="\n")
        else:
            print(i, list[i], end="\t")
    print()


# 转职需求
print_list(C.fetter_database)
print("是否有转职需求？(无则输入.)")
Input = input()
if Input != ".":
    C.fetter_data[int(Input)] = 1

initialIndexes = 0
# 必须棋子
print_list(C.hero_database)
print("是否有必须棋子？(无则输入.)")
Input = input()
if Input != ".":
    initialIndexes = M.member_access(initialIndexes, int(Input))

# 默认:routine
print("请输入生成文件名称(无则输入.)")
Input = input()
if Input != ".":
    solution = FileDispose(PerfectScheme(initialIndexes), Input)
    PerfectScheme.solution = solution
    Timekeeping(solution).Method()
    # 输出各方法用时
    if is_Timekeeping:
        print_statistical_time()
else:
    solution = DirectOutput(PerfectScheme(initialIndexes))
    PerfectScheme.solution = solution
    solution.Method()

print("\n套路数据库已建立")
