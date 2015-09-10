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
    return [vector_add(v_1,v_2) for v_1 in args for v_2 in args if v_1 != v_2]
print(vector_sum([3,2,1],[2,1,3],[1,3,2],[1,2,3]))
    # """vector_sum can take any number of vectors and add them together."""
    #
    # assert vector_sum(v, w, u, y, z) == [12, 26, 35]

def dot(vector_1, vector_2):
    """
    dot([a b], [c d])   = a * c + b * d

    dot(Vector, Vector) = Scalar
    """
    shape_exception_check(vector_1, vector_2)
    return sum([vector_1[i]*vector_2[i] for i in range(len(vector_1))])
    # assert dot(w, y) == 160
    # assert dot(m, n) == 15
    # assert dot(u, z) == 0


def vector_multiply(vector, scalar):
    """
    [a b]  *  Z     = [a*Z b*Z]

    Vector * Scalar = Vector
    """
    return[vector[i]*scalar for i in range(len(vector))]
    
def test_vector_mean():
    """
    mean([a b], [c d]) = [mean(a, c) mean(b, d)]

    mean(Vector)       = Vector
    """
    assert vector_mean(m, n) == [4, 2]
    assert vector_mean(v, w) == [0.5, 2.5, 2]
    assert is_equal(vector_mean(v, w, u)[0], 2 / 3)
    assert is_equal(vector_mean(v, w, u)[1], 2)
    assert is_equal(vector_mean(v, w, u)[2], 5 / 3)
