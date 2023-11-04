from DNOC.ComplementScheme import ComplementScheme
from DNOC.DirectOutput import DirectOutput
from OC import Configuration as C
from OC import GettingData
from OC import MemberAccessAndExit as M


# 补全计划,出已有单位,然后补全
#

def print_list(list):
    for i in range(0, len(list), 1):
        if i % 5 == 0:
            print(i, list[i], end="\n")
        else:
            print(i, list[i], end="\t")
    print()


GettingData.execute()

# 转职需求
print_list(C.fetter_database)
print("是否有转职需求？(无则输入.)")
Input = input()
if Input != ".":
    C.fetter_data[int(Input)] += 1
    print_list(C.fetter_database)
    print("是否有转职需求？(无则输入.)")
    Input = input()
    if Input != ".":
        C.fetter_data[int(Input)] += 1

while True:
    print_list(C.fetter_database)
    print("是否有必须羁绊?(无则输入.)")
    key = input()
    if key == ".":
        break
    else:
        print("请输入所需层数")
        value = int(input())
        C.must_fetter[int(key)] = value

nest = 0
# 必须棋子
while True:
    print_list(C.hero_database)
    print("已有棋子(结束输入.)")
    Input = input()
    if Input == ".":
        break
    else:
        nest = M.member_access(nest, int(Input))

solution = DirectOutput(ComplementScheme(nest))
ComplementScheme.solution = solution
solution.Method()

print("程序运行结束")
