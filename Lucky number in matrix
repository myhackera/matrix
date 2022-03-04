# leetcode 1380
class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        row = []
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            res = []
            for j in range(n):
                res.append(mat[i][j])
            row.append(min(res))
        print(row)
        
        col = []
        for i in range(n):
            res = []
            for j in range(m):
                res.append(mat[j][i])
            col.append(max(res))
        print(col)
        
        ret= []
        for val in row:
            if val in col:
                ret.append(val)
        return ret
