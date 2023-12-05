def calculate_tour_package_cost():
    group_leader = input("ชื่อหัวหน้ากรุ๊ปทัวร์: ")
    contact_number = input("เบอร์ติดต่อหัวหน้ากรุ๊ปทัวร์: ")
    group_size = int(input("จำนวนคนที่จะไปทัวร์: "))

    if group_size >= 1 and group_size <= 2:
        package_cost = group_size * 300
    elif group_size <= 5:
        package_cost = group_size * 250
    elif group_size <= 10:
        package_cost = group_size * 210
    else:
        package_cost = group_size * 150

    print(f"ค่าใช้จ่ายในการซื้อแพ็กเกจท่องเที่ยวของกรุ๊ปทัวร์ '{group_leader}' จำนวน {group_size} คน คือ {package_cost} บาท")

calculate_tour_package_cost()
