matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3


def matrixsearch(matrix, target):
    for i in range(len(matrix)):
        left = 0
        right = len(matrix[i])-1

        while left <= right:
            mid = (left+right)//2

            if target < matrix[i][mid]:
                right = mid -1
            elif target > matrix[i][mid]:
                left = mid +1 
            else:
                return True
    return False

print(matrixsearch(matrix, target))