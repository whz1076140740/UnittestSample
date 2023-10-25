from abc import ABCmeta, abstractclassmethod

class Transformator(metaclass = ABCmeta):
    @abstractclassmethod
    def transform(self):
        return NotImplementedError