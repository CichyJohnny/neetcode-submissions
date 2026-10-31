class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = len(matrix[0])
        l = 0
        p = len(matrix) * k - 1
        
        while l <= p:
            i = (l + p) // 2
            if matrix[i // k][i % k] == target:
                return True
            elif matrix[i // k][i % k] < target:
                l = i + 1
            else:
                p = i - 1
        
        return False

# [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]], l=0, p=11, i=5, matrix[1][1]=11>3
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]], l=0, p=4, i=2, matrix[0][2]=5>3
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]], l=0, p=1, i=1, matrix[0][1]=3==3
# return True
