def calculate_commission(employee_id, employee_name, sales_amount):
    if sales_amount <= 1000:
        commission = 0.0
    elif sales_amount <= 2000:
        commission = sales_amount * 0.01
    elif sales_amount <= 3000:
        commission = sales_amount * 0.03
    else:
        commission = sales_amount * 0.05

    print(f"พนักงาน {employee_name} (รหัส {employee_id}) ได้รับค่าคอมมิชชันจากยอดขาย {sales_amount} บาท คือ {commission} บาท")

# Input employee sales information
employee_id = input("ป้อนรหัสพนักงาน: ")
employee_name = input("ป้อนชื่อพนักงาน: ")
sales = float(input("ป้อนยอดขายของพนักงาน: "))

# Calculate and display commission
calculate_commission(employee_id, employee_name, sales)
