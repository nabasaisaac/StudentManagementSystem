from customtkinter import *
from PIL import Image
import os
import sys
from datetime import datetime
from student_registration import Student
from classes_file import Student, Enrollment

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class StudentGUI:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.upper_buttons_frame = CTkFrame(self.display_window, bg_color='#2c2c2c', fg_color='#2c2c2c',
                                            )
        self.upper_buttons_frame.pack(fill=X)

        self.view_students_button = CTkButton(self.upper_buttons_frame, text='View Students', text_color='white',
                                        corner_radius=0, bg_color='#C2C1C8', fg_color='#525252', hover_color='#525252',
                                        font=('roboto', 15), image=CTkImage(Image.open(resource_path('icons/view_customers.png')),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.view_students_button, self.view_students))
        self.view_students_button.pack(side=LEFT)

        self.add_students_button = CTkButton(self.upper_buttons_frame, text='Students', text_color='white',
                                        corner_radius=0, bg_color='#C2C1C8', fg_color='#525252', hover_color='#525252',
                                        font=('roboto', 15), image=CTkImage(Image.open(resource_path('icons/add.png')),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.add_students_button, self.add_students))
        self.add_students_button.pack(side=LEFT, padx=(0, 5))

        self.sliding(self.view_students_button, self.view_students)
        # self.sliding(self.add_students_button, self.add_students)

    def view_students(self):
        self.scrollable_frame = CTkScrollableFrame(self.display_window, fg_color='gray95', bg_color='gray95',
                                                   )
        self.scrollable_frame.pack(fill=BOTH, expand=True)
        if not Student.studentsDatabase:
            CTkLabel(self.scrollable_frame, text="No students registered yet.\nYou'll be able to view students here!",
                     text_color='#2c2c2c', font=('roboto', 15, 'bold')).pack(expand=True, fill=BOTH, pady=(200, 0))
        for key, value in Student.studentsDatabase.items():
            self.info_frame = CTkFrame(self.scrollable_frame, bg_color='gray95', fg_color='#2c2c2c',
                                       corner_radius=15, width=500)
            self.info_frame.pack(side=LEFT, fill=X, padx=20, pady=20, expand=True)

            CTkLabel(self.info_frame, text=f'Student ID:', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30, pady=(20, 0))
            CTkLabel(self.info_frame, text=f'{key}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=30)

            CTkLabel(self.info_frame, text=f'Student Name', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30)
            CTkLabel(self.info_frame, text=f'{value[0].upper()} {value[1].upper()}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=30)

            CTkLabel(self.info_frame, text=f'Gender', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30)
            CTkLabel(self.info_frame, text=f'{value[2]}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=30)

            CTkLabel(self.info_frame, text=f'Contact', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30)
            CTkLabel(self.info_frame, text=f'{value[3]}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=30)

            CTkLabel(self.info_frame, text=f'Email', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30)
            CTkLabel(self.info_frame, text=f'{value[4]}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=30)

            CTkLabel(self.info_frame, text=f'National Identification Number', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30)
            CTkLabel(self.info_frame, text=f'{value[5]}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=30)

            CTkLabel(self.info_frame, text=f'Location', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30)
            CTkLabel(self.info_frame, text=f'{value[6].upper()}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(side=LEFT, fill=X, pady=(0, 20), padx=30)
            self.enrollment_button = CTkButton(self.info_frame, text='Course Enrollment', bg_color='#2c2c2c', fg_color='#2c2c2c',
                                          corner_radius=10, height=35, hover_color='#2c2c2c', compound=LEFT,
                                          border_color='#725cff',
                                          font=('roboto', 15), text_color='#725cff', border_width=1)
            self.enrollment_button.configure(command=lambda student_id=key, name=f'{value[0]} {value[1]}':
            self.course_enrollment(student_id, name))
            self.enrollment_button.pack(side=RIGHT, padx=(0, 20), pady=(0, 20))

    def course_enrollment(self, student_id, name):
        enroll_student = CTkInputDialog(fg_color='#2c2c2c', button_fg_color='#725cff',
                                        text=f'To enroll {name.upper()}\nEnter Course ID Here',
                                        title='Course Enrollment', font=('roboto', 15),
                                        )
        course_id = enroll_student.get_input()
        if not course_id: return

        enroll_date = datetime.now().date()
        enrollment_object = Enrollment(student_id, course_id, enroll_date)
        enrollment_object.enrollStudent()

        from main_window import MainWindow
        MainWindow.__new__(MainWindow).success_information(f'{name} successfully enrolled in the course')

    def add_students(self):
        from student_registration import RegisterStudents
        RegisterStudents(self.display_window)

    def hiding(self):
        self.view_students_button.configure(fg_color='#525252')
        self.add_students_button.configure(fg_color='#525252')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#C2C1C8')

        methods()

