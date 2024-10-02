"""
345. Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/description/


    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


    Example 1:

        Input: s = "IceCreAm"

        Output: "AceCreIm"

        Explanation:
            The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

    Example 2:

        Input: s = "leetcode"

        Output: "leotcede"


    Constraints:

        1 <= s.length <= 3 * 10^5
        s consist of printable ASCII characters.


    Topics:

        Two Pointers
        String


    Courses:

        LeetCode 75

"""


if __name__ == "__main__":

    InputLst = ["IceCreAm",
                "leetcode"]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Srt = case

        print(f"\tString: {case}")
        print()

        vwls = ('a', 'e', 'i', 'o', 'u',
                'A', 'E', 'I', 'O', 'U')
        vwl_cnt = 1

        print("\t\tVowels in the string:")
        for idx, crc in enumerate(Srt):

            if crc in vwls:
                print(f"\t\t\t{vwl_cnt}. Str[{idx}] = {crc}")

                vwl_cnt += 1

        ln_srt = len(Srt)

        lft = 0
        rgt = ln_srt - 1

        while lft < rgt:

            print(Srt[lft])

            lft += 1
        print()

        lft = 0
        rgt = ln_srt - 1

        while lft < rgt:

            print(Srt[rgt])

            rgt -= 1

        print("\n")
