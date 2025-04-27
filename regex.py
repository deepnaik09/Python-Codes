import re

def verify_roll_number(roll_no):
    pattern = r"^(21|22)(AD|AM|CE|CC|IT)\d{4}$"
    if re.fullmatch(pattern, roll_no):
        print("Attendance marked successfully!")
    else:
        print("Invalid roll number!")

# Taking input from user
roll_no = input("Enter your roll number: ")
verify_roll_number(roll_no)
