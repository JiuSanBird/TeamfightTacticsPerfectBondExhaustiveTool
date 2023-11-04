import csv
from DNOC.ResultReduction import ResultReduction


# 文件处理
class FileDispose(ResultReduction):
    def __init__(self, next, fileName):
        super().__init__(next)
        self.file = open(fileName + ".csv", 'w')

    file = None

    @property
    def dis(self):
        return self.file

    @dis.setter
    def dis(self, value):
        self.file = value

    def Method(self):
        csv.writer(self.file).writerow(['羁绊', '1', '2', '3', '4', '5', '6', '7', '8'])
        self.next.Method()
        self.file.close()

    def solution(self, result):
        print('.', end='')
        csv.writer(self.file).writerow(result)
