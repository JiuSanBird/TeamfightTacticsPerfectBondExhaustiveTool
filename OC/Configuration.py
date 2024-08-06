hero_n = 60  # 英雄数
hero_n_virtual = 73  # 虚的英雄数 有一些棋子为无效数据
job_n = 11  # 职业数
race_n = 16  # 种族数
fetter_n = job_n + race_n + 1  # 羁绊数量
job_max = 4  # 职业最大羁绊组成次数
race_max = 4  # 种族最大羁绊组成次数
population = 8  # 人口数

# 英雄数据库
hero_database = [0] * hero_n_virtual
# 羁绊数据库
fetter_database = [0] * fetter_n

# 套路数据库 成员
r_database = [0] * population

# 羁绊数据 第一个数据是0的数量,无用 (用于计算)
fetter_data = {i: 0 for i in range(fetter_n)}

# 必须羁绊
must_fetter = {}  # 遍历
