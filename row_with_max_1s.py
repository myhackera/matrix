#User function Template for python3



class Solution:
	def rowWithMax1s(self,arr, n, m):
	    i = 0
	    j = m-1
	    ans = -1
	    while i<n and j>=0:
	        if arr[i][j] == 1:
	            j -= 1
	            ans = i
	        else:
	            i += 1 
	    return ans
