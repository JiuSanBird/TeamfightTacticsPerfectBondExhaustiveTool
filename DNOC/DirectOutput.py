from DNOC.ResultReduction import ResultReduction


# 直接输出结果
class DirectOutput(ResultReduction):
    def Method(self):
        self.next.Method()

    def solution(self, result):
        print(result)
