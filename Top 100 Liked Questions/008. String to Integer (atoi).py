"""
8. String to Integer (atoi)

https://leetcode.com/problems/string-to-integer-atoi/description/

    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

    The algorithm for myAtoi(string s) is as follows:

        1. Read in and ignore any leading whitespace.

        2. Check if the next character (if not already at the end of the string)
            is '-' or '+'. Read this character in if it is either.
            This determines if the final result is negative or positive respectively.
            Assume the result is positive if neither is present.

        3. Read in next the characters until the next non-digit character
            or the end of the input is reached. The rest of the string is ignored.

        4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
            If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

        5. If the integer is out of the 32-bit signed integer range [-2³¹, 2³¹ - 1],
            then clamp the integer so that it remains in the range. Specifically,
            integers less than -2³¹ should be clamped to -2³¹,
            and integers greater than 2³¹ - 1 should be clamped to 2³¹ - 1.

        6. Return the integer as the final result.

        Note:

            Only the space character ' ' is considered a whitespace character.
            Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


    Example 1:

        Input: s = "42"
        Output: 42

        Explanation: The underlined characters are what is read in, the caret is the current reader position.

            Step 1: "42" (no characters read because there is no leading whitespace)
                     ^
            Step 2: "42" (no characters read because there is neither a '-' nor '+')
                     ^
            Step 3: "42" ("42" is read in)
                       ^
            The parsed integer is 42.
            Since 42 is in the range [-231, 231 - 1], the final result is 42.

    Example 2:

        Input: s = "   -42"
        Output: -42

        Explanation:

            Step 1: "   -42" (leading whitespace is read and ignored)
                        ^
            Step 2: "   -42" ('-' is read, so the result should be negative)
                         ^
            Step 3: "   -42" ("42" is read in)
                           ^
            The parsed integer is -42.
            Since -42 is in the range [-231, 231 - 1], the final result is -42.

    Example 3:

        Input: s = "4193 with words"
        Output: 4193

        Explanation:

            Step 1: "4193 with words" (no characters read because there is no leading whitespace)
                     ^
            Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
                     ^
            Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
                         ^
            The parsed integer is 4193.
            Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

    Constraints:

        0 <= s.length <= 200
        s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

"""

Input_strNumLst = ["42", "   -42", "4193 with words",
                   "     -a"]

print("Driver print:\n")

for strNum in Input_strNumLst:

    print(f"\tIn str num.: \"{strNum}\"")
    print()
print()

print("Driver solution:\n")

for strNum in Input_strNumLst:
    print(f"\tIn str num.: \"{strNum}\"")
    print()

    """     Read in and ignore any leading whitespace.  """
    print("\t\t1.Step:")

    if strNum[0] == ' ':
        print(f"\t\t\t\"{strNum}\" -> ", end="")

        while True:
            if strNum[0] == ' ':
                strNum = strNum[1:]

            else:
                break

        print(f"\"{strNum}\"")

    else:
        print("\t\t\tNo leading white spaces found")

    print()

    """     Check if the next character is '-' or '+'
                (if not at the end of the string)   """
    print("\t\t2.Step:")

    negat = False

    if len(strNum):
        if strNum[0] == '-':
            negat = True
            strNum = strNum[1:]
            print("\t\t\tNegative sign read")

        elif strNum[0] == '+':
            negat = False
            strNum = strNum[1:]
            print("\t\t\tPlus sign read")

        else:
            print("\t\t\tNo sign read")


    else:
        print("\t\t\tString is empty")

    print()

    """     Read in next the characters until the next non-digit character      
                or the end of the input is reached.     """
    print("\t\t3.Step:")

    digCnt = 0

    for char in strNum:

        if '0' <= char <= '9':
            digCnt += 1

        else:
            break

    print(f"\t\t\t\"{strNum}\" -> \"{strNum[:digCnt]}\"")
    strNum = strNum[:digCnt]

    print()

    """     Convert these digits into an integer    
                If no digits were read, then the integer is 0   """
    print("\t\t4.Step:")

    if len(strNum):
        num = int(strNum)

        if negat:
            num *= -1
    else:
        num = 0

    print(f"\t\t\tNum: {num}")
    print()


    print()

