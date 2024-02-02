'''
This function should return 2 values: 
- the BMI category (ex. "underweight") 
- the actual BMI value (ex. 22.86)

Reminders: 
- calculate bmi before returning outputs 
- add error checking for invalid input and unrealistic information
'''
def bmi_check(weight, height):
#Using try catch here to avoid ValueError when detecting for errors when the user input string
    try:
        #Convert all the input from main.py to float datatype to do the calculation
        weight = float(weight)
        height = float(height)
        
        #Check for invalid input such as negative weight and height
        if weight <= 0 or height < 0:
            return "invalid input"
        #Check for unrealistic weight and height as per the Flowchart
        elif weight > 650 or height > 2.72:
            return "unrealistic information"
        
        #BMI calculation
        bmi = weight / height ** 2
        
        #Check the BMI index to return the user's body status and also BMI index
        if bmi < 18.5: 
            return "underweight", round(bmi, 1)
        elif bmi <= 24.9: 
            return "normal", round(bmi, 1)
        elif bmi <= 29.9: 
            return "overweight", round(bmi, 1)
        elif bmi < 40: 
            return "obese", round(bmi, 1)
        elif bmi > 40:
            return "extremely obese", round(bmi, 1)
    except ValueError:
        return "invalid input"