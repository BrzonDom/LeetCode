"""
214. Shortest Palindrome

https://leetcode.com/problems/shortest-palindrome/description/


    You are given a string s. You can convert s to a palindrome by adding characters in front of it.

    Return the shortest palindrome you can find by performing this transformation.


    Example 1:

        Input: s = "aacecaaa"

        Output: "aaacecaaa"

    Example 2:

        Input: s = "abcd"

        Output: "dcbabcd"


    Constraints:

        0 <= s.length <= 5 * 10^4
        s consists of lowercase English letters only.


    Topics:

        String
        Rolling Hash
        String Matching
        Hash Function


    Courses:

        Daily: 2024/09/20

"""


def Hlp01_PlnChck(Str):

    return Str == Str[::-1]


if __name__ == "__main__":

    InputLst = ["aacecaaa",
                "abcd"]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Str = case

        print(f"\tString: {Str}")
        print()

        rmn_Str = Str
        sfx_Str = ""

        while rmn_Str:

            fnd_Pln = Hlp01_PlnChck(rmn_Str)

            if fnd_Pln:
                print(f"\t\tRemaining string: {rmn_Str}")
                print(f"\t\t\tSuffix of string: {sfx_Str}")

                break

            sfx_Str = rmn_Str[-1] + sfx_Str
            rmn_Str = rmn_Str[:-1]

        pfx_Str = sfx_Str[::-1]

        print("\n")
