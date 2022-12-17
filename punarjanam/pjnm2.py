class Student:
    def __init__(self, marks):
        self.marks = marks
    
    @classmethod
    def average_marks(cls, students):
        total_marks = sum(student.marks for student in students)
        num_students = len(students)
        average_marks = total_marks / num_students
        return average_marks

# create a list of Student instances
students = [Student(80), Student(75), Student(90), Student(60), Student(85)]

# calculate the average marks
average_marks = Student.average_marks(students)

# print the average marks
print(average_marks)