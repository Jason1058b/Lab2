def calculate_bmi(weight, height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    weight = float(weight)
    height = float(height)

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        print("Under Weight, -1")
    elif bmi <= 25.0:
        print("Normal Weight, 0")
    else:
        print("Over Weight, 1")

    return bmi


bmi = calculate_bmi(weight="57", height="1.73")
print("BMI = " + str(bmi))