import sqlite3
import io
from customtkinter import *
from PIL import Image
from main_window import MainWindow
from tkinter import messagebox
from datetime import datetime

import os
import sys
from classes_file import Teacher


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class RegisterTeachers:
    def __init__(self, display_window):
        self.display_window = display_window
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):

        self.scrollable_frame = CTkScrollableFrame(self.display_window, fg_color='gray95', bg_color='gray95',
                                                   )
        self.scrollable_frame.pack(fill=BOTH, expand=True)

        self.side_frame = CTkFrame(self.scrollable_frame, bg_color='gray95', fg_color='white',
                                   corner_radius=15, )
        self.side_frame.pack(side=LEFT, fill=Y, padx=20, pady=20)

        self.basic_infor_frame = CTkFrame(self.scrollable_frame, bg_color='gray95', fg_color='white',
                                          corner_radius=15, )
        self.basic_infor_frame.pack(side=LEFT, pady=20, padx=(0, 20), fill=X, expand=True)

        global default_circular_image
        image = Image.open(resource_path('images/default_photo.png'))
        default_circular_image = MainWindow.__new__(MainWindow).make_circular_image(image)
        self.teacher_photo_label = CTkLabel(self.side_frame, fg_color='white', bg_color='white', text='',
                                             image=CTkImage(default_circular_image, size=(150, 150)))
        self.teacher_photo_label.pack(padx=80, pady=(80, 10))

        self.upload_photo_button = CTkButton(self.side_frame, bg_color='white', fg_color='#0C2844', font=('roboto', 15),
                                             text='Upload photo', text_color='white', hover_color='#032F5B',
                                             text_color_disabled='white', command=self.uploading_photo)
        self.upload_photo_button.pack(pady=(0, 15))

        CTkLabel(self.side_frame, bg_color='white', fg_color='white', text='Teacher ID',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20)
        self.teacher_id_entry = CTkEntry(self.side_frame, bg_color='white', border_color='#C2C1C8', fg_color='#FAFAFF',
                                       border_width=1, height=35, text_color='#0C2844')
        self.teacher_id_entry.pack(fill=X, pady=(0, 10), padx=20)
        self.teacher_id_entry.bind('<FocusIn>', lambda event: self.teacher_id_entry.configure(border_color='#7E6AFE'))
        self.teacher_id_entry.bind('<FocusOut>', lambda event: self.teacher_id_entry.configure(border_color='#C2C1C8'))
        
        CTkLabel(self.side_frame, bg_color='white', fg_color='white', text='Teaching Course ID',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X, padx=20)
        self.course_entry = CTkEntry(self.side_frame, bg_color='white', border_color='#C2C1C8', fg_color='#FAFAFF',
                                       border_width=1, height=35, text_color='#0C2844')
        self.course_entry.pack(fill=X, padx=20)
        self.course_entry.bind('<FocusIn>', lambda event: self.course_entry.configure(border_color='#7E6AFE'))
        self.course_entry.bind('<FocusOut>', lambda event: self.course_entry.configure(border_color='#C2C1C8'))

        
        # working on teacher basic information
        two_frames_holder = CTkFrame(self.basic_infor_frame, fg_color='white', bg_color='white')
        two_frames_holder.pack(fill=X, expand=True, pady=(10, 0))

        first_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        first_frame.pack(side=LEFT, fill=X, padx=20, pady=20, expand=True)

        second_frame = CTkFrame(two_frames_holder, fg_color='white', bg_color='white')
        second_frame.pack(side=LEFT, fill=BOTH, padx=(0, 20), pady=20, expand=True)
        self.basic_infor_label = CTkLabel(first_frame, bg_color='white', fg_color='white', text='Basic Information',
                                          text_color='#0C2844', font=('roboto', 16, 'bold'), justify=LEFT, anchor='w')
        self.basic_infor_label.pack(fill=X, pady=(0, 10))

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Surname',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.sur_name_entry = CTkEntry(first_frame, bg_color='white', border_color='#C2C1C8', fg_color='#FAFAFF',
                                       border_width=1, height=35, text_color='#0C2844')
        self.sur_name_entry.pack(fill=X, pady=(0, 10))
        self.sur_name_entry.bind('<FocusIn>', lambda event: self.sur_name_entry.configure(border_color='#7E6AFE'))
        self.sur_name_entry.bind('<FocusOut>', lambda event: self.sur_name_entry.configure(border_color='#C2C1C8'))

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Other Names',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.other_name_entry = CTkEntry(first_frame, bg_color='white', border_color='#C2C1C8', fg_color='#FAFAFF',
                                         border_width=1, height=35, text_color='#0C2844')
        self.other_name_entry.pack(fill=X, pady=(0, 10))
        self.other_name_entry.bind('<FocusIn>', lambda event: self.other_name_entry.configure(border_color='#7E6AFE'))
        self.other_name_entry.bind('<FocusOut>', lambda event: self.other_name_entry.configure(border_color='#C2C1C8'))

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='Email',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.email_entry = CTkEntry(first_frame, bg_color='white', border_color='#C2C1C8', fg_color='#FAFAFF',
                                    border_width=1, height=35, text_color='#0C2844', placeholder_text=
                                    'example@gmail.com', placeholder_text_color='gray50')
        self.email_entry.pack(fill=X, pady=(0, 10))
        self.email_entry.bind('<FocusIn>', lambda event: self.email_entry.configure(border_color='#7E6AFE'))
        self.email_entry.bind('<FocusOut>', lambda event: self.email_entry.configure(border_color='#C2C1C8'))

        CTkLabel(first_frame, bg_color='white', fg_color='white', text='National ID No.',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.id_number_entry = CTkEntry(first_frame, bg_color='white', border_color='#C2C1C8', fg_color='#FAFAFF',
                                        border_width=1, height=35, text_color='#0C2844', placeholder_text=
                                        "Teacher's NIN", placeholder_text_color='gray50')
        self.id_number_entry.pack(fill=X)
        self.id_number_entry.bind('<FocusIn>', lambda event: self.id_number_entry.configure(border_color='#7E6AFE'))
        self.id_number_entry.bind('<FocusOut>', lambda event: self.id_number_entry.configure(border_color='#C2C1C8'))

        """Working on the second frame"""
        CTkLabel(second_frame, bg_color='white', fg_color='white', text='',
                 text_color='#0C2844', font=('roboto', 16, 'bold'), justify=LEFT, anchor='w').pack(fill=X, pady=(0, 10))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='First Name',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.first_name_entry = CTkEntry(second_frame, bg_color='white', border_color='#C2C1C8', fg_color='#FAFAFF',
                                         border_width=1, height=35, text_color='#0C2844')
        self.first_name_entry.pack(fill=X, pady=(0, 10))
        self.first_name_entry.bind('<FocusIn>', lambda event: self.first_name_entry.configure(border_color='#7E6AFE'))
        self.first_name_entry.bind('<FocusOut>', lambda event: self.first_name_entry.configure(border_color='#C2C1C8'))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='Phone Number',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.phone_entry = CTkEntry(second_frame, bg_color='white', border_color='#C2C1C8', fg_color='#FAFAFF',
                                    border_width=1, height=35, text_color='#0C2844', placeholder_text=
                                    '07XXXXXXXXXX', placeholder_text_color='gray50')
        self.phone_entry.pack(fill=X, pady=(0, 10))
        self.phone_entry.bind('<FocusIn>', lambda event: self.phone_entry.configure(border_color='#7E6AFE'))
        self.phone_entry.bind('<FocusOut>', lambda event: self.phone_entry.configure(border_color='#C2C1C8'))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='Gender',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)

        self.gender_value = StringVar()
        self.gender_value.set('Select')
        self.genders = ['MALE', 'FEMALE']
        self.gender_combo = CTkComboBox(second_frame, variable=self.gender_value, text_color='gray20',
                                        border_color='#C2C1C8',
                                        fg_color='#FAFAFF', values=self.genders, border_width=1, bg_color='white',
                                        height=35,
                                        dropdown_fg_color='white', dropdown_hover_color='#DBEAFF',
                                        dropdown_text_color='black'
                                        , button_hover_color='#C2C1C8', button_color='#C2C1C8')
        self.gender_combo.pack(fill=X, pady=(0, 10))

        CTkLabel(second_frame, bg_color='white', fg_color='white', text='Location',
                 text_color='#0C2844', font=('roboto', 15), justify=LEFT, anchor='w').pack(fill=X)
        self.location_entry = CTkEntry(second_frame, bg_color='white', border_color='#C2C1C8', fg_color='#FAFAFF',
                                       border_width=1, height=35, text_color='#0C2844')
        self.location_entry.pack(fill=X)
        self.location_entry.bind('<FocusIn>', lambda event: self.location_entry.configure(border_color='#7E6AFE'))
        self.location_entry.bind('<FocusOut>', lambda event: self.location_entry.configure(border_color='#C2C1C8'))

        """Save teacher button here"""
        self.save_frame = CTkFrame(self.basic_infor_frame, fg_color='white', bg_color='white')
        self.save_frame.pack(fill=X, padx=20, pady=(10, 80), expand=True)
        self.save_button = CTkButton(self.save_frame, bg_color='white', fg_color='#725cff', hover_color='#7E6AFE',
                                     image=CTkImage(Image.open(resource_path('icons/save.png')), size=(20, 20)),
                                     text_color='white',
                                     text='Save', command=self.saving_teacher)
        self.save_button.pack(side=RIGHT)

    def uploading_photo(self):
        try:
            self.passport_image_browsed = 'images/default_photo.png'
            self.passport_image_browsed = filedialog.askopenfilename(title='Select teacher passport photo',
                                                                     filetypes=(
                                                                     ('jpg files', '*.jpg'), ('png files', '*.png'),
                                                                     ('All types', '*.*')))

            current_current_passport = Image.open(resource_path(self.passport_image_browsed))

            circular_image = MainWindow.__new__(MainWindow).make_circular_image(current_current_passport)
            self.teacher_photo_label.configure(image=CTkImage(circular_image, size=(150, 150)))
        except AttributeError:
            self.passport_image_browsed = 'images/default_photo.png'
            current_current_passport = Image.open(resource_path(self.passport_image_browsed))
            circular_image = MainWindow.__new__(MainWindow).make_circular_image(current_current_passport)
            self.teacher_photo_label.configure(image=CTkImage(circular_image, size=(150, 150)))

    def saving_teacher(self):
        condition1 = self.first_name_entry.get().strip() == '' or self.sur_name_entry.get().strip() == ''
        condition2 = (self.phone_entry.get().strip() == '' or self.gender_value.get().strip() == 'Select' or
                      self.location_entry.get().strip() == '')
        if condition1 or condition2:
            MainWindow.__new__(MainWindow).unsuccessful_information('All fields are required')
            return

        if self.email_entry.get().strip() == '':
            pass
        else:
            import re
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
                MainWindow.__new__(MainWindow).unsuccessful_information('Invalid email address')
                return

        if not self.phone_entry.get().strip().isdigit() or len(self.phone_entry.get().strip()) != 10:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid phone number')
            return

        if not self.gender_value.get() in ['MALE', 'FEMALE']:
            MainWindow.__new__(MainWindow).unsuccessful_information('Invalid gender')
            return


        def resetting_fields():
            self.sur_name_entry.delete(0, END)
            self.first_name_entry.delete(0, END)
            if self.other_name_entry.get() == '':
                pass
            else:
                self.other_name_entry.delete(0, END)
            self.teacher_photo_label.configure(image=CTkImage(default_circular_image, size=(150, 150)))
            self.passport_image_browsed = 'images/default_photo.png'
            self.id_number_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.location_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.sur_name_entry.focus_set()

        try:
            """Adding teacher from here"""
            teacher_object = Teacher(self.sur_name_entry.get(), self.first_name_entry.get(), self.gender_value.get(),
                                     self.phone_entry.get(), self.email_entry.get(), self.id_number_entry.get(),
                                     self.location_entry.get(), self.teacher_id_entry.get(), self.course_entry.get().upper())

            teacher_object.register_teacher()

            MainWindow.__new__(MainWindow).success_information(f'Teacher successfully registered.')
            resetting_fields()

        except AttributeError:
            self.passport_image_browsed = 'images/default_photo.png'
            self.saving_teacher()

    def update_photo(self):

        try:
            self.new_passport_image_browsed = filedialog.askopenfilename(title='Select teacher passport photo',
                                                                         filetypes=(
                                                                             ('jpg files', '*.jpg'),
                                                                             ('png files', '*.png'),
                                                                             ('All types', '*.*')))

            current_current_passport = Image.open(resource_path(self.new_passport_image_browsed))

            circular_image = MainWindow.__new__(MainWindow).make_circular_image(current_current_passport)
            self.teacher_photo_label.configure(image=CTkImage(circular_image, size=(150, 150)))
            self.previous_directory = self.new_passport_image_browsed
        except AttributeError:
            try:
                self.new_passport_image_browsed = self.previous_directory
            except AttributeError:
                pass


    def deleting_teacher(self, teacher_data):
        confirm_deletion = messagebox.askyesno('Confirm deletion', f'Are you sure you want to \n'
                                                                   f'permanently delete {teacher_data[2].split()[-1]}',
                                               parent=self.display_window)
        if confirm_deletion:
            connection = sqlite3.connect(resource_path('munange.db'))
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(f"DELETE FROM teachers WHERE teacher_id='{teacher_data[0]}'")
            connection.commit()
            cursor.close()
            connection.close()
            MainWindow.__new__(MainWindow).success_information(f'teacher successfully deleted.')
            self.back_to_view_teachers()

    def emptying_data_fields(self):
        self.upload_photo_button.configure(state=DISABLED)
        # self.basic_infor_label.configure(text='Add a guarantor')
        self.sur_name_entry.delete(0, END)
        self.first_name_entry.delete(0, END)
        self.other_name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.id_number_entry.delete(0, END)
        self.location_entry.delete(0, END)
        self.gender_value.set('Select')
        # self.delete_button.pack_forget()
        # self.save_button.configure(text='Save', command=lambda : self.save_guarantor(teacher_data))
        self.phone_entry.focus_set()
        self.email_entry.focus_set()
        self.id_number_entry.focus_set()
        self.sur_name_entry.focus_set()

