# 1st input: enter height in meters e.g: 1.65
height = float(input("Enter height in meters: "))
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input("Enter weight in kilograms: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

BMI = weight / (height ** 2)

#print(BMI)

print(int(BMI))

if BMI > 25:
    print("You are fat!")

elif BMI < 19:
    print("You are skinny!")
else:
    print("You are fit!")
