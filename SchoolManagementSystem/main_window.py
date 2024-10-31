from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageOps, ImageSequence
import io
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class MainWindow:
    def __init__(self, display_window):
        self.display_window = display_window
        self.frames_holder = CTkFrame(self.display_window, bg_color='gray95', fg_color='gray95')
        self.frames_holder.pack(expand=True, fill=BOTH)
        self.bottom_frame = CTkFrame(self.display_window, bg_color='gray20', fg_color='gray20', height=40)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        self.all_methods_here()

    def all_methods_here(self):
        self.designing_window()

    def designing_window(self):
        global upper_frame
        upper_frame = CTkFrame(self.frames_holder, bg_color='gray95', corner_radius=0, fg_color='#e9edf2',
                                )
        upper_frame.pack(fill=X)

        self.side_frame = CTkFrame(self.frames_holder, bg_color='#2c2c2c', corner_radius=0, fg_color='#2c2c2c',
                                   )
        self.side_frame.pack(side=LEFT, fill=Y)
        self.munange_logo = CTkLabel(upper_frame, fg_color='#2c2c2c', corner_radius=0, width=200, text='',
                                     image=CTkImage(Image.open(resource_path('images/5.jpg')), size=(200, 100)))
        self.munange_logo.pack(side=LEFT)

        self.display_frame = CTkFrame(self.frames_holder, bg_color='gray40', corner_radius=0, fg_color='gray40',
                                   )
        self.display_frame.pack(side=LEFT, fill=BOTH, expand=True)

        CTkLabel(upper_frame, text='STUDENT MANAGEMENT SYSTEM - GROUP 3', font=('roboto', 16, 'bold'), fg_color='#e9edf2',
                 bg_color='#e9edf2', text_color='#382F86').pack(side=LEFT, padx=(20, 0))

        """Working on the profile of the user"""
        global profile_button
        profile_photo = self.make_circular_image(Image.open('images/default_passport.png'))
        profile_button = CTkButton(upper_frame, bg_color='#e9edf2', fg_color='#e9edf2', compound=RIGHT,
                                   text='Group 3 Admi...\ngroup3@gma...', text_color='#172b4c', font=('roboto', 15),
                                   hover_color='#e9edf2', image=CTkImage(profile_photo, size=(60, 60)),
                                        command=lambda: self.sliding(profile_button, self.profile,
                                                                     self.display_frame))

        profile_button.pack(side=RIGHT, padx=(10, 15))

        self.language_button = CTkButton(upper_frame, bg_color='#e9edf2', fg_color='white', compound=LEFT, width=100,
                                        image=CTkImage(Image.open(resource_path('images/english.png')), size=(15, 10)), text='English',
                                        text_color='#172b4c', font=('roboto', 15), hover_color='#e9edf2', height=40)

        self.language_button.pack(side=RIGHT, padx=(10, 5))
        self.language_button.bind('<Enter>', lambda event: self.language_button.configure(text_color='#44aaee',
                                                                                          fg_color='#e9edf2'))
        self.language_button.bind('<Leave>', lambda event: self.language_button.configure(text_color='#172b4c',
                                                                                          fg_color='white'))

        self.student_reg_button = CTkButton(self.side_frame, bg_color='#2c2c2c', fg_color='#2c2c2c', corner_radius=15,
                                     width=150, height=40, hover_color='#525252', text_color='white',
                                     text='Students', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open(resource_path('icons/students2.png')), size=(20, 20)),
                                     border_color='#2c2c2c', border_width=1, command=lambda: self.sliding(self.student_reg_button,
                                     self.student_registration, self.display_frame))

        self.student_reg_button.pack(side=TOP, padx=25, pady=(15, 0))

        self.teacher_reg_button = CTkButton(self.side_frame, bg_color='#2c2c2c', fg_color='#2c2c2c', corner_radius=15,
                                     width=150, height=40, hover_color='#525252', text_color='white',
                                     text='Teachers', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open(resource_path('icons/employees.png')), size=(20, 20)),
                                     border_color='#2c2c2c', border_width=1, command=lambda: self.sliding(self.teacher_reg_button,
                                     self.teacher_registration, self.display_frame))

        self.teacher_reg_button.pack(side=TOP, padx=25)

        self.course_enrollment_button = CTkButton(self.side_frame, bg_color='#2c2c2c', fg_color='#2c2c2c', corner_radius=15,
                                     width=150, height=40, hover_color='#525252', text_color='white',
                                     text='Courses', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open(resource_path('icons/dashboard.png')), size=(20, 20)),
                                     border_color='#2c2c2c', border_width=1, command=lambda: self.sliding(self.course_enrollment_button,
                                     self.course_enrollment, self.display_frame))

        self.course_enrollment_button.pack(side=TOP, padx=25)

        self.grades_button = CTkButton(self.side_frame, bg_color='#2c2c2c', fg_color='#2c2c2c', corner_radius=15,
                                     width=150, height=40, hover_color='#525252', text_color='white',
                                     text='Grades', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open(resource_path('icons/reports.png')), size=(20, 20)),
                                     border_color='#2c2c2c', border_width=1, command=lambda: self.sliding(self.grades_button,
                                     self.grades, self.display_frame))

        self.grades_button.pack(side=TOP)

        self.sliding(self.student_reg_button, self.student_registration, self.display_frame)

        self.logout_button = CTkButton(self.side_frame, bg_color='#2c2c2c', fg_color='#2c2c2c', corner_radius=15,
                                     width=150, height=40, hover_color='#525252', text_color='white',
                                     text='Logout', font=('roboto', 15), compound=LEFT, anchor='w',
                                     image=CTkImage(Image.open(resource_path('icons/logout.png')), size=(20, 20)),
                                    command=self.log_out)
        self.logout_button.pack(side=BOTTOM, padx=25, pady=10)

    def student_registration(self, display_frame):
        from student_GUI import StudentGUI
        StudentGUI(display_frame)

    def teacher_registration(self, display_frame):
        from teacher_GUI import TeacherGUI
        TeacherGUI(display_frame)
    def course_enrollment(self, display_frame):
        from courseGUI import CourseGUI
        CourseGUI(display_frame)

    def grades(self, display_frame):
        from grade_GUI import GradeGUI
        GradeGUI(display_frame)

    def hiding_hover(self):
        self.student_reg_button.configure(fg_color='#2c2c2c')
        self.teacher_reg_button.configure(fg_color='#2c2c2c')
        self.course_enrollment_button.configure(fg_color='#2c2c2c')
        self.grades_button.configure(fg_color='#2c2c2c')

    def sliding(self, button, function, parameters):

        self.hiding_hover()
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        button.configure(fg_color='#725cff')

        def methods():
            function(parameters)
        self.loading_gif(methods)

    def loading_gif(self, function):
        def animate(index):
            if index < 20:  # Only continue the animation loop until index reaches 20
                frame = gif_frames[index]
                index = (index + 1) % len(gif_frames)
                label.configure(image=frame)
                label.after(25, animate, index)
            else:
                label.pack_forget()
                function()
                return # Call the provided function when index reaches 20

        gif_path = "images/giphy.gif"
        gif = Image.open(resource_path(gif_path))
        gif2 = ImageTk.PhotoImage(Image.open(gif_path))
        gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
        label = Label(self.display_frame, image=gif2, bg='white', fg='white', text='', width=100, height=100)
        label.pack(expand=True, fill=BOTH)

        animate(0)  # Start the animation loop

    def success_information(self, info):
        global y, y2
        y = 0
        y2 = 0.4

        def destroying_label():
            global y2
            if y2 >= -0.1:  # Continue animating while y is less than 0.4
                y2 -= 0.01
                correct_input.place(relx=0.5, rely=y2)
                upper_frame.after(2, destroying_label)
            else:
                correct_input.destroy()

        def animating_label():
            global y
            if y < 0.4:  # Continue animating while y is less than 0.4
                y += 0.01
                correct_input.place(relx=0.5, rely=y)
                upper_frame.after(3, animating_label)  # Call the function again after 10ms
            else:  # If y is 0.4 or more, stop animation
                correct_input.place(relx=0.5, rely=y)  # Ensure the label is placed
                # destroying_label()
                upper_frame.after(2000, destroying_label)

        correct_input = CTkLabel(upper_frame, text=f'   {info}  ', text_color='#725cff', bg_color='#e9edf2',
                                 fg_color='white', corner_radius=5, width=70, height=45, compound=LEFT,
                                 image=CTkImage(Image.open(resource_path('icons/tick.png'))), font=('roboto', 15))

        correct_input.place(relx=0.5, rely=0.3)
        animating_label()

    def unsuccessful_information(self, info):
        global y, y2
        y = 0
        y2 = 0.4

        def destroying_label():
            global y2
            if y2 >= -0.1:  # Continue animating while y is less than 0.4
                y2 -= 0.01
                invalid_input.place(relx=0.5, rely=y2)
                upper_frame.after(2, destroying_label)
            else:
                invalid_input.destroy()

        def animating_label():
            global y
            if y < 0.4:  # Continue animating while y is less than 0.4
                y += 0.01
                invalid_input.place(relx=0.5, rely=y)
                upper_frame.after(3, animating_label)  # Call the function again after 10ms
            else:  # If y is 0.4 or more, stop animation
                invalid_input.place(relx=0.5, rely=y)  # Ensure the label is placed
                # destroying_label()
                upper_frame.after(2000, destroying_label)

        invalid_input = CTkLabel(upper_frame, text=f'   {info}  ', text_color='red', bg_color='#e9edf2', fg_color='#FFEEEE',
                                 corner_radius=10, width=70, height=45, image=CTkImage(Image.open(resource_path('icons/cancel.png'))),
                                 compound=LEFT, font=('roboto', 15))
        animating_label()

    def make_circular_image(self, image):
        diameter = min(image.size)
        # Create a mask (black with a white circle)
        mask = Image.new("L", (diameter, diameter), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, diameter, diameter), fill=255)

        # Crop the image to a square
        square_image = ImageOps.fit(image, (diameter, diameter), centering=(0.5, 0.5))

        # Apply the mask to get the circular image
        circular_image = ImageOps.fit(image, (diameter, diameter), centering=(0.5, 0.5))
        circular_image.putalpha(mask)

        return circular_image

    def log_out(self):
        confirm_logout = messagebox.askyesno('Confirm Logout', 'Are you sure you want to exit?',
                                             parent=self.display_window)
        if confirm_logout:
            sys.exit()

