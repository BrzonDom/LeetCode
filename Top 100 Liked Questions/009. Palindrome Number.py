"""
9. Palindrome Number

https://leetcode.com/problems/palindrome-number/description/

    Given an integer x, return true if x is a palindrome, and false otherwise.

    Example 1:

        Input: x = 121
        Output: true

        Explanation:
            121 reads as 121 from left to right and from right to left.

    Example 2:

        Input: x = -121
        Output: false

        Explanation:
            From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:

        Input: x = 10
        Output: false

        Explanation:
            Reads 01 from right to left. Therefore it is not a palindrome.

    Constraints:

        -2³¹ <= x <= 2³¹ - 1
"""

def palindromeNum_Sol(num):

    revNum = str(num)
    revNum = revNum[::-1]

    return revNum == str(num)


def palindromeNum_Prt(num):
    print("\tIn num.: ", num)

    revNum = str(num)
    revNum = revNum[::-1]

    print("\tRev num.:", revNum)
    print()

    if revNum == str(num):

        print("\t\tNumber IS a palindrome")
        return True

    else:

        print("\t\tNumber is NOT a palindrome")
        return False


Input_numLst = [121, -121, 10]

print("Driver print:\n")

for num in Input_numLst:
    print("\tNum: ", num)
    print()

print("Dirver solution:\n")

for num in Input_numLst:
    print("\tIn num.: ", num)

    revNum = str(num)
    revNum = revNum[::-1]

    print("\tRev num.:", revNum)
    print()

    if revNum == str(num):
        print("\t\tNumber IS a palindrome")
    else:
        print("\t\tNumber is NOT a palindrome")

    print("\n")

print("Function solution:\n")

for num in Input_numLst:

    palindromeNum_Prt(num)

    isPal = palindromeNum_Sol(num)

    if isPal:
        print("\t\t\tNumber IS a palindrome")
    else:
        print("\t\t\tNumber is NOT a palindrome")

    print("\n")