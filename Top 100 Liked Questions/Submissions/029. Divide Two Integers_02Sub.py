"""
29. Divide Two Integers

https://leetcode.com/problems/divide-two-integers/

    Given two integers dividend and divisor, divide two integers without using multiplication, division,
    and mod operator.

    The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would
    be truncated to 8, and -2.7335 would be truncated to -2.

    Return the quotient after dividing dividend by divisor.

    Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
    range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1,
    and if the quotient is strictly less than -2^31, then return -2^31.


    Example 1:

        Input: dividend = 10, divisor = 3
        Output: 3

        Explanation: 10/3 = 3.33333.. which is truncated to 3.

    Example 2:

        Input: dividend = 7, divisor = -3
        Output: -2

        Explanation: 7/-3 = -2.33333.. which is truncated to -2.


    Constraints:

        -2^31 <= dividend, divisor <= 2^31 - 1
        divisor != 0

"""


def Sol02_WhlWhlDbl_Prt(case):

    num = case[0]
    div = case[1]

    print(f"\tDividend: {num}")
    print(f"\tDivisor:  {div}")
    print()

    if num:
        if num < 0 and div < 0:
            neg = False

            num = abs(num)
            div = abs(div)

            print(f"\t\tPolarity:  1 ~ Positive")

        elif num > 0 and div < 0:
            neg = True

            div = abs(div)

            print(f"\t\tPolarity: -1 ~ Negative")

        elif num < 0 and div > 0:
            neg = True

            num = abs(num)

            print(f"\t\tPolarity: -1 ~ Negative")

        else:
            neg = False

            print(f"\t\tPolarity:  1 ~ Positive")
        print()

        rem = num
        quo = 0

        while rem >= div:

            tmpDiv = div
            tmpQuo = 1

            while rem >= (tmpDiv + tmpDiv):

                tmpDiv += tmpDiv
                tmpQuo += tmpQuo

            rem -= tmpDiv
            quo += tmpQuo

        if neg:
            quo = max(-quo, -2147483648)

            print(f"\tResult: {-quo}")

        else:
            quo = min(quo, 2147483647)

            print(f"\tResult: {quo}")

    else:

        print(f"\t\tDividend is 0")
        print()

        print(f"\tResult: 0")

    print("\n")


def Sol02_WhlWhlDbl(num, div):

    if num:
        if num < 0 and div < 0:
            neg = False

            num = abs(num)
            div = abs(div)

        elif num > 0 and div < 0:
            neg = True

            div = abs(div)

        elif num < 0 and div > 0:
            neg = True

            num = abs(num)

        else:
            neg = False

        rem = num
        quo = 0

        while rem >= div:

            tmpDiv = div
            tmpQuo = 1

            while rem >= (tmpDiv + tmpDiv):

                tmpDiv += tmpDiv
                tmpQuo += tmpQuo

            rem -= tmpDiv
            quo += tmpQuo

        if neg:

            return max(-quo, -2147483648)

        else:
            return min(quo, 2147483647)

    else:
        return 0


if __name__ == '__main__':

    InputLst = [[10, 3],
                [7, -3],
                [-17, 3],
                [0, 5],
                [-8, -2]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case\n")

        # Sol02_WhlWhlDbl_Prt(case)

        Sol02_WhlWhlDbl(case[0], case[1])
