numbers = [1, -2, -48, 48, 26, -1]
minimum = numbers[0]
maximum = numbers[0]
for number in numbers:
    
    if minimum > number:
        minimum = number
print("min is", minimum)

for number in numbers:
    if maximum < number:
        maximum = number
print("max is", maximum)
