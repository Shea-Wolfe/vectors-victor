class ShapeException(Exception):
    pass

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
    if shape(vector_1) != shape(vector_2):
        raise ShapeException('Those vectors aren\'t the same length!')
    return [vector_1[i]+vector_2[i] for i in range(len(vector_1))]


    assert vector_add(v, w) == [1, 5, 4]
    assert vector_add(u, y) == [11, 21, 31]
    assert vector_add(u, z) == u
