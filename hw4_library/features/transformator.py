from abc import ABCMeta, abstractclassmethod

class Transformator(metaclass = ABCMeta):
    @abstractclassmethod
    def transform(self,data,columns):
        return NotImplementedError
    


class NormalizationTransformator(Transformator):
    """
    NormalizationTransformator normalizes our columns

    Methods:
        transform(data,columns): DataFrame of interest and nromalized with columns
    """


    def __init__(self):
        pass



    def transform(self, data, columns):
        for c in columns:
            min_value = data[c].min()  # Use .min() to find the minimum value of the column
            max_value = data[c].max()  # Use .max() to find the maximum value of the column
            normalized_c = (data[c] - min_value) / (max_value - min_value)
            data[c] = normalized_c  # Update the column in the DataFrame
        return data


import numpy as np
class StandarizationTransformator(Transformator):
    """
    StandarizationTransformator normalizes our columns

    Methods:
        transform(data,columns): DataFrame of interest and standarized with columns
    """

    def __init__(self):
        pass

    import numpy as np

    def transform(self, data, columns):
        for c in columns:
            mean_value = np.mean(data[c])  # Calculate the mean of the column using np.mean()
            std_value = np.std(data[c])    # Calculate the standard deviation using np.std()
            data[c] = (data[c] - mean_value) / std_value
        return data
