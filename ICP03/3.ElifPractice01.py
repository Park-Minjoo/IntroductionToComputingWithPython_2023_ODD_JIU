height = eval(input("Enter your height(m) : "))
weight = eval(input("Enter your weight: "))

bmi = weight / (height ** 2)
print("BMI:", bmi)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Overweight")

