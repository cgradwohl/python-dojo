from math import floor


def diagonal_sum(M):
    N = len(M)
    result = 0
    for i in range(N):
        result += M[i][i]
        result += M[i][N - i - 1]
    if N % 2 != 0:
        return result - (M[floor(N/2)][floor(N/2)])
    return result


M = [[1, 2, 3, 9],
     [4, 5, 6, 4],
     [7, 8, 9, 13],
     [7, 8, 9, 13]
     ]
print(diagonal_sum(M))
