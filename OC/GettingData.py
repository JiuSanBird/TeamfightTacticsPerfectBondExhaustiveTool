import re  # re库用来通过正则表达式查找指定字符串
from DNOC import Network
from OC import Configuration as C

fetter_ID = [0, ]

# 创建正则表达式对象，表示规则（即字符串的模式）
link_name = re.compile(',"displayName":"(.*?)"')
link_jobs = re.compile(',"jobIds":"(.*?)"')
link_races = re.compile(',"raceIds":"(.*?)"')
link_jobId = re.compile('"jobId":"(.....)"')
link_raceId = re.compile('"raceId":"(.....)",')

link_name_f = re.compile(',"name":"(.*?)"')
# 阶段提取规则
link_stage_f = re.compile('"(.?)":"')


# 供外部调用
def execute():
    get_job()
    get_race()
    get_chess()
    remedial_work()


def get_job():
    url = "https://game.gtimg.cn/images/lol/act/img/tft/js/job.js"
    html = Network.ask_url(url)
    initial_value = 0  # 起始值
    # 返回string中所有与pattern匹配的全部字符串,返回形式为数组
    l = re.findall(link_stage_f, html)
    for i in range(0, C.job_n):
        # job_max指一个羁绊最大的触发次数
        date_h = [0] * (C.job_max + 1)
        date_h[0] = re.findall(link_name_f, html)[i]
        for m in range(initial_value, len(l), 1):
            # 注意:如果出现下一个的最少羁绊需求 > 本羁绊需求的最大值,那么就要根据情况修改
            # *** 双修出道
            if i == 2:
                for n in range(0, m - initial_value + 1, 1):
                    date_h[n + 1] = int(l[initial_value + n])
                initial_value = m + 1
                break
            if m < len(l) - 1:
                # 这时，m前面的几个就是我们要的
                if l[m + 1] <= l[m]:
                    for n in range(0, m - initial_value + 1, 1):
                        date_h[n + 1] = int(l[initial_value + n])
                    # 更新初始值的位置
                    initial_value = m + 1
                    break
            else:
                # 最后一个装弹
                for n in range(0, m - initial_value + 1, 1):
                    date_h[n + 1] = int(l[initial_value + n])
        # print(date_h)
        C.fetter_database[i + 1] = date_h
    # 生成修正表
    global fetter_ID
    fetter_ID += list(map(int, re.findall(link_jobId, html)))
    # *** 召唤物
    # fetter_ID.pop()
    # fetter_ID.remove(9018)
    # C.fetter_database[14] = ['海洋之灾', 1]
    print("职业羁绊数据库已建立")


def get_race():
    url = "https://game.gtimg.cn/images/lol/act/img/tft/js/race.js"
    html = Network.ask_url(url)
    # 起始值
    initial_value = 0
    l = re.findall(link_stage_f, html)
    for i in range(0, C.race_n):
        date_h = [0] * (C.race_max + 1)
        date_h[0] = re.findall(link_name_f, html)[i]
        for m in range(initial_value, len(l), 1):
            # 注意:如果出现下一个的最少羁绊需求 > 本羁绊需求的最大值,那么就要根据情况修改
            # *** 戏命师
            if i == 1 or i == 3 or i == 13:
                for n in range(0, m - initial_value + 1, 1):
                    date_h[n + 1] = int(l[initial_value + n])
                initial_value = m + 1
                # *** 暗裔修正
                # date_h[2] = 2
                # initial_value += 1
                break
            if m < len(l) - 1:
                if l[m + 1] <= l[m]:
                    for n in range(0, m - initial_value + 1, 1):
                        date_h[n + 1] = int(l[initial_value + n])
                    initial_value = m + 1  # 更新初始值的位置
                    break
            else:
                for n in range(0, m - initial_value + 1, 1):
                    date_h[n + 1] = int(l[initial_value + n])
        C.fetter_database[C.job_n + i + 1] = date_h
    global fetter_ID
    fetter_ID += list(map(int, re.findall(link_raceId, html)))
    print("种族羁绊数据库已建立")


# 获取棋子
def get_chess():
    url = "https://game.gtimg.cn/images/lol/act/img/tft/js/chess.js"
    html = Network.ask_url(url)
    # 仅以次注释，纪念我浪费的7个小时，在动态网页和411的先后折磨中逝去
    # data = bytes(urllib.parse.urlencode({"name": "eric"}), encoding="utf-8") #数据包
    for i in range(C.hero_n):
        date_h = [0] * 5
        # 名字
        date_h[0] = re.findall(link_name, html)[i]

        l = re.findall(link_jobs, html)[i].split(',')
        for n in range(0, len(l), 1):
            date_h[n + 1] = int(l[n] if l[n] != '' else 0)
        l = re.findall(link_races, html)[i].split(',')
        for n in range(0, min(len(l), 2), 1):
            date_h[n + 3] = int(l[n] if l[n] != '' else 0)
        for n in range(1, len(date_h), 1):
            if date_h[n] in fetter_ID:
                date_h[n] = fetter_ID.index(date_h[n])
            else:
                date_h[n] = 0
        while 0 in date_h:
            date_h.remove(0)
        C.hero_database[i] = date_h
    print("英雄数据库已建立")


# 补救工作
def remedial_work():
    # *** 将龙神排在最前方
    # C.hero_database.sort(key=lambda t: 14 not in t)

    # *** 修正英雄羁绊错误
    # C.hero_database[16] = ['众星之子', 16, 20]
    # C.hero_database.remove()

    # 排除0
    for list in C.fetter_database:
        while list != 0 and 0 in list:
            list.remove(0)

    # 根据羁绊数量进行倒序排序
    C.hero_database.sort(key=lambda x: len(x), reverse=True)

    # 将列表转换为元组,提高效率 节约35秒
    C.hero_database = tuple(C.hero_database)
    C.fetter_database = tuple(C.fetter_database)