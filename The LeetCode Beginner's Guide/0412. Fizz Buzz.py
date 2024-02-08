"""
412. Fizz Buzz

https://leetcode.com/problems/fizz-buzz/description/

    Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

    Example 1:

        Input: n = 3
        Output: ["1","2","Fizz"]

    Example 2:

        Input: n = 5
        Output: ["1","2","Fizz","4","Buzz"]

    Example 3:

        Input: n = 15
        Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


    Constraints:

        1 <= n <= 10^4

"""

def Sol_FizzBuzzSort(num):

    answerOut = []
    Fizz = "Fizz"
    Buzz = "Buzz"

    for n in range(1, num+1):

        if (n % 3 == 0) and (n % 5 == 0):
            answerOut.append(Fizz+Buzz)

        elif n % 3 == 0:
            answerOut.append(Fizz)

        elif n % 5 == 0:
            answerOut.append(Buzz)

        else:
            answerOut.append(str(n))

    return answerOut


def FizzBuzzSort(num):

    answerOut = []
    Fizz = "Fizz"
    Buzz = "Buzz"

    print(f"\tFor range {num}")

    for n in range(1, num+1):
        print(f"\t\t {n:2}", end=".\t")

        if (not n % 3) and (not n % 5):
            print(Fizz+Buzz)
            answerOut.append(Fizz+Buzz)

        elif not n % 3:
            print(Fizz)
            answerOut.append(Fizz)

        elif not n % 5:
            print(Buzz)
            answerOut.append(Buzz)

        else:
            print(str(n))
            answerOut.append(str(n))

    return answerOut


Input_num = [3, 5, 15]

print("Driver solution:\n")

for num in Input_num:

    answerOut = []
    Fizz = "Fizz"
    Buzz = "Buzz"

    print(f"\tFor range {num}")

    for n in range(1, num+1):
        print(f"\t\t {n:2}", end=".\t")

        if (not n % 3) and (not n % 5):
            print(Fizz+Buzz)
            answerOut.append(Fizz+Buzz)

        elif not n % 3:
            print(Fizz)
            answerOut.append(Fizz)

        elif not n % 5:
            print(Buzz)
            answerOut.append(Buzz)

        else:
            print(str(n))
            answerOut.append(str(n))

    print(f"\n\t\tFinal String: {answerOut}")
    print()

print("Function solution:\n")

for num in Input_num:

    answerOut = FizzBuzzSort(num)
    answerSol = Sol_FizzBuzzSort(num)

    print(f"\n\t\tFinal String: {answerOut}")
    print(f"\t\tFinal String: {answerOut}")
    print()

