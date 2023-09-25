# python中没有接口...

import abc


# abc.ABCMeta是实现抽象类的一个基础类
class Agency(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Method(self):
        pass
