# a b c
# d e f
# g h i
# Each cornor of matrix is maintained and take it's sum and simultaneously reduce cornors and add it into the resultant sum.


class Solution:
    def diagonalSum(self, a: List[List[int]]) -> int:
        res = 0
        n = len(a)
        r1 = r2 = 0
        r3 = r4 = n-1
        h1 = h3 = 0
        h2 = h4 = n-1
        while r1 < r3 and r2 < r4:
            res += a[r1][h1] 
            r1 += 1
            h1 += 1
            
            res += a[r2][h2]
            r2 += 1
            h2 -= 1
     
            res += a[r3][h3]
            r3 -= 1
            h3 += 1
            
            res += a[r4][h4]
            r4 -= 1
            h4 -= 1
            
        if r1 == r2 and h1 == h2 :
            res += a[r1][h1]
            
        return res
      
      
  # OPTIMAL SOLUTION
  class Solution:
    def diagonalSum(self, a: List[List[int]]) -> int:
        n = len(a)
        mid = n//2
        res = 0
        for i in range(n):
            
            # primary diagonal
            res += a[i][i]
            
            # secondary diagonal
            res += a[n-i-1][i]
        
        # middle element
        if n%2 == 1:
            res -= a[mid][mid]
        return res
