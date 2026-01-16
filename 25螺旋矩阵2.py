class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        num = 1
        for i in range(n//2):
            for j in range(i,n-i-1):
                matrix[i][j] = num
                num += 1
            for j in range(i,n-i-1):
                matrix[j][n-i-1] = num
                num += 1
            for j in range(i,n-i-1):
                matrix[n-i-1][n-j-1] = num
                num += 1
            for j in range(i,n-i-1):
                matrix[n-j-1][i] = num
                num += 1
        if n%2:
            matrix[n//2][n//2] = num
        return matrix