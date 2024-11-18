from management import student_management_system

def main():
    system = student_management_system()
    while True:
        print('student_management_system')
        print('1. Add Student')
        print('2. Student Information')
        print('3. View All Students')
        print('5. Exit')
        
        
        choice = input('Enter Your Choice')
        
        if choice == '1':
            student_id = input('Enter Student ID: ')
            student_name = input('Enter Student Name: ')
            department = input('Department: ')
            system.add_students(student_id, student_name, department)
            
            
        elif choice =='2':
            student_id = input('Enter Your ID: ')
            student_name = input('Enter Your Name')
            department = input('Enter Department')
            
            
        elif choice =='3':
            system.view_all_students
            
            
            
        elif choice == '4':
            break
        else:
            print("Exiting the system. Thank you!")


if __name__ == "__main__":
    
    main()

            
            