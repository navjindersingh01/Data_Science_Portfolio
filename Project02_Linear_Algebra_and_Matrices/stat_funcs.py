import math
from collections import defaultdict

def get_row (matrix,row):
    return matrix[row]

def get_column(matrix,col):
    return [matrix_row[col]
            for matrix_row in matrix]

def vector_add(v1,v2):
    return [v1_i + v2_i 
            for v1_i,v2_i in zip(v1,v2)]

def vector_subtract(v1,v2):
    return [v1_i - v2_i 
            for v1_i,v2_i in zip(v1,v2)]

def get_popular_interests(matrix):
    result = matrix[0]
    for vector in matrix[1:]:
        result = vector_add(result,vector)
    return result

def dot(v1,v2):
    return sum(v1_i * v2_i
               for v1_i,v2_i in zip(v1,v2))

def squared_sum(vector):
    return dot(vector,vector)

def magnitude(vector):
    return math.sqrt(squared_sum(vector))

def distance(v1,v2):
    return magnitude(vector_subtract(v1,v2))

def find_soulmate(user_id,matrix):
    user_basket = matrix[user_id]
    distances = defaultdict(list)
    for user_ids,vector in enumerate(matrix):
        dist = distance(user_basket,vector)
        if dist > 0:
            distances[user_ids].append(dist)
    recommended_user = min(distances,key = lambda k : distances[k][0])
    return recommended_user,round(distances[recommended_user][0],2)


def is_connected(matrix, user_a, user_b):
    return True if matrix[user_a][user_b] == 1 else False