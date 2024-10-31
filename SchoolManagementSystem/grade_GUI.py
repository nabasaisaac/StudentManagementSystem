from customtkinter import *
from PIL import Image
import os
import sys
from classes_file import *


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class GradeGUI:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.side_frame = CTkFrame(self.display_window, bg_color='gray40', fg_color='#2c2c2c',
                                   corner_radius=15, )
        self.side_frame.pack(side=LEFT, fill=Y, padx=20, pady=(20, 0))
        self.basic_infor_frame = CTkFrame(self.display_window, bg_color='gray40', fg_color='#2c2c2c',
                                          corner_radius=15, )
        self.basic_infor_frame.pack(side=LEFT, pady=(20, 0), padx=(0, 20), fill=BOTH, expand=True)

        self.scrollable_frame = CTkScrollableFrame(self.basic_infor_frame, fg_color='#2c2c2c', bg_color='#2c2c2c',
                                                   )
        self.scrollable_frame.pack(fill=BOTH, expand=True, pady=10)

        CTkLabel(self.side_frame, text=f'Grade Management', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                 font=('roboto', 16, 'bold'), width=400, justify=CENTER).pack(fill=X, pady=(15, 20))

        CTkLabel(self.side_frame, text='Student ID', text_color='white', font=('roboto', 15), justify=LEFT,
                 anchor='w').pack(fill=X, padx=20)
        self.student_id_entry = CTkEntry(self.side_frame, border_color='#C2C1C8',
                                         border_width=1, height=35, text_color='white')
        self.student_id_entry.pack(fill=X, pady=(0, 10), padx=20)
        self.student_id_entry.bind('<FocusIn>', lambda event: self.student_id_entry.configure(border_color='#7E6AFE'))
        self.student_id_entry.bind('<FocusOut>', lambda event: self.student_id_entry.configure(border_color='#C2C1C8'))

        CTkLabel(self.side_frame, text='Grade', text_color='white', font=('roboto', 15), justify=LEFT,
                 anchor='w').pack(fill=X, padx=20)
        self.grade_name_entry = CTkEntry(self.side_frame,  border_color='#C2C1C8', border_width=1, height=35,
                                          text_color='white')
        self.grade_name_entry.pack(fill=X, pady=(0, 10), padx=20)
        self.grade_name_entry.bind('<FocusIn>', lambda event: self.grade_name_entry.configure(border_color='#7E6AFE'))
        self.grade_name_entry.bind('<FocusOut>', lambda event: self.grade_name_entry.configure(border_color='#C2C1C8'))

        self.register_button = CTkButton(self.side_frame, text='Register grade', bg_color='#2c2c2c', fg_color='#2c2c2c',
                                           corner_radius=10, height=35, hover_color='#2c2c2c', border_color='#725cff',
                                           font=('roboto', 15), text_color='#725cff', border_width=1,
                                            command=lambda: self.register_grades())

        self.register_button.pack(padx=20, pady=20, fill=X)

        self.display_grades()

    def register_grades(self):
        from main_window import MainWindow
        if self.student_id_entry.get() not in Student.studentsDatabase.keys():
            MainWindow.__new__(MainWindow).unsuccessful_information(f'No Student with this ID')
            return
        if self.student_id_entry.get() not in Enrollment.enrollmentsDatabase.keys():
            MainWindow.__new__(MainWindow).unsuccessful_information(f'First Enroll this Student in the Course')
            return
        grade_object = Grade(self.grade_name_entry.get())
        grade_object.assignGrade(self.student_id_entry.get(), )
        self.display_grades()

        MainWindow.__new__(MainWindow).success_information(f'Student Successfully Graded')
        self.student_id_entry.delete(0, END)
        self.grade_name_entry.delete(0, END)

    def display_grades(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        CTkLabel(self.scrollable_frame, text=f'REGISTERED GRADES', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                 font=('roboto', 16, 'bold'), width=400, justify=CENTER).pack(fill=X, pady=(15, 0))

        if not Grade.gradesDatabase:
            CTkLabel(self.scrollable_frame, text="No grades registered yet.\nYou'll be able to view students grades here!",
                     text_color='white', font=('roboto', 15, 'bold')).pack(expand=True, fill=BOTH, pady=(200, 0))
            return

        for key, grade in Grade.gradesDatabase.items():
            self.info_frame = CTkFrame(self.scrollable_frame, bg_color='#2c2c2c', fg_color='#2c2c2c',
                                       corner_radius=15, width=500)
            self.info_frame.pack(fill=X, padx=20, pady=10, expand=True)

            CTkLabel(self.info_frame, text=f"Student Name", text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20, pady=(20, 0))

            student_name = f'{Student.studentsDatabase[key][0]} {Student.studentsDatabase[key][1]}'

            CTkLabel(self.info_frame, text=f'{student_name.upper()}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=20)

            CTkLabel(self.info_frame, text=f"Enrolled Course", text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20)

            course = Course.coursesDatabase[Enrollment.enrollmentsDatabase[key][0]]
            CTkLabel(self.info_frame, text=f'{course.upper()}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=20)

            CTkLabel(self.info_frame, text=f"Enrolled On", text_color='white', fg_color='#2c2c2c',
                     bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20)

            enroll_date = Enrollment.enrollmentsDatabase[key][1]
            CTkLabel(self.info_frame, text=f'{enroll_date}', text_color='white', fg_color='#2c2c2c',
                     bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=20)

            CTkLabel(self.info_frame, text=f"Grade", text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20)
            CTkLabel(self.info_frame, text=f'{grade}', text_color='white',
                     fg_color='#2c2c2c', bg_color='#2c2c2c', font=('roboto', 15, 'bold'), justify=LEFT,
                     anchor='w').pack(fill=X, pady=(0, 10), padx=20)
            CTkLabel(self.info_frame, text=f'---------------------------------------------------------------------------'
                                           f'----------------------------------------', text_color='white',
                     fg_color='#2c2c2c', bg_color='#2c2c2c', font=('roboto', 15, 'bold'), justify=LEFT,
                     anchor='w').pack(fill=X, padx=20)
