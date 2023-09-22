# ข้อ 3

def showProgramName() :
    print('โปรแกรมคำนวณภาษี')

def inputData( ) :
    name = input('ป้อนชื่อสินค้า :')
    price = int(input('ป้อนราคาสินค้า :') )
    return name, price

def checkPrice( name, price ) :
    price = price * 7 / 100
    print(f'ชื่อสินค้า :{name} ภาษีของสินค้าชิ้นนี้ :{price}')

print('-----------------------------')
showProgramName()
print('-----------------------------')
name, price = inputData()
print('-----------------------------')
checkPrice( name, price )
print('-----------------------------')

    

    