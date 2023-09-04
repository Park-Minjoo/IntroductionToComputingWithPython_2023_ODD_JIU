# Input the score
score = int(input("Enter your score: "))

# Input the evaluation method (PF or grade)
evaluation_method = input("Enter the evaluation method (PF or grade): ")

# Check the evaluation method and print the corresponding result
if evaluation_method == "PF":
    if score >= 70:
        print("Pass")
    else:
        print("Fail")
elif evaluation_method == "grade":
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("F")
