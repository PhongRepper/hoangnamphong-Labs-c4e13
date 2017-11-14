numbers = [1, 2, 4, 6 ,7 ,8, 19]
x = int(input("Which number do yo wanna search? "))
Start = 0
Stop = len(numbers) - 1
found_index = -1
while Start != Stop:
    mid = (Start + Stop) // 2
    if x == numbers[mid]:
        found_index = mid
        break
    else:
        if mid == Start or mid == Stop:
            break
        elif x < numbers[mid]:
            Stop = mid
        else:
            Start = mid

if found_index == -1:
    print("Not found")
else:
    print("Found", x, "at", found_index)

#     # if mid < x:
#     #     Start = mid
#     #
#     # if mid > x:
#     #     Stop = mid
#     if numbers[mid] == x:
#         print("")
#         break
# else:
#     if numbers[mid] < x:
#         Start = numbers[mid]
#     else:
#
#
#     break
