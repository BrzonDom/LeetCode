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


def contVol_Prt(heights):

    print("\tHeights:", heights)
    print()

    """     maxVol ~ Maximal volume of the container    """
    maxVol = 0
    """     maxVolDim ~ Dimensions of the maximal volume of the container"""
    maxVolDim = []

    for posBs in range(len(heights)):

        """     posBs ~ Base position, 1. position of a boarder of the container     """
        """     heiBs ~ Base height, 1. height of a boarder of the container     """
        heiBs = heights[posBs]

        """     pos ~ Next position, 2. position of a boarder of the container    """
        pos = posBs

        for hei in heights[posBs + 1:]:
            pos += 1

            """     hei ~ Next border, 2. height of a boarder of the container   """
            print(f"\t\t [{heiBs}, {posBs}] [{hei}, {pos}]")

            """     min(hei, heiBs) ~ Height of the container     """
            """     pos - posBs ~ Width of the container    """
            print(f"\t\t\tCont. height / width:  {min(hei, heiBs)} / {(pos - posBs)}")

            """     vol ~ Volume of the container   
                        Volume = Height * Width     """
            vol = min(hei, heiBs) * (pos - posBs)
            print("\t\t\tCont. volume: ", vol)

            if vol >= maxVol:
                maxVol = vol
                maxVolDim = [min(hei, heiBs), pos - posBs]
        print()

    print("\tMax cont. volume:", maxVol)
    print(f"\t\tMax cont. height / width: {maxVolDim[0]} / {maxVolDim[1]}")

    print("\n")


Input_heightLst = [[1, 8, 6, 2, 5, 4, 8, 3, 7],
                   [1, 1]]

print("Driver print:\n")

for heights in Input_heightLst:
    print("\tHeights:", heights)
    print()

    borDim = []

    print("\t\t[height, position]")

    for pos, hei in enumerate(heights):
        borDim.append([hei, pos])

    print("\t\t", borDim)
    print("\n")


print()
print("Driver solution:\n")

for heights in Input_heightLst:
    print("\tHeights:", heights)
    print()

    """     borDim ~ Border dimensions  """
    borDim = []

    print("\t\t[height, position]")
    for pos, hei in enumerate(heights):
        borDim.append([hei, pos])

    print("\t\t", borDim)
    print("\n")

    """     maxVol ~ Maximal volume of the container    """
    maxVol = 0
    """     maxVolDim ~ Dimensions of the maximal volume of the container"""
    maxVolDim = []

    for posBs in range(len(heights)):

        """     posBs ~ Base position, 1. position of a boarder of the container     """
        """     heiBs ~ Base height, 1. height of a boarder of the container     """
        heiBs = heights[posBs]

        """     pos ~ Next position, 2. position of a boarder of the container    """
        pos = posBs

        for hei in heights[posBs + 1:]:
            pos += 1

            """     hei ~ Next border, 2. height of a boarder of the container   """
            print(f"\t\t [{heiBs}, {posBs}] [{hei}, {pos}]")

            """     min(hei, heiBs) ~ Height of the container     """
            """     pos - posBs ~ Width of the container    """
            print(f"\t\t\tCont. height / width:  {min(hei, heiBs)} / {(pos - posBs)}")

            """     vol ~ Volume of the container   
                        Volume = Height * Width     """
            vol = min(hei, heiBs) * (pos - posBs)
            print("\t\t\tCont. volume: ", vol)

            if vol >= maxVol:
                maxVol = vol
                maxVolDim = [min(hei, heiBs), pos - posBs]
        print()

    print("\tMax cont. volume:", maxVol)
    print(f"\t\tMax cont. height / width: {maxVolDim[0]} / {maxVolDim[1]}")

    print("\n")

print()
print("Function solution:\n")

for heights in Input_heightLst:

    contVol_Prt(heights)
