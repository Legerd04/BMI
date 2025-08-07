weight =float(input("Enter the weight in kg: "))
height = input("Enter the height in feet and inches: ")
print("Calculating BMI...")
height = height.strip().replace('"', '')
fi = [] # List or array created to hold feet and inches
fi = (height.split("'"))
m = float(fi[0]) * 0.3048 + float(fi[1]) * 0.0254
bmi = weight / (m ** 2)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
elif bmi >= 30:
    print("You are obese.")
print("BMI calculation completed.")
