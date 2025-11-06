# Healthcare Patient Management System

# Bug 1: Wrong comparison - should use < instead of <=
def check_fever(temperature):
    if temperature < 100.4:  # Bug: should be < not <=
        return "Normal"
    else:
        return "Fever detected"

# Bug 2: Missing return statement
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    # Bug: missing return statement
    
# Bug 3: Wrong operator - should be 'or' not 'and'
def check_emergency(heart_rate, blood_pressure):
    if heart_rate > 120 and blood_pressure > 180:  # Bug: should be 'or' not 'and'
        return "Emergency"
    else:
        return "Normal"

# Bug 4: Off-by-one error in range
def get_age_group(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teen"
    elif age >= 20 and age <= 64:
        return "Adult"
    elif age >= 65:  # Bug: should be age > 64 to avoid gap
        return "Senior"

# Test the functions
print(check_fever(100.4))
print(calculate_bmi(70, 1.75))
print(check_emergency(130, 150))
print(get_age_group(64))
