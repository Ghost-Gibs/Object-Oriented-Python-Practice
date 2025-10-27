import re
import os

# File to store student data
STUDENTS_FILE = 'students_list.txt'

# Part 1: Class Definition
class Student:
    """
    A class to represent a student with their name, email, and grades.
    """
    def __init__(self, name, email, grades=None):
        """
        Initialize a new student.
        
        Args:
            name (str): The student's name
            email (str): The student's email address
            grades (list): Optional list of initial grades
        """
        self.name = name
        self.email = email
        # If no grades provided, start with empty list
        self.grades = grades if grades is not None else []
    
    def add_grade(self, grade):
        """
        Add a new grade to the student's grades list.
        
        Args:
            grade (int): The grade to add
        """
        self.grades.append(grade)
    
    def average_grade(self):
        """
        Calculate and return the average of all grades.
        
        Returns:
            float: The average grade, or 0 if no grades exist
        """
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        """
        Print the student's information including name, email, and grades.
        """
        print(f"\nStudent: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        if self.grades:
            print(f"Average Grade: {self.average_grade():.2f}")
        else:
            print("Average Grade: No grades yet")
    
    def grades_tuple(self):
        """
        Return the grades as a tuple (immutable version).
        
        Returns:
            tuple: A tuple of all grades
        """
        return tuple(self.grades)


# Function to write students to a text file
def write_students(students_list):
    """
    Save all student data to a text file.
    
    Args:
        students_list (list): List of Student objects to save
    """
    with open(STUDENTS_FILE, 'w') as file:
        for student in students_list:
            # Convert grades list to comma-separated string
            grades_str = ','.join(map(str, student.grades)) if student.grades else ''
            file.write(f"{student.name}-:-{student.email}-:-{grades_str}\n")


# Function to read students from a text file
def read_students():
    """
    Load student data from a text file.
    
    Returns:
        list: List of Student objects loaded from file
    """
    students_list = []
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, 'r') as file:
            for line in file:
                # Parse the line using regex
                data = re.search(r"([\w\s]+)-:-([\w@.]+)-:-(.*)", line)
                if data:
                    name = data.group(1).strip()
                    email = data.group(2).strip()
                    grades_str = data.group(3).strip()
                    # Convert comma-separated grades back to list of integers
                    grades = []
                    if grades_str:
                        grades = [int(g) for g in grades_str.split(',') if g]
                    students_list.append(Student(name, email, grades))
    return students_list


# Function to validate email format
def validate_email(email):
    """
    Validate email format using regex (name@domain.com).
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^[\w.+-]+@[\w.-]+\.\w+$'
    return re.match(pattern, email) is not None


# Function to add a new student
def add_student(students_list):
    """
    Add a new student to the list.
    
    Args:
        students_list (list): Current list of students
    """
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    
    # Validate email
    if not validate_email(email):
        print("\nInvalid email format! Please use format: name@domain.com")
        return
    
    # Check if email already exists
    for student in students_list:
        if student.email == email:
            print(f"\nA student with email {email} already exists!")
            return
    
    # Create new student
    new_student = Student(name, email)
    students_list.append(new_student)
    write_students(students_list)
    print(f"\n{name} has been added successfully!")


# Function to remove a student
def remove_student(students_list):
    """
    Remove a student from the list.
    
    Args:
        students_list (list): Current list of students
    """
    if not students_list:
        print("\nNo students to remove.")
        return
    
    view_students(students_list)
    try:
        choice = int(input("\nEnter the number of the student to remove: "))
        if 1 <= choice <= len(students_list):
            removed_student = students_list.pop(choice - 1)
            write_students(students_list)
            print(f"\n{removed_student.name} has been removed successfully!")
        else:
            print("\nInvalid choice.")
    except ValueError:
        print("\nPlease enter a valid number.")


# Function to view all students
def view_students(students_list):
    """
    Display all students with their information.
    
    Args:
        students_list (list): Current list of students
    """
    if not students_list:
        print("\nNo students in the system.")
        return
    
    print("\n" + "="*60)
    print("STUDENT LIST")
    print("="*60)
    for i, student in enumerate(students_list, 1):
        print(f"\n{i}. {student.name}")
        print(f"   Email: {student.email}")
        print(f"   Grades: {student.grades}")
        if student.grades:
            print(f"   Average: {student.average_grade():.2f}")
        else:
            print(f"   Average: No grades yet")
    print("="*60)


# Function to add a grade to a student
def add_grade_to_student(students_list):
    """
    Add a grade to an existing student.
    
    Args:
        students_list (list): Current list of students
    """
    if not students_list:
        print("\nNo students in the system.")
        return
    
    view_students(students_list)
    try:
        choice = int(input("\nEnter the number of the student: "))
        if 1 <= choice <= len(students_list):
            student = students_list[choice - 1]
            grade = int(input(f"Enter grade for {student.name} (0-100): "))
            if 0 <= grade <= 100:
                student.add_grade(grade)
                write_students(students_list)
                print(f"\nGrade {grade} added to {student.name}!")
                print(f"New average: {student.average_grade():.2f}")
            else:
                print("\nGrade must be between 0 and 100.")
        else:
            print("\nInvalid choice.")
    except ValueError:
        print("\nPlease enter a valid number.")


# Function to view statistics
def view_statistics(students_list):
    """
    Display statistics about all students.
    
    Args:
        students_list (list): Current list of students
    """
    if not students_list:
        print("\nNo students in the system.")
        return
    
    # Collect all grades
    all_grades = []
    for student in students_list:
        all_grades.extend(student.grades)
    
    if not all_grades:
        print("\nNo grades recorded yet.")
        return
    
    # Create set of unique grades
    unique_grades = set(all_grades)
    
    # Count grades above 90
    grades_above_90 = sum(1 for grade in all_grades if grade > 90)
    
    print("\n" + "="*60)
    print("STATISTICS")
    print("="*60)
    print(f"Total students: {len(students_list)}")
    print(f"Total grades recorded: {len(all_grades)}")
    print(f"Unique grades: {len(unique_grades)}")
    print(f"All unique grades: {sorted(unique_grades)}")
    print(f"Grades above 90: {grades_above_90}")
    if all_grades:
        print(f"Overall average: {sum(all_grades)/len(all_grades):.2f}")
    print("="*60)


# Main interactive menu
def main():
    """
    Main function to run the interactive student manager.
    """
    # Create file if it doesn't exist
    if not os.path.exists(STUDENTS_FILE):
        open(STUDENTS_FILE, 'w').close()
    
    while True:
        students_list = read_students()
        action = input('''
Student Manager
-----------------------
1 - Add a Student
2 - Remove a Student
3 - View All Students
4 - Add Grade to Student
5 - View Statistics
6 - Quit
-----------------------
Choose an option: ''')
        
        if action == '1':
            add_student(students_list)
        elif action == '2':
            remove_student(students_list)
        elif action == '3':
            view_students(students_list)
        elif action == '4':
            add_grade_to_student(students_list)
        elif action == '5':
            view_statistics(students_list)
        elif action == '6':
            print("\nThank you for using Student Manager!")
            break
        else:
            print("\nInvalid option. Please choose 1-6.")


# Run the program
if __name__ == "__main__":
    main()
