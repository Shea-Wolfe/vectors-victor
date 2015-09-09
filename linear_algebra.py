class ShapeException(Exception):
    pass

def shape_exception_check(vector_1, vector_2):
    if shape(vector_1) != shape(vector_2):
        raise ShapeException('Those vectors aren\'t the same length!')


def shape(vector):
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    return (len(vector),)

def vector_add(vector_1, vector_2):
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    """
    shape_exception_check(vector_1, vector_2)
    return [vector_1[i]+vector_2[i] for i in range(len(vector_1))]


    # assert vector_add(v, w) == [1, 5, 4]
    # assert vector_add(u, y) == [11, 21, 31]
    # assert vector_add(u, z) == u

def vector_sub(vector_1, vector_2):
    """
    [a b]  - [c d]  = [a-c b-d]

    Matrix + Matrix = Matrix
    """
    shape_exception_check(vector_1, vector_2)
    return [vector_1[i] - vector_2[i] for i in len(vector_1)]
    # assert vector_sub(v, w) == [1, 1, -4]
    # assert vector_sub(w, v) == [-1, -1, 4]
    # assert vector_sub(y, z) == y
    # assert vector_sub(w, u) == vector_sub(z, vector_sub(u, w))

def vector_sum(*args):
    return [vector_sum(i) for i in zip(*args)]
    # """vector_sum can take any number of vectors and add them together."""
    #
    # assert vector_sum(v, w, u, y, z) == [12, 26, 35]
