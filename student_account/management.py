from students_account import students


class student_management_system:
    def __init__(self):
        self.students = {}
        
    def add_students(self, student_id, student_name, department):
        if student_id not in self.students:
            student = students(student_id, student_name, department)
            self.students[student_id] = student
            print(f'Added Student: {student_id}, Name: {student_name}, Department: {department}')
        else: 
            print('Not Found')
    def get_account(self, student_id):
        return self.students.get(student_id)
        
        
        
    def view_all_students(self):
        if not self.students:
            print('Not Found')
            
        else:
            for student in self.students.values():
                
                 print(f'student_id: {Student.student_id}, Name: {Student.student_name}, Department: {Student.department}')
            