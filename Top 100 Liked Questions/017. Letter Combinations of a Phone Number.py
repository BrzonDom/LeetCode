"""
17. Letter Combinations of a Phone Number

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
    represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to
    any letters.

    Example 1:

        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Example 2:

        Input: digits = ""
        Output: []

    Example 3:

        Input: digits = "2"
        Output: ["a","b","c"]

    Constraints:

        0 <= digits.length <= 4
        digits[i] is a digit in the range ['2', '9'].

"""
import itertools


Input_numComb = ["23", "", "2"]

phoneConv = {"2": ["a", "b", "c"],
             "3": ["d", "e", "f"],
             "4": ["g", "h", "i"],
             "5": ["j", "k", "l"],
             "6": ["m", "n", "o"],
             "7": ["p", "q", "r", "s"],
             "8": ["t", "u", "v"],
             "9": ["w", "x", "y", "z"]}


print("Driver solution:")

for numCnt, numComb in enumerate(Input_numComb):

    print(f"{numCnt+1}. case:\n")

    print(f"\t\"{numComb}\"\n")

    lenComb = len(numComb)

    if lenComb:
        for dig in numComb:
            print(f"\t{dig}: {phoneConv[dig]}")
        print()

    if lenComb == 1:

        for letter in phoneConv[numComb]:
            print("\t\t", letter)
        print()

    elif lenComb == 2:
        letterComb = list(itertools.product(phoneConv[numComb[0]], phoneConv[numComb[1]]))

        letterComb = ["".join(elem) for elem in letterComb]

        for comb in letterComb:
            print("\t\t", comb)
        print()

    elif lenComb == 3:
        letterComb = list(itertools.product(phoneConv[numComb[0]], phoneConv[numComb[1]],
                                            phoneConv[numComb[2]]))

        letterComb = ["".join(elem) for elem in letterComb]

        for comb in letterComb:
            print("\t\t", comb)
        print()

    elif lenComb == 4:
        letterComb = list(itertools.product(phoneConv[numComb[0]], phoneConv[numComb[1]],
                                            phoneConv[numComb[2]], phoneConv[numComb[3]]))

        letterComb = ["".join(elem) for elem in letterComb]

        for comb in letterComb:
            print("\t\t", comb)
        print()

    print()
