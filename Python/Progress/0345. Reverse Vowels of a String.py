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

        vwls = ('a', 'e', 'i', 'o', 'u',
                'A', 'E', 'I', 'O', 'U')

        for crc in Srt:

            if crc in vwls:
                print(crc)

        print("\n")
