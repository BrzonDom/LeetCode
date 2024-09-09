"""
54. Spiral Matrix

https://leetcode.com/problems/spiral-matrix/description/


    Given an m x n matrix, return all elements of the matrix in spiral order.


    Example 1:

        Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    Example 2:

        Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

        Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


    Constraints:

        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 10
        -100 <= matrix[i][j] <= 100


    Tags:

        Array
        Matrix
        Simulation

"""


if __name__ == "__main__":

    InputLst = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Mrx = case

        dmR = len(Mrx)
        dmC = len(Mrx[0])

        print(f"\tMatrix:")

        for rw in Mrx:
            print("\t\t", end="")
            for cl in rw:
                print(f"{cl:2}", end=" ")
            print()
        print()

        print(f"\tRows: {dmR}")
        print(f"\tCols: {dmC}")
        print()

        brTp = 0
        brRg = dmC
        brDw = dmR
        brLf = 0

        print("\t\t", end="")
        for idx in range(brLf, brRg):
            print(f"{Mrx[brTp][idx]:2}", end=" ")

        print("\n")
