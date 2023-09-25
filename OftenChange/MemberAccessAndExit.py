from DoNotOftenChange.Decorator import timekeeping
from OftenChange import Configuration as C


@timekeeping
# 成员加入 耗时约24秒
def member_access(nest, heroIndexes):
    # 成员加入套路数据库
    C.r_database[nest] = heroIndexes
    for i in range(1, len(C.hero_database[heroIndexes]), 1):
        C.fetter_data[C.hero_database[heroIndexes][i]] += 1
    # # ***龙神为14
    # if 14 in C.hero_database[heroIndexes]:
    #     # 龙神不为最后一个
    #     if nest != 7:
    #         C.r_database[nest + 1] = -1
    #     return nest + 2
    return nest + 1


# 成员退出 耗时约23秒
@timekeeping
def member_exit(nest, heroIndexes):
    for i in range(1, len(C.hero_database[heroIndexes]), 1):
        C.fetter_data[C.hero_database[heroIndexes][i]] -= 1
    # ***
    # if 14 in C.hero_database[heroIndexes]:
    #     return nest - 2
    return nest - 1
