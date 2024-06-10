import re

def assess_pass_strength(password):
    #Criteria
    length_criteria= len(password) >= 8
    uppercase_criteria= bool(re.search(r'[A-Z]', password))
    lowercase_criteria= bool(re.search(r'[a-z]', password))
    number_criteria= bool(re.search(r'[0-9]', password))
    special_char_criteria= bool(re.search(r'[!@#$%^&*]', password))

    #Strength Calc
    strength= sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_char_criteria
    ])

    #Feedback
    feedback=[]
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*).")

    #Strength msg
    if strength== 5:
        strength_msg= "Strong"
    elif strength >= 3:
        strength_msg= "Medium"
    else:
        strength_msg= "Weak"

    return {
        "strength": strength_msg,
        "feedback": feedback
    }

password = input("Enter your password: ")
assessment= assess_pass_strength(password)
print(f"Password Strength: {assessment['strength']}")
if assessment['feedback']:
    print("Feedback:")
    for feedback in assessment['feedback']:
        print(f" - {feedback}")