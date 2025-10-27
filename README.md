# Student Manager

A simple, interactive command-line application for managing student information and grades.

## Features

- **Student Management**: Add and remove students from the system
- **Email Validation**: Ensures all student emails are properly formatted using regex
- **Grade Tracking**: Add grades (0-100) and automatically calculate averages
- **Statistics Dashboard**: View comprehensive statistics about all students and grades
- **Data Persistence**: All student data is automatically saved to a text file

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone or download this repository
2. No additional dependencies required - uses Python standard library only

### Running the Application

```bash
python main.py
```

## Usage

When you run the application, you'll see an interactive menu with the following options:

### 1. Add a Student
- Enter the student's name
- Enter a valid email address (format: name@domain.com)
- The system validates the email and checks for duplicates
- Student is saved automatically

### 2. Remove a Student
- View the list of all students
- Enter the number corresponding to the student you want to remove
- Student is permanently removed from the system

### 3. View All Students
- Displays a formatted list of all students
- Shows each student's name, email, grades, and average

### 4. Add Grade to Student
- Select a student from the list
- Enter a grade between 0 and 100
- The grade is added and the new average is calculated automatically

### 5. View Statistics
- Total number of students
- Total grades recorded
- Number of unique grades
- List of all unique grades
- Count of grades above 90
- Overall class average

### 6. Quit
- Exit the application

## Example Session

```
Student Manager
-----------------------
1 - Add a Student
2 - Remove a Student
3 - View All Students
4 - Add Grade to Student
5 - View Statistics
6 - Quit
-----------------------
Choose an option: 1

Enter student name: John Smith
Enter student email: john.smith@example.com

John Smith has been added successfully!
```

## Technical Details

### Student Class

The `Student` class includes:
- **Attributes**: name, email, grades (list)
- **Methods**:
  - `add_grade(grade)`: Add a new grade
  - `average_grade()`: Calculate average of all grades
  - `display_info()`: Display student information
  - `grades_tuple()`: Return grades as an immutable tuple

### Data Storage

- Student data is stored in `students_list.txt`
- Format: `name-:-email-:-grade1,grade2,grade3`
- Data is automatically loaded when the program starts
- Changes are saved immediately after each operation

### Email Validation

Uses regex pattern: `^[\w.+-]+@[\w.-]+\.\w+$`

This validates:
- Username can contain letters, numbers, dots, plus signs, and hyphens
- Must have @ symbol
- Domain name with at least one dot
- Top-level domain

## File Structure

```
.
├── main.py              # Main application file
├── students_list.txt    # Auto-generated data file
├── README.md            # This file
└── .gitignore          # Git ignore file
```

## Features in Detail

### Grade Management
- Grades must be between 0 and 100
- Average is calculated automatically
- Displays as "No grades yet" if student has no grades

### Statistics
- Uses Python sets to track unique grades
- Counts high performers (grades > 90)
- Calculates overall class average

### Error Handling
- Invalid email format detection
- Duplicate email prevention
- Input validation for numeric entries
- Bounds checking for grade values

## Future Enhancements

Possible features to add:
- Edit student information
- Search for students by name or email
- Export data to CSV
- Grade history with timestamps
- Letter grade conversion (A, B, C, etc.)
- Sort students by average grade

## License

This project is free to use for educational purposes.

## Author

Created as a Python learning project demonstrating:
- Object-oriented programming
- File I/O operations
- Regular expressions
- Data validation
- Interactive CLI applications
# Object-Oriented-Python-Practice
