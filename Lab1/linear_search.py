numbers = [1, 3, 4, 5,6,23, -47, 67]
x = int(input("Enter a numbers "))
# for number in numbers, x in enumerate(numbers):
#
#     if e in numbers:
#         print("found", e, "at", x)
#
#     else:
#         print("not found")
found_index = -1
for index, number in enumerate(numbers):
    if x == number:
        found_index = index
        break

if found_index == -1:
    print("not found")
else:
    print("Found:", found_index)
