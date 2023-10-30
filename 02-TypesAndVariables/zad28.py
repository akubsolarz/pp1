cm = int(input(" Enter your height in cm: "))
kg = int(input(" Enter your weight in kg: "))
bmi = kg / (cm / 100)**2
print(f" Your BMI index: {bmi} \n Correct weight: {18.5<bmi<25}")