class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        k = 0
        l = 0
        m = len(matrix)
        n = len(matrix[0])
        
        while k < m and l < n:
           
            for p in range(l, n):
                res.append(matrix[k][p])
            k += 1 
            
            for p in range(k, m):
                res.append(matrix[p][n-1])
            n -= 1 
            
            if k<m:
                for p in range(n-1, l-1, -1):
                    res.append(matrix[m-1][p])
                m -= 1
            
            if l<n:
                for p in range(m-1, k-1, -1):
                    res.append(matrix[p][l])
                l += 1 
        return res
                    
