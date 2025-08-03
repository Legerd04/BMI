weight =float(input("Enter the weight in kg: "))
height = float(input("Enter the height in meters: "))

print("Calculating BMI...")
bmi = weight / (height ** 2)
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

