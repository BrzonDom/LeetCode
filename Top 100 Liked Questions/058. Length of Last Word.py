"""
58. Length of Last Word

https://leetcode.com/problems/length-of-last-word/description/

    Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal substring consisting of non-space characters only.


    Example 1:

        Input: s = "Hello World"
        Output: 5
        Explanation: The last word is "World" with length 5.

    Example 2:

        Input: s = "   fly me   to   the moon  "
        Output: 4
        Explanation: The last word is "moon" with length 4.

    Example 3:

        Input: s = "luffy is still joyboy"
        Output: 6
        Explanation: The last word is "joyboy" with length 6.


    Constraints:

        1 <= s.length <= 10^4
        s consists of only English letters and spaces ' '.
        There will be at least one word in s.

"""
import copy

if __name__ == "__main__":

    InputLst = ["Hello World",
                "   fly me   to   the moon  ",
                "luffy is still joyboy"]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt+1}.Case\n")

        InStr = case

        print(f"\tString: \"{InStr}\"")
        print()

        rawStr = InStr
        stpStr = copy.deepcopy(InStr)

        for idx, chr in enumerate(rawStr):

            if chr != " ":
                stpStr = rawStr[idx:]
                break

        for idx, chr in enumerate(rawStr[::-1]):

            if chr != " ":
                if idx == 0:
                    break

                stpStr = stpStr[:-idx]
                break

        print(f"\t\tStripped String: \"{stpStr}\"")
        print()

        wrdStr = copy.deepcopy(stpStr)
        wrdLst = []
        wrd = ""

        for idx, chr in enumerate(wrdStr):

            if chr == " ":
                if wrd:
                    wrdLst.append(wrd)
                    wrd = ""

            else:
                wrd += chr

        print("\t\tWords:")
        print(f"\t\t\t{wrdLst}")

        print("\n")
