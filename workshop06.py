def calculate_interest(name, loan_amount):
    if loan_amount >= 1000:
        interest_rate = 2.5
    else:
        interest_rate = 5.5

    interest = (interest_rate / 100) * loan_amount
    print(f"ผู้กู้ {name} จะได้รับดอกเบี้ยจากเงินกู้ {interest_rate}% ที่มีจำนวน {loan_amount} บาท คือ {interest} บาท")

# Input borrower's information
borrower_name = input("ป้อนชื่อผู้กู้: ")
loan = float(input("ป้อนจำนวนเงินกู้: "))

# Calculate and display interest
calculate_interest(borrower_name, loan)
