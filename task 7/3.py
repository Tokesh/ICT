import math
weight = float(input())
height = float(input())
index = math.ceil(weight / (height * height))
s = ""
if(index < 18.5): s = "underweight"
elif(index >= 18.5 and index < 25): s = "normal weight"
elif(index >= 25 and index < 30): s = "slightly weight"
elif(index >= 30 and index < 35): s = "obese weight"
else: s="clinically obese"
print("Your BMI is %d, you are "%index, s, sep='')