bacb = int(input("How many B bacterias are there? "))
minutes = int(input("How much time in minutes will we wait? "))

if minutes < 2:
    print("After", minutes, "minutes, we have", bacb, "B bacterias")
else:
    if minutes % 2 == 0:
        tota = minutes * bacb
    else:
        even_min = minutes - 1
        tota = bacb * even_min

    print("After", minutes, "minutes, we have", tota, "B bacterias")
