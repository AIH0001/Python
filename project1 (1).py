

while True:
    print('student_management_system')
    print('1. Add Student')
    print('2. Student Information')
    print('3. View All Students')
    print('4. Exit')

    choice = input('Enter Your Choice : ')
    if choice == '1':
        student_id = input('Enter Student ID : ')
        student_name = input('Enter Student Name : ')
        department = input('Department : ')
        f = open("info.txt", "a")

        f.write('\n'+student_id+' '+ student_name+' '+ department+'\n')
        f.close()
        print(f'Added Student: {student_id}, Name: {student_name}, Department: {department}')

    elif choice == '2':
        student_id = input('Enter Student ID : ')
        f = open("info.txt", "r")
        ids = []
        names = []
        departments = []
        for x in f.readlines():
            y  = x.split()
            ids.append(y[0])
            names.append(y[1])
            departments.append(y[2])
        if student_id in ids:
            idx = ids.index(student_id)
            print(f'Student Id: {ids[idx]}, Name: {names[idx]}, Department: {departments[idx]}')
        else:
            print('Not Found')
        f.close()

        # print(f'Added Student: {student_id}, Name: {student_name}, Department: {department}')

    elif choice =='3':
        f = open("info.txt", "r")
        print(f.read())
        f.close()
    elif choice =='4':
        break
