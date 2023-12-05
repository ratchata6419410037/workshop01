def check_ph_province(province, ph_value):
    if ph_value >= 7 and ph_value <= 8:
        print(f"จังหวัด {province} มีค่า PH เท่ากับ {ph_value}: Result is Normal")
    elif ph_value > 8:
        print(f"จังหวัด {province} มีค่า PH เท่ากับ {ph_value}: Result is Acid")
    else:
        print(f"จังหวัด {province} มีค่า PH เท่ากับ {ph_value}: Result is Alkali")

# Input province and PH value
province_name = input("ป้อนชื่อจังหวัด: ")
ph_level = float(input("ป้อนค่า PH: "))

# Check and display PH value
check_ph_province(province_name, ph_level)
