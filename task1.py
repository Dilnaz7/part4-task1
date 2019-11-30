class Student:
    def __init__(self, name, lastname, year_of_entrance, department):

        self.name = name
        self.lastname = lastname
        self.year_of_entrance = year_of_entrance
        self.department = department

    def get_student_info (self):
        return 'Студент:' + self.name + " " + self.lastname + " " + 'поступил(а) в ' +  self.year_of_entrance + " " + 'на факультет ' + self.department

student = Student('Dilnaz', 'Cholponbaeva', '2020', 'Business administration')
print(student.get_student_info())
