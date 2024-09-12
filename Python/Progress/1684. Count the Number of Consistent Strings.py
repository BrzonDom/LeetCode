"""
1684. Count the Number of Consistent Strings

https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

        Daily: 2024/09/12


    You are given a string allowed consisting of distinct characters and an array of strings words. A string is
    consistent if all characters in the string appear in the string allowed.

    Return the number of consistent strings in the array words.


    Example 1:

        Input: allowed = "ab", words = ["ad", "bd", "aaab", "baa", "badab"]

        Output: 2

        Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

    Example 2:

        Input: allowed = "abc", words = ["a", "b", "c", "ab", "ac", "bc", "abc"]

        Output: 7

        Explanation: All strings are consistent.

    Example 3:

        Input: allowed = "cad", words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]

        Output: 4

        Explanation: Strings "cc", "acd", "ac", and "d" are consistent.


    Constraints:

        1 <= words.length <= 10^4
        1 <= allowed.length <= 26
        1 <= words[i].length <= 10
        The characters in allowed are distinct.
        words[i] and allowed contain only lowercase English letters.


    Topics:

        Array
        Hash Table
        String
        Bit Manipulation
        Counting

"""


if __name__ == "__main__":

    InputLst = [["ab", ["ad", "bd", "aaab", "baa", "badab"]],
                ["abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]],
                ["cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Alw = case[0]
        Strs = case[1]

        print(f"\tAllowed characters: {Alw}")
        print(f"\tString list: {Strs}")
        print()

        print("\tStrings:")
        for st in Strs:
            print(f"\t\t{st}")
        print()

        cnss = []
        inCnss = []
        cnsCnt = 0

        for st in Strs:
            fndCn = True

            for ch in st:
                if ch not in Alw:
                    fndCn = False

                    inCnss.append(st)
                    break

            if fndCn:
                cnss.append(st)
                cnsCnt += 1

        print("\tInconsistent strings:")
        for st in inCnss:
            print(f"\t\t{st}")

        for st in cnss:
            print(st)

        print("\n")
