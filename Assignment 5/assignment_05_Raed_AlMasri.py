import json


class Course:

    def __init__(self,code,name,credit_hours,is_core=True):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.is_core = is_core

    def __str__(self):
        course_type = "Core" if self.is_core else "Elective"
        return f"[{course_type}] {self.code} - {self.name} ({self.credit_hours} credit hours)"

# ----------------------------------------------------------------------------------------------

class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll(self, course):
        if course.code in self.courses:
            raise ValueError(f"Already enrolled in course {course.code}.")
        self.courses[course.code] = course

    def drop(self, course_code):
        if course_code not in self.courses:
            raise KeyError(f"Course {course_code} not found in enrolled courses.")
        del self.courses[course_code]

    def list_courses(self):
        if not self.courses:
            return f"{self.name} is not enrolled in any courses."
        return "\n".join(str(course) for course in self.courses.values())
    
# -----------------------------------------------------------------------------------------------

class CourseCatalog:
    
    def __init__(self):
        self.courses = {}  # Dictionary to store courses by course code

    def add_course(self, course):
        self.courses[course.code] = course

    def get_course(self, code):
        if code not in self.courses:
            raise KeyError(f"Course with code {code} not found.")
        return self.courses[code]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            data = {
                code: {
                    'name': course.name,
                    'credit_hours': course.credit_hours,
                    'is_core': course.is_core
                }
                for code, course in self.courses.items()
            }
            json.dump(data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.courses = {
                code: Course(code, details['name'], details['credit_hours'], details['is_core'])
                for code, details in data.items()
            }

# -------------------------------------------------------------------------------------------------------------------

class EnrollmentSystem:
    
    def __init__(self):
        self.catalog = CourseCatalog()
        self.students = []

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        self.students.append(Student(student_id, name))
        print(f"Student {name} added.")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        raise ValueError(f"Student with ID {student_id} not found.")

    def add_course(self):
        code = input("Enter course code: ")
        name = input("Enter course name: ")
        credit_hours = int(input("Enter credit hours: "))
        is_core = input("Is this a core course? (y/n): ").lower() == 'y'
        course = Course(code, name, credit_hours, is_core)
        self.catalog.add_course(course)
        print(f"Course {name} added to the catalog.")

    def enroll_student_in_course(self):
        student_id = input("Enter student ID: ")
        try:
            student = self.find_student(student_id)
            course_code = input("Enter course code: ")
            course = self.catalog.get_course(course_code)
            student.enroll(course)
            print(f"Enrolled {student.name} in {course.name}.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

    def drop_course_for_student(self):
        student_id = input("Enter student ID: ")
        try:
            student = self.find_student(student_id)
            course_code = input("Enter course code to drop: ")
            student.drop(course_code)
            print(f"Dropped course {course_code} for {student.name}.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

    def list_student_courses(self):
        student_id = input("Enter student ID: ")
        try:
            student = self.find_student(student_id)
            print(student.list_courses())
        except ValueError as e:
            print(f"Error: {e}")

    def save_course_catalog(self):
        filename = input("Enter filename to save catalog: ")
        self.catalog.save_to_file(filename)
        print("Course catalog saved.")

    def load_course_catalog(self):
        filename = input("Enter filename to load catalog: ")
        try:
            self.catalog.load_from_file(filename)
            print("Course catalog loaded.")
        except FileNotFoundError:
            print("File not found.")

    def run(self):
        while True:
            print("\n--- Course Enrollment System ---")
            print("1. Add Course")
            print("2. Enroll Student in Course")
            print("3. Drop Course for Student")
            print("4. List Student Courses")
            print("5. Save Course Catalog")
            print("6. Load Course Catalog")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_course()
            elif choice == '2':
                self.enroll_student_in_course()
            elif choice == '3':
                self.drop_course_for_student()
            elif choice == '4':
                self.list_student_courses()
            elif choice == '5':
                self.save_course_catalog()
            elif choice == '6':
                self.load_course_catalog()
            elif choice == '7':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

system = EnrollmentSystem()
system.run()