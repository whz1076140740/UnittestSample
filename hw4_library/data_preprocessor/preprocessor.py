from abc import ABCMeta,abstractclassmethod

class Preprocessor(metaclass = ABCMeta):

    @abstractclassmethod
    def preprocess(self,train_data, column):
        return NotImplementedError
    
class FillNaNsColumnPreprocessor(Preprocessor):
    def preprocess(self,train_data, columns):
        for c in columns:
            train_data[c].fillna(train_data[c].mean(), inplace=True)
        return train_data

class RemoveNaNsRowPreprocessor(Preprocessor):
    def preprocess(self,train_data, column):
        return train_data.dropna(subset = column)