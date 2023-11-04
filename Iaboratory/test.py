import time

from OC.Configuration import fetter_data as C
from OC.GettingData import execute

# 四种方案:
# 用一个数组,成员加入增加数据,成员退出减少数据
# 每一个组合新建一个数组,成员加入增加数组,无需退出减少数据
# 用一个数组,每次Clear数组,成员加入增加数组,无需退出减少数据
# 改用字典,配合前三种方案中最快的方案


execute()


start_time = time.time()

for item in range(123456789):
    for i in range(1, len(C.fetter_data)):
        if C.fetter_data[i] != 0:
            # 有此羁绊时
            if C.fetter_data[i] not in C.fetter_database[i]:
                break

end_time = time.time()
print("\n总耗时: {:.2f}秒".format(end_time - start_time))
