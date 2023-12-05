def calculate_net_salary(salary):
    tax = salary * 7 / 100
    social_security = 500
    net_salary = salary - tax - social_security
    return net_salary

# Input employee information
employee_id = input("ป้อนรหัสพนักงาน: ")
employee_name = input("ป้อนชื่อพนักงาน: ")
basic_salary = float(input("ป้อนเงินเดือนปกติของพนักงาน: "))

# Calculate net salary and display the result
net_salary_result = calculate_net_salary(basic_salary)
print(f"รหัสพนักงาน: {employee_id}")
print(f"ชื่อพนักงาน: {employee_name}")
print(f"เงินเดือนสุทธิ: {net_salary_result}")
