numbers = [1, 3, 4,23, -47, 68 , 37, 3, 3 ,3,3, 37]
print(numbers)
find = int(input("Enter a number: "))

# number_count = {}
number_count = 0

if find in numbers:
    for index, number in enumerate(numbers):
        if find == number:
            number_count += 1
    # else:
    #     number_count = 1
    print(find, "appears", number_count, "times in my list")

else:
    print(find, "appears 0 times in my list")
