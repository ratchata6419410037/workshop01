# ข้อ 2

def showProgramName() :
    print('โปรแกรมหาค่าเฉลี่ยของนักเรียน')

def inputData( ) :
    no = int( input('ป้อนรหัสนร : ') )
    name = input('ป้อนชื่อนร :')
    scoreone = int( input('คะแนนครั้งที่หนึ่ง : ') )
    scoretwo = int( input('คะแนนครั้งที่สอง : ') )
    scorethree = int( input('คะแนนครั้งที่สาม : ') )
    return no, name, scoreone, scoretwo, scorethree

def checkScore( no, name, scoreone, scoretwo, scorethree ) :
    score = (scoreone + scoretwo + scorethree) / 3
    print(f'รหัส {no} ชื่อ{name} ได้คะแนนรวมทั้งสามครั้ง {score:.2f} ')

print('-------------------------------')
showProgramName()
print('-------------------------------')
no, name, scoreone, scoretwo, scorethree = inputData() 
print('-------------------------------')
checkScore( no, name, scoreone, scoretwo, scorethree )
print('-------------------------------')
    
    

