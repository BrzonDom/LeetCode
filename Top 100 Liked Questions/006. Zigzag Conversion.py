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

def ZigZagEncodeV2_Sol(strIn, rows):

    if rows == 1 or rows >= len(strIn):
        return strIn

    rowMat = [''] * rows

    direct = 1
    row = 0

    for char in strIn:
        rowMat[row] += char
        row += direct

        if row == 0 or row == rows-1:
            direct *= -1

    return ''.join(rowMat)


def ZigZagEncodeV1_Sol(strIn, rows):

    if rows == 1 or rows >= len(strIn):
        return strIn


    strLen = len(strIn)

    colFill = [rows]

    for zigFill in range(rows - 2):
        colFill.append(1)

    colCnt = 0
    colFillCnt = 0
    colFillLen = len(colFill)

    while strLen > 0:
        strLen -= colFill[colFillCnt]
        colCnt += 1
        colFillCnt += 1

        if colFillCnt == colFillLen:
            colFillCnt = 0

    strLen = len(strIn)
    cols = colCnt

    zzMat = [[' ' for col in range(cols)] for row in range(rows)]

    colFillCnt = 0
    fillCnt = 0

    for c in range(cols):
        for r in range(rows):

            if fillCnt >= strLen:
                break

            if colFillCnt == 0:
                zzMat[r][c] = strIn[fillCnt]
                fillCnt += 1

                if r == rows-1:
                    colFillCnt += 1

            elif r == rows - 1 - colFillCnt:
                zzMat[r][c] = strIn[fillCnt]
                fillCnt += 1
                colFillCnt += 1

                if colFillCnt == colFillLen:
                    colFillCnt = 0

                break

            if colFillCnt == colFillLen:
                colFillCnt = 0

            strOut = ""

            for row in zzMat:
                for col in row:

                    if col != " ":
                        strOut += col

            return strOut


def ZigZagEncode_Prt(strIn, rows):

    print("\tString:         ", strIn)

    strLen = len(strIn)
    print("\t\tStr. len.:  ", strLen)
    print("\tNum. of rows.:  ", rows)
    print()

    """     Pattern for filling up the ZigZag matrix     
                1. it fills the first column with num. of letters as num. of rows   """
    colFill = [rows]

    for zigFill in range(rows-2):
        """     2. 3... it fills the rest of the columns in pattern with
                    a single letter     """
        colFill.append(1)

    """     colCnt ~ count of needed columns    """
    colCnt = 0
    """     colFillCnt ~ count of the pattern   """
    colFillCnt = 0
    """     colFillLen ~ length of the pattern  """
    colFillLen = len(colFill)

    while strLen > 0:
        strLen -= colFill[colFillCnt]
        colCnt += 1
        colFillCnt += 1

        if colFillCnt == colFillLen:
            """     Return the pattern to its beginning     """
            colFillCnt = 0

    strLen = len(strIn)
    cols = colCnt

    print("\tNum. of cols.:  ", colCnt)
    print()
    print("\tCol fill pattern:", colFill)
    print()
    print("\tZigZag matrix slots:\n")

    zzMat = [[' ' for col in range(cols)] for row in range(rows)]

    for row in zzMat:
        print("\t\t", row)

    """     colFillCnt ~ count of the pattern   """
    colFillCnt = 0
    """     fillCnt ~ count of used characters  """
    fillCnt = 0

    for c in range(cols):
        for r in range(rows):

            if fillCnt >= strLen:
                """     If all the characters from In string were used """
                break

            if colFillCnt == 0:
                """     1. pattern numb.
                            fills the entire column     """

                zzMat[r][c] = strIn[fillCnt]
                fillCnt += 1

                if r == rows-1:
                    """     When column filled
                                shift to next pattern numb.     """
                    colFillCnt += 1

            elif r == rows-1 - colFillCnt:
                """     If matching row for n. pattern numb.
                            fill the space      """

                zzMat[r][c] = strIn[fillCnt]
                fillCnt += 1
                colFillCnt += 1

                if colFillCnt == colFillLen:
                    """     Return the pattern to its beginning     """
                    colFillCnt = 0

                """     Skip to next column     """
                break

            if colFillCnt == colFillLen:
                """     Return the pattern to its beginning     """
                colFillCnt = 0

    print("\n\tZigZag matrix filled:")
    strOut = ""

    for row in zzMat:
        print("\n", end="\t\t ")
        for col in row:
            print(col, end=" ")
            if col != " ":
                strOut += col
    print("\n")

    print("\tOut string:", strOut)
    print()

    return strOut


Input_encodeLst = [["PAYPALISHIRING", 3],
                   ["PAYPALISHIRING", 4],
                   ["A", 1],
                   ["AB", 1]]

# print("Driver print:\n")
#
# for encode in Input_encodeLst:
#     strIn = encode[0]
#     rows = encode[1]
#
#     print("\tString:       ", strIn)
#     print("\tNum. of rows: ", rows)
#     print("\n")
#

print("Driver solution:\n")

for encode in Input_encodeLst:
    strIn = encode[0]
    rows = encode[1]
    strLen = len(strIn)

    print("\tIn string:      ", strIn)
    print("\t\tStr. len.:  ", strLen)
    print("\tNum. of rows.:  ", rows)
    print()

    """     Pattern for filling up the ZigZag matrix     
                1. it fills the first column with num. of letters as num. of rows   """
    colFill = [rows]

    for zigFill in range(rows-2):
        """     2. 3... it fills the rest of the columns in pattern with
                    a single letter     """
        colFill.append(1)

    """     colCnt ~ count of needed columns    """
    colCnt = 0
    """     colFillCnt ~ count of the pattern   """
    colFillCnt = 0
    """     colFillLen ~ length of the pattern  """
    colFillLen = len(colFill)

    while strLen > 0:
        strLen -= colFill[colFillCnt]
        colCnt += 1
        colFillCnt += 1

        if colFillCnt == colFillLen:
            """     Return the pattern to its beginning     """
            colFillCnt = 0

    strLen = len(strIn)
    cols = colCnt

    print("\tNum. of cols.:  ", colCnt)
    print()
    print("\tCol fill pattern:", colFill)
    print()
    print("\tZigZag matrix slots:\n")

    zzMat = [[' ' for col in range(cols)] for row in range(rows)]

    for row in zzMat:
        print("\t\t", row)

    """     colFillCnt ~ count of the pattern   """
    colFillCnt = 0
    """     fillCnt ~ count of used characters  """
    fillCnt = 0

    for c in range(cols):
        for r in range(rows):

            if fillCnt >= strLen:
                """     If all the characters from In string were used """
                break

            if colFillCnt == 0:
                """     1. pattern numb.
                            fills the entire column     """

                zzMat[r][c] = strIn[fillCnt]
                fillCnt += 1

                if r == rows-1:
                    """     When column filled
                                shift to next pattern numb.     """
                    colFillCnt += 1

            elif r == rows-1 - colFillCnt:
                """     If matching row for n. pattern numb.
                            fill the space      """

                zzMat[r][c] = strIn[fillCnt]
                fillCnt += 1
                colFillCnt += 1

                if colFillCnt == colFillLen:
                    """     Return the pattern to its beginning     """
                    colFillCnt = 0

                """     Skip to next column     """
                break

            if colFillCnt == colFillLen:
                """     Return the pattern to its beginning     """
                colFillCnt = 0

    print("\n\tZigZag matrix filled:")
    strOut = ""

    for row in zzMat:
        print("\n", end="\t\t ")
        for col in row:
            print(col, end=" ")
            if col != " ":
                strOut += col
    print("\n")

    print("\tOut string:", strOut)

    print("\n")

print("1. Function solution:\n")

for encode in Input_encodeLst:
    strIn = encode[0]
    rows = encode[1]

    ZigZagEncode_Prt(strIn, rows)

    strOut = ZigZagEncodeV1_Sol(strIn, rows)
    print("\t\tOut string: ", strOut)
    print("\n")


print("2. Function solution:\n")

for encode in Input_encodeLst:
    strIn = encode[0]
    rows = encode[1]

    strLen = len(strIn)

    print("\tIn string:      ", strIn)
    print("\t\tStr. len.:  ", strLen)
    print("\tNum. of rows.:  ", rows)
    print()

    strOut = ZigZagEncodeV2_Sol(strIn, rows)
    print("\t\tOut string: ", strOut)
    print("\n")