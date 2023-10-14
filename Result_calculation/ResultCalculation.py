class Student:
    all_student_marks = {}
    def __init__(self, student_id, student_name) -> None:
        self.student_id = student_id
        self.student_name = student_name
        self.student_total_Result = {}
        self.total_gpa = 0
        self.student_total_Result['student_id'] = self.student_id
        self.student_total_Result['Name'] = self.student_name 

    
    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00, 
            'A': 4.00, 
            'A-': 3.50, 
            'B': 3.00, 
            'C': 2.00, 
            'D': 1.00, 
            'F': 0.00
            }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'
        elif 3.5 <= value < 4.5:
            return 'A'
        elif 3.0 <= value < 3.5:
            return 'A-'
        elif 2.5 <= value < 3.0:
            return 'B'
        elif 2.0 <= value < 2.5:
            return 'C'
        elif 1.0 <= value < 2.0:
            return 'D'
        else:
            return 'F'

    
    def calculate_result(self, subject_title, subject_id, mark):
        self.marks = {}
        self.marks['Subject_id'] = subject_id
        self.marks['mark'] = mark
        self.marks['Grade'] = self.calculate_grade(mark)
        self.marks['GPA'] = self.grade_to_value(self.marks['Grade'])
        self.student_total_Result[subject_title] = self.marks
        self.total_gpa += self.marks['GPA']
    
    
        
    
    def final_gpa(self, number):
        ans = self.total_gpa / number
        self.student_total_Result['Final_GPA'] = ans
        self.student_total_Result['Final_grade'] = self.value_to_grade(ans)

        
    def add_all_Student(self):
        Student.all_student_marks[self.student_id] = self.student_total_Result
    