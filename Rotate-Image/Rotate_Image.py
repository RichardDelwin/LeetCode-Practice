class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_bndry = len(matrix)-1
        
        for row in range(len(matrix)//2):
            
            for col in range(row, matrix_bndry):
                
                temp = matrix[row][col]
                matrix[row][col] = matrix[matrix_bndry-col+row][row]
                matrix[matrix_bndry-col+row][row] =  matrix[matrix_bndry][matrix_bndry-col+row]
                matrix[matrix_bndry][matrix_bndry-col+row] = matrix[col][matrix_bndry]
                matrix[col][matrix_bndry] = temp
                
            matrix_bndry -= 1