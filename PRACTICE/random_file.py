import numpy as np

def random_diagonal_matrix(vector):
    identity_matrix = np.identity(vector.shape[0])
    result = identity_matrix*vector
    return result
goal = random_diagonal_matrix(np.random.randint(1,700,[600]))


print(goal)

