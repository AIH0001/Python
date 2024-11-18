class students:
    def __init__(self, student_id, student_name, department):
        self.student_id = student_id
        self.student_name = student_name
        self.department = department
        
    def info(self):
        print(f'ID: {self.student_id}')
        print(f'Name: {self.student_name}')
        print(f'Department: {self.department}')
        
        