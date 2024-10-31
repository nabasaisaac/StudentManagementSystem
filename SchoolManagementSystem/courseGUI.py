from customtkinter import *
from PIL import Image
import os
import sys
from classes_file import Course, Teacher


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class CourseGUI:
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

        CTkLabel(self.side_frame, text=f'COURSE REGISTRATION', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                 font=('roboto', 16, 'bold'), width=400, justify=CENTER).pack(fill=X, pady=(15, 20))

        CTkLabel(self.side_frame, text='Course ID', text_color='white', font=('roboto', 15), justify=LEFT,
                 anchor='w').pack(fill=X, padx=20)
        self.course_id_entry = CTkEntry(self.side_frame, border_color='#C2C1C8',
                                         border_width=1, height=35, text_color='white')
        self.course_id_entry.pack(fill=X, pady=(0, 10), padx=20)
        self.course_id_entry.bind('<FocusIn>', lambda event: self.course_id_entry.configure(border_color='#7E6AFE'))
        self.course_id_entry.bind('<FocusOut>', lambda event: self.course_id_entry.configure(border_color='#C2C1C8'))

        CTkLabel(self.side_frame, text='Course Name', text_color='white', font=('roboto', 15), justify=LEFT,
                 anchor='w').pack(fill=X, padx=20)
        self.course_name_entry = CTkEntry(self.side_frame,  border_color='#C2C1C8', border_width=1, height=35,
                                          text_color='white')
        self.course_name_entry.pack(fill=X, pady=(0, 10), padx=20)
        self.course_name_entry.bind('<FocusIn>', lambda event: self.course_name_entry.configure(border_color='#7E6AFE'))
        self.course_name_entry.bind('<FocusOut>', lambda event: self.course_name_entry.configure(border_color='#C2C1C8'))

        self.register_button = CTkButton(self.side_frame, text='Register Course', bg_color='#2c2c2c', fg_color='#2c2c2c',
                                           corner_radius=10, height=35, hover_color='#2c2c2c', border_color='#725cff',
                                           font=('roboto', 15), text_color='#725cff', border_width=1,
                                            command=lambda: self.register_courses())

        self.register_button.pack(padx=20, pady=20, fill=X)

        self.display_courses()

    def register_courses(self):

        course_object = Course(self.course_id_entry.get(), self.course_name_entry.get())
        course_object.registerCourse()
        self.display_courses()

        from main_window import MainWindow
        MainWindow.__new__(MainWindow).success_information(f'Teacher successfully registered.')
        self.course_id_entry.delete(0, END)
        self.course_name_entry.delete(0, END)


    def display_courses(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        CTkLabel(self.scrollable_frame, text=f'REGISTERED COURSES', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                 font=('roboto', 16, 'bold'), width=400, justify=CENTER).pack(fill=X, pady=(15, 0))

        if not Course.coursesDatabase:
            CTkLabel(self.scrollable_frame, text="No courses registered yet.\nYou'll be able to view courses here!",
                     text_color='white', font=('roboto', 15, 'bold')).pack(expand=True, fill=BOTH, pady=(200, 0))
            return

        for key, value in Course.coursesDatabase.items():
            self.info_frame = CTkFrame(self.scrollable_frame, bg_color='#2c2c2c', fg_color='#2c2c2c',
                                       corner_radius=15, width=500)
            self.info_frame.pack(fill=X, padx=20, pady=10, expand=True)

            CTkLabel(self.info_frame, text=f"Course ID", text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20, pady=(20, 0))
            CTkLabel(self.info_frame, text=f'{key}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=20)

            CTkLabel(self.info_frame, text=f"Course Name", text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20)
            CTkLabel(self.info_frame, text=f'{value.upper()}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=20)

            CTkLabel(self.info_frame, text=f"Assigned Teacher", text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20)
            try:
                teacher = [ids for ids in Teacher.teachersDatabase.keys() if Teacher.teachersDatabase[ids][-1] == key][0]
                teacher_info = Teacher.teachersDatabase[teacher]
                teacher_name = f'{teacher_info[0].upper()} {teacher_info[1].upper()}'
            except (KeyError, IndexError):
                teacher_name = 'No Teacher Assigned yet'

            CTkLabel(self.info_frame, text=f'{teacher_name}', text_color='white',
                     fg_color='#2c2c2c', bg_color='#2c2c2c', font=('roboto', 15, 'bold'), justify=LEFT,
                     anchor='w').pack(fill=X, pady=(0, 10), padx=20)
            CTkLabel(self.info_frame, text=f'---------------------------------------------------------------------------'
                                           f'----------------------------------------', text_color='white',
                     fg_color='#2c2c2c', bg_color='#2c2c2c', font=('roboto', 15, 'bold'), justify=LEFT,
                     anchor='w').pack(fill=X, padx=20)
