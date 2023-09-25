import abc
from DoNotOftenChange.Agency import Agency


# 处理结果
class ResultReduction(Agency):
    def __init__(self, next):
        self.next = next

    def Method(self):
        pass

    @abc.abstractmethod
    def solution(self, result):
        pass
