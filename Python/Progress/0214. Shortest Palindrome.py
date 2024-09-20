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


def Brt01_WhlRvs_PlnChck_Prt(Str):

    print(f"\tString: {Str}")

    rmn_Str = Str
    sfx_Str = ""


def Hlp01_PlnChck(Str):

    lft, rgh = 0, len(Str) - 1

    while lft < rgh:

        if Str[lft] != Str[rgh]:
            return False

        lft += 1
        rgh -= 1

    return True


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
                print()

                break

            sfx_Str = rmn_Str[-1] + sfx_Str
            rmn_Str = rmn_Str[:-1]

        pfx_Str = sfx_Str[::-1]
        pld_Str = pfx_Str + rmn_Str + sfx_Str

        print(f"\tPalindrome: {pld_Str}")
        print(f"\t\tPrefix:    {pfx_Str}")
        print(f"\t\tRemainder: {rmn_Str}")
        print(f"\t\tSuffix:    {sfx_Str}")

        print("\n")
