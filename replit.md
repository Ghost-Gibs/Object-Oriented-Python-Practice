# Student Manager

## Overview
A command-line student management system built in Python. This application allows you to manage student information, track grades, and view statistics.

## Features
- Add and remove students
- Email validation with regex
- Add grades to students (0-100 scale)
- Calculate average grades per student
- View statistics across all students
- Persistent data storage in text file

## Project Structure
- `main.py` - Main application with Student class and all functionality
- `students_list.txt` - Auto-generated file to store student data

## How to Use
Run the program and use the interactive menu:
1. Add a Student - Register new students with name and email
2. Remove a Student - Delete a student from the system
3. View All Students - See all registered students and their grades
4. Add Grade to Student - Add a grade (0-100) to any student
5. View Statistics - See overall statistics including total students, grades, and averages
6. Quit - Exit the program

## Technical Details
- Uses regex for email validation and data parsing
- Student data persists to `students_list.txt`
- Implements OOP with Student class
- Data format: `name-:-email-:-grade1,grade2,grade3`

## Recent Changes
- October 27, 2025: Initial project setup
