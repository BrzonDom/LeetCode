"""
https://leetcode.com/problems/richest-customer-wealth

You are given an m x n integer grid accounts where
accounts[i][j] is the amount of money the i^th customer has in the j^th bank.

Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Example 1:

    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6

Example 2:

    Input: accounts = [[1,5],[7,3],[3,5]]
    Output: 10

Example 3:

    Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
    Output: 17


Constraints:

    m == accounts.length
    n == accounts[i].length
    1 <= m, n <= 50
    1 <= accounts[i][j] <= 100

"""


Input_matLst = [[[1, 2, 3], [3, 2, 1]],
                [[1, 5], [7, 3], [3, 5]],
                [[2, 8, 7], [7, 1, 3], [1, 9, 5]]]


print("Driver solution:\n")

for mat in Input_matLst:
    sumLst = []
    maxSum = 0
    maxI = 0
    for r, row in enumerate(mat):
        print(f"\t{r+1}.Pers.\t\t{row}")
        sumRow = sum(row)

        print(f"\t\tSum: {sumRow}")
        sumLst.append(sumRow)

        if sumRow > maxSum:
            maxSum = sumRow
            maxI = r + 1

    print()
    print(f"\tMax sum: {maxI} person with {maxSum}")

    print("\n")


