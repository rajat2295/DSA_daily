class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for j in range(n):
            k = n-1
            i = 0
            while i<k:
                temp = matrix[j][i]
                matrix[j][i] = matrix[j][k]
                matrix[j][k] = temp
                i+=1
                k-=1    
''' easy way to understand
 # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for row in matrix:
            row.reverse() '''
