# จงเขียนโปรแกรมPython คำนวณหาราคาขายสินค้า โดยรับชื่อสินค้า และราคาสินค้า(ต้นทุน) ทางแป้นพิมพ์ 
# แล้วคำนวณหาราคาขายของสินค้า โดยราคาขายสินค้าจะคิดเพิ่มจากราคาสินค้า (ต้นทุน) ร้อยละ 10 สูตร ราคาขายสินค้า  =  ราคาสินค้า(ต้นทุน)  + (ราคาสินค้า(ต้นทุน) * 10 / 100)

def showProgramName() :
    print('----โปรแกรมคำนวณราคาสินค้าโดยคิดจากต้นทุน----')

def inputData( ) :
    name = input('ป้อนชื่อสินค้า : ')
    price = int( input('ป้อนราคาสินค้า : ') )
    return name, price, 

def checkPrice( name, price ) :
    price = price + price * 10 / 100
    print(f'ชื่อสินค้า{name} ราคา {price}')

print('-------------------------------')
showProgramName()
print('-------------------------------')
name, price = inputData()
print('-------------------------------')
checkPrice( name, price)
print('-------------------------------')