class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #count no. of lists in matrix
        m = len(matrix) -1
        #count how many elements in 1 list in the matrix
        n = len(matrix[0]) -1

        row = 0
        #initialise 2 points, 1 points at last element of first row, other points at first element of last row

        while row <= m:
            l = matrix[row][n]
            r = matrix[m][0]
            #if l is too small, target must not be in this list, move on to next list
            if l < target:
                row = row+1
            #if r is too large
            elif r > target:
                m=m-1
            # if l > target, if target exists, it must be within current list
            elif l > target:
                #do a linear scan through current list
                for i in range(n+1):
                    if matrix[row][i] == target:
                        return True
                return False
            # r < target, if target exists, it must be within current list
            else:
                for i in range(n+1):
                    if matrix[m][i] == target:
                        return True
                return False
        
        return False







        