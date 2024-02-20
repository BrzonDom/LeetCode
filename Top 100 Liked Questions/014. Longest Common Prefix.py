"""
14. Longest Common Prefix

https://leetcode.com/problems/longest-common-prefix/

    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

        Input: strs = ["flower","flow","flight"]
        Output: "fl"

    Example 2:

        Input: strs = ["dog","racecar","car"]
        Output: ""

        Explanation: There is no common prefix among the input strings.

    Constraints:

        1 <= strs.length <= 200
        0 <= strs[i].length <= 200
        strs[i] consists of only lowercase English letters.
"""

Input_strLst = [["flower", "flow", "flight"],
                ["dog", "racecar", "car"]]


print("Driver print:\n")

for strLst in Input_strLst:

    for i, str in enumerate(strLst):

        print(f"\t{i+1}. Str: {str}")

    print("\n")

print()
print("Driver print solution:\n")

for strLst in Input_strLst:

    baseStr = min(strLst, key=len)

    print(f"\tBase str:   {baseStr}")
    print()

    strLst.remove(baseStr)

    for i, str in enumerate(strLst):

        print(f"\t\t{i+1}. Str: {str}")
    print()

    match = True

    print("\tPrefix: \"", end="")

    for c, char in enumerate(baseStr):

        for str in strLst:

            if str[c] != char:
                match = False

        if match:
            print(char, end="")
        else:
            print("\"")
            break

    print("\n")
