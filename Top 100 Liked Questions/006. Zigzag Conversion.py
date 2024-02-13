"""
6. Zigzag Conversion

https://leetcode.com/problems/zigzag-conversion/

    The string "PAYPALISHIRING" is written in a zigzag pattern
    on a given number of rows like this:

        P   A   H   N
        A P L S I I G
        Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion
    given a number of rows:

        string convert(string s, int numRows);

    Example 1:

        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"

    Example 2:

        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"

        Explanation:
            P     I    N
            A   L S  I G
            Y A   H R
            P     I

    Example 3:

        Input: s = "A", numRows = 1
        Output: "A"

    Constraints:

        1 <= s.length <= 1000
        s consists of English letters (lower-case and upper-case), ',' and '.'.
        1 <= numRows <= 1000
"""

Input_encodeLst = [["PAYPALISHIRING", 3],
                   ["PAYPALISHIRING", 4],
                   ["A", 1]]

# print("Driver print:\n")
#
# for encode in Input_encodeLst:
#     str = encode[0]
#     rows = encode[1]
#
#     print("\tString:       ", str)
#     print("\tNum. of rows: ", rows)
#     print("\n")
#

print("Driver solution:\n")

for encode in Input_encodeLst:
    str = encode[0]
    rows = encode[1]
    strLen = len(str)

    print("\tString:         ", str)
    print("\t\tStr. len.:  ", strLen)
    print("\tNum. of rows.:  ", rows)
    print()

    colFill = [rows]

    if rows > 1:
        for zigFill in range(rows-2):
            colFill.append(1)

    # print("\t", colFill)
    # print()

    colCnt = 0
    colFillCnt = 0
    colFillLen = len(colFill)

    while strLen > 0:
        strLen -= colFill[colFillCnt]
        colCnt += 1
        colFillCnt += 1

        if colFillCnt == colFillLen:
            colFillCnt = 0

    print("\tNum. of cols.:  ", colCnt)
    print()
    print("\tCol fill pattern:", colFill)
    print()
    print("\tZigZag matrix:\n")

    zigMat = [[' ' for col in range(colCnt)] for row in range(rows)]

    for row in zigMat:
        print("\t\t", row)


    print("\n")

