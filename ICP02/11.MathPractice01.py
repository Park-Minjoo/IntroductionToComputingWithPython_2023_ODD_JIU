import math

angle = float(input("Enter angle [degrees]: "))

rad = math.radians(angle) # Convert to radians
result_sin = math.sin(rad)
result_cos = math.cos(rad)
result_tan = math.tan(rad)

print("Degree:", angle, ", Radian:", rad)
print("Sine:", result_sin, ", Cosine:", result_cos, ", Tangent:", result_tan)
