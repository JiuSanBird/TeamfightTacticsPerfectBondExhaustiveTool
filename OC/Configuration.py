hero_n = 59  # 英雄数
job_n = 15  # 职业数
race_n = 13  # 种族数
fetter_n = job_n + race_n + 1
job_max = 5  # 职业最大羁绊组成次数
race_max = 4  # 种族最大羁绊组成次数
population = 8  # 人口数

# 英雄数据库
hero_database = [0] * hero_n # 查    [] 遍历 查
# 羁绊数据库
fetter_database = [0] * fetter_n # 赋值  [] in

# 套路数据库 成员
r_database = [0] * population

# 羁绊数据 第一个数据是0的数量,无用 (用于计算)
fetter_data = [0] * fetter_n

# 必须羁绊
must_fetter = { } # 遍历
