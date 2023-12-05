def calculate_phone_bill(name, phone_number, minutes):
    if minutes >= 1 and minutes <= 15:
        cost = minutes * 5
    elif minutes <= 30:
        cost = 15 * 5 + (minutes - 15) * 3
    else:
        cost = 15 * 5 + 15 * 3 + (minutes - 30) * 1.50

    print(f"คุณ {name} (เบอร์โทร {phone_number}) ใช้โทรศัพท์ {minutes} นาที ค่าใช้จ่ายคือ {cost} บาท")

# Input phone usage information
user_name = input("ป้อนชื่อผู้ใช้โทรศัพท์: ")
phone_num = input("ป้อนหมายเลขโทรศัพท์: ")
used_minutes = int(input("ป้อนจำนวนนาทีที่ใช้: "))

# Calculate and display phone bill
calculate_phone_bill(user_name, phone_num, used_minutes)
