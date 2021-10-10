
import numpy as np

def calculate(values):
    print(len(values))
    if len(values)==9:
        array = np.array(values)
    else: 
        for non in range(9-len(values)):
            values.append(np.random.randint(1,10))
            print(len(values))
            array = np.array(values)
    matrix = array.reshape(3,3)
    mean_1 = matrix.mean(axis=0)
    mean_2 = matrix.mean(axis=1)
    mean_flatten = matrix.mean()
    variance_1 = matrix.var(axis=0)
    variance_2 = matrix.var(axis=1)
    variance_flatten = matrix.var()
    standard_desviation_1 = matrix.std(axis=0)
    standard_desviation_2 = matrix.std(axis=1)
    standard_desviation_flatten = matrix.std()
    max_1 = matrix.max(axis=0)
    max_2 = matrix.max(axis=1)
    max_flatten = matrix.max()
    min_1 = matrix.min(axis=0)
    min_2= matrix.min(axis=1)
    min_flatten = matrix.min()
    sum_1 = matrix.sum(axis=0)
    sum_2 = matrix.sum(axis=1)
    sum_flatten = matrix.sum()
    result = {
         "mean": [list(mean_1),list(mean_2),mean_flatten],
         "variance": [list(variance_1),list(variance_2),variance_flatten],
         "standard desviation": [list(standard_desviation_1),list(standard_desviation_2),standard_desviation_flatten],
         "max": [list(max_1),list(max_2),max_flatten],
         "min": [list(min_1),list(min_2),min_flatten],
         "sum": [list(sum_1),list(sum_2),sum_flatten]
    }
    return result
print(calculate([2,6,2,8,4,0,1]))