class Solution:
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    def reverseCol(self, matrix):
        n = len(matrix)
        for i in range(n):
            j = 0
            k = n-1
            while j<k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1 
                k -= 1
    
    # FOR LEFT ROTATION
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reverseCol(matrix)
        return matrix
        
   # FOR RIGHT ROTATION
    def rotate(self, matrix: List[List[int]]) -> None:
        self.reverseCol(matrix)
        self.transpose(matrix)
        return matrix
