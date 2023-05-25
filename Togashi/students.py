class Student:
    '''生徒を表す'''
    def __init__(self, id, name, score = 0):
        '''初期化'''
        self.id = id
        self.name = name
        self.score = score

    def getId(self):
        '''Id取得'''
        return self.id
    
    def getName(self):
        '''生徒名取得'''
        return self.name
    
    def setScore(self, score):
        '''点数を取得'''
        self.score = score

    def getScore(self):
        '''点数を設定'''
        return self.score
    
class CalcScore:
    '''点数計算'''
    def __init__(self):
        '''初期化'''
        self.students = []

    def addStudent(self, student):
        '''学生追加'''
        self.students.append(student)

    def ave(self):
        v = 0
        for i in self.students:
            v += i.getScore()
        ave_v = v / len(self.students)
        return ave_v
    
p1 = Student(10, "佐藤")
p1.setScore(80)
p2 = Student(11, "鈴木", score = 79)
p3 = Student(12, "佐々木", score = 84)
p4 = Student(13, "井上", score = 77)

calc = CalcScore()
calc.addStudent(p1)
calc.addStudent(p2)
calc.addStudent(p3)
calc.addStudent(p4)
print("平均点=", calc.ave())