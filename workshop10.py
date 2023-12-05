def welcome_student(year):
    if year == 1:
        print("Welcome Freshman")
    elif year == 2:
        print("Welcome Sophomore")
    elif year == 3:
        print("Welcome Junior")
    elif year == 4:
        print("Welcome Senior")
    else:
        print("ป้อนข้อมูลชั้นปีไม่ถูกต้อง")

# Input student's year
student_year = int(input("ป้อนชั้นปีของนักศึกษา (1-4): "))

# Display welcome message
welcome_student(student_year)
