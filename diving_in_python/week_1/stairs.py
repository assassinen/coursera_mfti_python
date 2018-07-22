import sys

digit_string = int(sys.argv[1])
step = 1
string = []

for i in range(digit_string):
    space_count = digit_string - i - 1
    step_count = digit_string - space_count
    # print(space_count, end = "")
    # print(step_count)

    for y in range(space_count):
        print(" ", end = "")
    for z in range(step_count):
        print("#", end = "")
    print()



# n = 5
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print (" ", end = "")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()