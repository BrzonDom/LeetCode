"""
3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

    Given a string s, find the length of the longest
    substring without repeating characters.

    Example 1:

        Input: s = "abcabcbb"
        Output: 3

        Explanation: The answer is "abc", with the length of 3.

    Example 2:

        Input: s = "bbbbb"
        Output: 1

        Explanation: The answer is "b", with the length of 1.

    Example 3:

        Input: s = "pwwkew"
        Output: 3

        Explanation: The answer is "wke", with the length of 3.
            Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Constraints:

        0 <= s.length <= 5 * 10⁴
        s consists of English letters, digits, symbols and spaces.
"""

def subStrLen_Sol(string):

    subLen = 0
    maxSubLen = 0

    used = set()

    for char in string:
        if char not in used:

            subLen += 1

            used.add(char)

        else:
            if subLen > maxSubLen:
                maxSubLen = subLen

            subLen = 1

            used.clear()
            used.add(char)

    if subLen > maxSubLen:
        return subLen

    else:
        return maxSubLen


Input_strLst = ["abcabcbb",
                "bbbbb",
                "pwwkew",
                "dvdf"]


print("Substring print:\n")

for string in Input_strLst:

    print("\tString: ", string)
    print()

    for c in range(len(string)):
        print("\t\t", string[c:])

    print("\n")


print("Driver solution:\n")

for string in Input_strLst:

    print("\tString: ", string)

    subLen = 0
    maxSubLen = 0

    used = set()


    for c in range(len(string)):
        used.clear()
        subLen = 0

        print("\n\t", end="\t")

        for char in string[c:]:

            if char not in used:
                print(char, end="")

                used.add(char)
                subLen += 1

            else:
                # print("\n\t", end="\t")
                # print(char, end="")

                if subLen > maxSubLen:
                    maxSubLen = subLen

                break

                # used.clear()
                # used.add(char)
                # subLen = 1

        if subLen > maxSubLen:
            maxSubLen = subLen

    print("\n\n\tMax len of substring: ", maxSubLen)
    print("\n")

print("Function solve solution:\n")

for string in Input_strLst:

    print("\tString: ", string)
    print()

    print("\t\tMax len of substring: ", subStrLen_Sol(string))
    print("\n")







