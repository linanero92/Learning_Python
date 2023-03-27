# BMI Calculator

"""
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9

Sample Output
Normal

Weight is in kg, height is in meters.
Note, that height is a float.
"""

w = input()
h = input()
weight = int(w)
height = float(h)
if weight / (height**2) < 18.5:
    print("Underweight")
elif 18.5 <= weight / (height**2) < 25:
    print("Normal")
elif 25 <= weight / (height**2) < 30:
    print("Overweight")
elif weight / (height**2) >= 30:
    print("Obesity")