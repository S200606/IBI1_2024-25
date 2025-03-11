#calculate BMI
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
BMI = weight / (height ** 2)
print("Your BMI is", str(BMI))
#decide whether the person is underweight, normal weight or overweight
if BMI < 18.5:
    print("You are underweight.")
elif BMI < 30:
    print("You are normal weight.")
else:
    print("You are overweight.")