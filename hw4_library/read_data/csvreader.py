#reader.Reader
import reader
import pandas as pd
from sklearn.model_selection import train_test_split 


class CSVReader(reader.Reader):

    def read(path):
        data = pd.read_csv(path)

        #split with test size
        trainSize = 0.83
        train_data,text_data = train_test_split(data, trainSize)
        return train_data,text_data