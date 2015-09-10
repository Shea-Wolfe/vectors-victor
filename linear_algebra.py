import math
class ShapeException(Exception):
    pass

def shape_exception_check(vector_1, vector_2):
    if shape(vector_1) != shape(vector_2):
        raise ShapeException('Those vectors aren\'t the same length!')

def matrix_exception_check(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ShapeException('Those vectors aren\'t the same length!')

def shape(vector):
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    if type(vector[0]) != list:
        return (len(vector),)
    return (len(vector),len(vector[0]))
def vector_add(vector_1, vector_2):
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    """
    shape_exception_check(vector_1, vector_2)
    return [vector_1[i]+vector_2[i] for i in range(len(vector_1))]


def vector_sub(vector_1, vector_2):
    """
    [a b]  - [c d]  = [a-c b-d]

    Matrix + Matrix = Matrix
    """
    shape_exception_check(vector_1, vector_2)
    return [vector_1[i] - vector_2[i] for i in range(len(vector_1))]


def vector_sum(*args):
    base = [0]*len(args[0])
    for arg in args:
        base = vector_add(base, arg)
    return base


def dot(vector_1, vector_2):
    """
    dot([a b], [c d])   = a * c + b * d

    dot(Vector, Vector) = Scalar
    """
    shape_exception_check(vector_1, vector_2)
    return sum([vector_1[i]*vector_2[i] for i in range(len(vector_1))])


def vector_multiply(vector, scalar):
    """
    [a b]  *  Z     = [a*Z b*Z]

    Vector * Scalar = Vector
    """
    return[vector[i]*scalar for i in range(len(vector))]


def vector_mean(*args):
    """
    mean([a b], [c d]) = [mean(a, c) mean(b, d)]

    mean(Vector)= Vector
    """
    return [i/len(args) for i in vector_sum(*args)]


def magnitude(vector):
    """
    magnitude([a b])  = sqrt(a^2 + b^2)

    magnitude(Vector) = Scalar
    """
    return math.sqrt(sum([vector[i]**2 for i in range(len(vector))]))


def matrix_row(matrix, row):
    """
           0 1  <- rows
       0 [[a b]]
       1 [[c d]]
       ^
     columns
    """
    return matrix[row]


def matrix_col(matrix, column):
    """
           0 1  <- rows
       0 [[a b]]
       1 [[c d]]
       ^
     columns
    """
    return [l[column]for l in matrix]



def matrix_scalar_multiply(matrix, scalar):
    """
    [[a b]   *  Z   =   [[a*Z b*Z]
     [c d]]              [c*Z d*Z]]

    Matrix * Scalar = Matrix
    """
    return [vector_multiply(vector, scalar) for vector in matrix]

def matrix_vector_multiply(matrix, vector):
    """
    [[a b g]   *  [x   =   [a*x+b*y+g*z
     [c d h]       y        c*x+d*y+h*z
     [e f i]       z]       e*x+f*y+i*z]

    Matrix * Vector = Vector
    """
    matrix_exception_check(matrix, vector)
    post_mult = [vector_multiply(matrix_col(matrix,i), vector[i]) for i in range(len(vector))]
    correct_rows = [matrix_col(post_mult, i) for i in range(len(post_mult[0]))]
    return [sum(x) for x in correct_rows]
