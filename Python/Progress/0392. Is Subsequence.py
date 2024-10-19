"""
392. Is Subsequence

https://leetcode.com/problems/is-subsequence/description/


    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
    of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a
    subsequence of "abcde" while "aec" is not).


    Example 1:

        Input: s = "abc", t = "ahbgdc"

        Output: true

    Example 2:

        Input: s = "axc", t = "ahbgdc"

        Output: false


    Constraints:

        0 <= s.length <= 100
        0 <= t.length <= 10^4
        s and t consist only of lowercase English letters.


    Topics:

        Two Pointers
        String
        Dynamic Programming


    Courses:

        LeetCode 75

"""


if __name__ == "__main__":

    InputLst = [["abc", "ahbgdc"],
                ["axc", "ahbgdc"]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Sbs = case[0]
        Srt = case[1]

        lng_sbs = len(Sbs)
        lng_srt = len(Srt)

        print(f"\tSubset: {Sbs}")
        print(f"\t\tLength: {lng_sbs}")
        print(f"\tString: {Srt}")
        print(f"\t\tLength: {lng_srt}")
        print()

        cnt_sbs = 0

        print("\t\tCommon characters:")
        for idx, crc in enumerate(Srt):

            if crc == Sbs[cnt_sbs]:
                cnt_sbs += 1

                print(f"\t\t\tSrt[{idx+1}] = Sbs[{cnt_sbs-1}] = {crc}")

        print("\n")
