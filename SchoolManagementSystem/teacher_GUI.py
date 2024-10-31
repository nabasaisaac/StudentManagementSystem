from customtkinter import *
from PIL import Image
import os
import sys
from teacher_registration import Teacher
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
from classes_file import Teacher

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class TeacherGUI:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        self.upper_buttons_frame = CTkFrame(self.display_window, bg_color='#2c2c2c', fg_color='#2c2c2c',
                                            )
        self.upper_buttons_frame.pack(fill=X)

        self.view_teachers_button = CTkButton(self.upper_buttons_frame, text='View Teachers', text_color='white',
                                        corner_radius=0, bg_color='#C2C1C8', fg_color='#525252', hover_color='#525252',
                                        font=('roboto', 15), image=CTkImage(Image.open(resource_path('icons/view_customers.png')),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.view_teachers_button, self.view_teachers))
        self.view_teachers_button.pack(side=LEFT)

        self.add_teachers_button = CTkButton(self.upper_buttons_frame, text='Teachers', text_color='white',
                                        corner_radius=0, bg_color='#C2C1C8', fg_color='#525252', hover_color='#525252',
                                        font=('roboto', 15), image=CTkImage(Image.open(resource_path('icons/add.png')),
                                        size=(20, 20)), compound=LEFT,  height=35, width=150, command=lambda:
                                        self.sliding(self.add_teachers_button, self.add_teachers))
        self.add_teachers_button.pack(side=LEFT, padx=(0, 5))

        self.sliding(self.view_teachers_button, self.view_teachers)
        # self.sliding(self.add_teachers_button, self.add_teachers)

    def view_teachers(self):
        self.scrollable_frame = CTkScrollableFrame(self.display_window, fg_color='gray95', bg_color='gray95',
                                                   )
        self.scrollable_frame.pack(fill=BOTH, expand=True)
        if not Teacher.teachersDatabase:
            CTkLabel(self.scrollable_frame, text="No teachers registered yet.\nYou'll be able to view teachers here!",
                     text_color='#2c2c2c', font=('roboto', 15, 'bold')).pack(expand=True, fill=BOTH, pady=(200, 0))
            return
        CTkLabel(self.scrollable_frame, text=f"TEACHERS PANEL, TOTAL: {len(Teacher.teachersDatabase)}",
                 text_color='#725cff', fg_color='gray95', bg_color='gray95',
                 font=('roboto', 15, 'bold'), justify=CENTER).pack(fill=X, padx=30, pady=(10, 0))
        for key, value in Teacher.teachersDatabase.items():
            self.info_frame = CTkFrame(self.scrollable_frame, bg_color='gray95', fg_color='#2c2c2c',
                                       corner_radius=15, width=500)
            self.info_frame.pack(side=LEFT, fill=X, padx=20, pady=20, expand=True)

            CTkLabel(self.info_frame, text=f"Teacher's ID", text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30, pady=(20, 0))
            CTkLabel(self.info_frame, text=f'{key}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=30)

            CTkLabel(self.info_frame, text=f"Teacher's Name", text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
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
            CTkLabel(self.info_frame, text=f'{value[5].upper()}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=30)

            CTkLabel(self.info_frame, text=f'Location', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30)
            CTkLabel(self.info_frame, text=f'{value[6].upper()}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10), padx=30)

            CTkLabel(self.info_frame, text=f'Assigned Course ID', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=30)
            CTkLabel(self.info_frame, text=f'{value[8].upper()}', text_color='white', fg_color='#2c2c2c', bg_color='#2c2c2c',
                     font=('roboto', 15, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 20), padx=30)


    def course_enrollment(self):
        pass

    def add_teachers(self):
        from teacher_registration import RegisterTeachers
        RegisterTeachers(self.display_window)

    def hiding(self):
        self.view_teachers_button.configure(fg_color='#525252')
        self.add_teachers_button.configure(fg_color='#525252')

    def sliding(self, button, methods):
        self.hiding()
        for widgets in self.display_window.winfo_children()[2::]:
            widgets.destroy()

        button.configure(fg_color='#C2C1C8')

        methods()





