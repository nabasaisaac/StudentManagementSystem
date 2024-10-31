class Person:
    def __init__(self, sur_name, first_name, gender, contact, email, nin, location):
        self.surname = sur_name
        self.first_name = first_name
        self.gender = gender
        self.contact = contact
        self.email = email
        self.nin = nin
        self.location = location


class Student(Person):
    studentsDatabase = {}

    def __init__(self, surname, first_name, gender, contact, email, nin, location, student_id):
        super().__init__(surname, first_name, gender, contact, email, nin, location)
        self.__student_id = student_id

    def register_student(self):
        try:
            self.studentsDatabase[self.__student_id] = [
                self.surname, self.first_name, self.gender, self.contact, self.email, self.nin, self.location,
            ]
        except KeyError:
            return False

    def display_student_info(self):
        return self.studentsDatabase


class Teacher(Person):
    teachersDatabase = {}

    def __init__(self, surname, first_name, gender, contact, email, nin, location, teacher_id, course_taught):
        super().__init__(surname, first_name, gender, contact, email, nin, location)
        self.__teacher_id = teacher_id
        self.course_taught = course_taught

    def register_teacher(self):
        try:
            self.teachersDatabase[self.__teacher_id] = [
                self.surname, self.first_name, self.gender, self.contact, self.email, self.nin, self.location, self.__teacher_id,
                self.course_taught
            ]
        except KeyError:
            return False

    def display_teacher_info(self):
        return self.teachersDatabase


class Course:
    coursesDatabase = {}

    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.course_name = course_name

    def registerCourse(self):
        try:
            self.coursesDatabase[self.__course_id] = self.course_name
            return f'Student successfully enrolled'
        except KeyError:
            return False

    def displayCourses(self):
        return self.coursesDatabase


class Enrollment:
    enrollmentsDatabase = {}

    def __init__(self, student_id, course_id, enrollment_date):
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def enrollStudent(self):
        if self.student_id not in Student.studentsDatabase:
            return False
        elif self.course_id not in Course.coursesDatabase:
            return False
        else:
            self.enrollmentsDatabase[self.student_id] = [self.course_id, self.enrollment_date]


class Grade:
    gradesDatabase = {}

    def __init__(self, grade):
        self.__grade = grade

    def assignGrade(self, student_id):
        self.gradesDatabase[student_id] = self.__grade

    def getGrades(self):
        return self.gradesDatabase


# print(Student.studentsDatabase)
#
# student1 = Student('NABASA', 'ISAAC', 'M', 'SMSD', 'KATOVU', 'BSCS')
# student2 = Student('NABASA', 'ISAAC', 'M', 'SMSD', 'KATOVU', 'BeCS')
#
# student1.register_student()
# student2.register_student()
# # print(student1.display_student_info())











