from ResultCalculation import Student

def main():
    print('\nHello sir! Welcome our Result calculator apps 👍\n')
    n = int(input('Enter student number: '))
   
    for i in range(n):
        roll = int(input(f'\nEnter {i+1}th student id: '))
        name = input(f'Enter {i+1}th student name: ')
        student1 = Student(roll, name)
        sub = int(input('\nEnter number of subject: '))
        for j in range(sub):
            sub_title = input('\nEnter subject title : ')
            sub_id = input('Enter subject id : ')
            mark = int(input('Enter subject Mark : '))
            student1.calculate_result(sub_title, sub_id, mark)
        
        student1.final_gpa(sub)
        student1.add_all_Student()
    
    print()
    
    count = 1
    for i in Student.all_student_marks:
        print(f"\nStudent numbert {count}th details result________\n")
        print(Student.all_student_marks[i])
        count += 1
            
    

if __name__ == '__main__':
    main()