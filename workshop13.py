def check_student_grades():
    num_students = int(input("ป้อนจำนวนนักเรียนที่ต้องการตรวจสอบ: "))
    for i in range(num_students):
        student_id = input(f"รหัสนักเรียนที่ {i+1}: ")
        student_name = input(f"ชื่อนักเรียนที่ {i+1}: ")
        grade = float(input(f"เกรดเฉลี่ยของนักเรียนที่ {i+1}: "))
        
        if grade < 2.00:
            print(f"นักเรียน {student_name} รหัส {student_id} สอบไม่ผ่าน")
        else:
            print(f"นักเรียน {student_name} รหัส {student_id} สอบผ่าน")

check_student_grades()
