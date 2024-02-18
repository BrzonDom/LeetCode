"""
11. Container With Most Water

https://leetcode.com/problems/container-with-most-water/description/

    You are given an integer array height of length n.
    There are n vertical lines drawn such that
    the two endpoints of the i-th line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container,
    such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    Example 1:

        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49

        Explanation:
            The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
            In this case, the max area of water the container can contain is 49.


    Example 2:

        Input: height = [1,1]
        Output: 1

    Constraints:

        n == height.length
        2 <= n <= 10⁵
        0 <= height[i] <= 10⁴

"""

def contVol_Prt(heigh):

    print("\tHeights:", heighs)
    print()

    heiDim = []

    print("\t\t[height, position]")
    for h, hei in enumerate(heighs):
        heiDim.append([hei, h])

    print("\t\t", heiDim)
    print("\n")

    maxVol = 0
    maxVolDim = []

    for h in range(len(heiDim)):

        heiBs = heiDim[h]

        for hei in heiDim[h+1:]:
            print("\t\t", heiBs, hei)
            print(f"\t\t\tCont. height / width:  {min(hei[0], heiBs[0])} / {(hei[1] - heiBs[1])}")

            vol = min(hei[0], heiBs[0]) * (hei[1] - heiBs[1])
            print("\t\t\tCont. volume: ", vol)

            if vol >= maxVol:
                maxVol = vol
                maxVolDim = [min(hei[0], heiBs[0]), hei[1] - heiBs[1]]
        print()

    print("\tMax cont. volume:", maxVol)
    print(f"\t\tMax cont. height / width: {maxVolDim[0]} / {maxVolDim[1]}")

    print("\n")


Input_heighLst = [[1, 8, 6, 2, 5, 4, 8, 3, 7],
                  [1, 1]]

print("Driver print:\n")

for heighs in Input_heighLst:
    print("\tHeights:", heighs)
    print()

    heiDim = []

    print("\t\t[height, position]")

    for h, hei in enumerate(heighs):
        heiDim.append([hei, h])

    print("\t\t", heiDim)
    print("\n")


print()
print("Driver solution:\n")

for heighs in Input_heighLst:
    print("\tHeights:", heighs)
    print()

    heiDim = []

    print("\t\t[height, position]")
    for h, hei in enumerate(heighs):
        heiDim.append([hei, h])

    print("\t\t", heiDim)
    print("\n")

    maxVol = 0
    maxVolDim = []

    for h in range(len(heiDim)):

        heiBs = heiDim[h]

        for hei in heiDim[h+1:]:
            print("\t\t", heiBs, hei)
            print(f"\t\t\tCont. height / width:  {min(hei[0], heiBs[0])} / {(hei[1] - heiBs[1])}")

            vol = min(hei[0], heiBs[0]) * (hei[1] - heiBs[1])
            print("\t\t\tCont. volume: ", vol)

            if vol >= maxVol:
                maxVol = vol
                maxVolDim = [min(hei[0], heiBs[0]), hei[1] - heiBs[1]]
        print()

    print("\tMax cont. volume:", maxVol)
    print(f"\t\tMax cont. height / width: {maxVolDim[0]} / {maxVolDim[1]}")

    print("\n")

print()
print("Function solution:\n")

for heighs in Input_heighLst:

    contVol_Prt(heighs)
