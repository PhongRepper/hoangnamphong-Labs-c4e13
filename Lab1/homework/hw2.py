prime = int(input("Enter a number: "))

if prime > 1:
    for p in range (2, prime):
        if prime % p == 0:
            print(prime, "is not a prime number")
        elif prime == 2:
            print("2 is a prime number")
        else:
            print(prime, "is a prime number")
        break
else:
    print(prime, "is not a prime number")
