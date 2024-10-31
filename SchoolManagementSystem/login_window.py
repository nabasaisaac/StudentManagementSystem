from customtkinter import *
import sqlite3
from tkinter import *
from PIL import Image, ImageFilter, ImageTk, ImageEnhance, ImageSequence

class Login_window:
    def __init__(self, window):
        self.window = window
        window.title('')
        # window.minsize(500, 500)
        window.geometry(f'1000x600+200+100')
        # window.geometry('1000x700+100+100')
        window.iconbitmap('icons/splash.ico')
        self.calling_all_methods_here()

    def calling_all_methods_here(self):
        self.designing_window(self.window)
        # self.splash_screen()

    def process_image(self, image_path, blur_radius=20, transparency=20):
        # Open the image
        image = Image.open(image_path).convert("RGBA")

        # Apply Gaussian blur
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))

        # Apply transparency
        alpha = blurred_image.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(transparency / 255.0)
        blurred_image.putalpha(alpha)

        return blurred_image

    def designing_window(self, window):
        self.window.attributes('-topmost', False)
        self.window.after(0, lambda: window.wm_state('zoomed'))
        self.window.iconbitmap('icons/login.ico')
        self.window.title('Login')
        self.window.minsize(450, 600)
        self.window.maxsize(self.window.winfo_screenwidth(), self.window.winfo_screenheight())

        self.background = Frame(window, bg='white')
        self.background.pack(expand=True, fill=BOTH)
        global background_photo, processed_img

        processed_img = self.process_image("images/5.jpg", blur_radius=8, transparency=500)
        background_photo = ImageTk.PhotoImage(processed_img)
        self.side_frame_canvas = Canvas(self.background, bg='white', highlightbackground='black')
        self.side_frame_canvas.place(rely=1, relheight=1, anchor='sw', relwidth=1)

        # Making image fit in the side frame using this function
        def side_resizer(e):
            global b, resized_b, new_b
            b = processed_img
            resized_b = b.resize((e.width, e.height), Image.LANCZOS)
            new_b = ImageTk.PhotoImage(resized_b)
            self.side_frame_canvas.create_image(0, 0, image=new_b, anchor='nw')

        self.side_frame_canvas.bind('<Configure>', side_resizer)

        self.login_frame = CTkFrame(self.background, width=350, height=450, corner_radius=40, fg_color='#ffffff',
                                    bg_color='white')
        self.login_frame.pack(pady=100)

        self.welcome = CTkLabel(self.login_frame, text='Welcome back', text_color='black', font=('roboto', 25))
        self.welcome.pack(padx=30, pady=(20, 0))
        slogan = CTkLabel(self.login_frame, text='Very many things are waiting for you!\n\n', text_color='gray60',
                          font=('roboto', 13))
        slogan.pack()

        self.user_name = CTkLabel(self.login_frame, text='Username\t\t\t', text_color='black', font=('roboto', 15))
        self.user_name.pack()

        self.user_name_entry = CTkEntry(self.login_frame, fg_color='#FAFAFF', bg_color='white', corner_radius=10,
                                        border_width=1, width=250, text_color='gray20', height=35,
                                        border_color='#725cff',
                                        font=('roboto', 15))
        self.user_name_entry.pack(padx=40)
        self.user_name_entry.bind('<FocusIn>', lambda event: self.user_name_entry.configure(border_color='#7E6AFE'))
        self.user_name_entry.bind('<FocusOut>', lambda event: self.user_name_entry.configure(border_color='#725cff'))

        CTkLabel(self.login_frame, text='').pack()

        self.password = CTkLabel(self.login_frame, text='Password\t\t\t', text_color='black', font=('roboto', 15))
        self.password.pack()

        self.password_entry = CTkEntry(self.login_frame, fg_color='#FAFAFF', bg_color='white', corner_radius=10,
                                       border_width=1, width=250, text_color='gray20', height=35, font=('roboto', 15),
                                       border_color='#725cff', show='●')
        self.password_entry.pack(padx=40)
        self.password_entry.bind('<FocusIn>', lambda event: self.password_entry.configure(border_color='#7E6AFE'))
        self.password_entry.bind('<FocusOut>', lambda event: self.password_entry.configure(border_color='#725cff'))

        def hide_password():
            closed_eye.configure(image=CTkImage(Image.open('icons/closed_eye.png'), size=(20, 20)),
                                 command=show_password)
            self.password_entry.configure(show='●')

        def show_password():
            closed_eye.configure(image=CTkImage(Image.open('icons/open_eye.png'), size=(20, 20)),
                                 command=hide_password)
            self.password_entry.configure(show='')

        closed_eye = CTkButton(self.password_entry,
                               image=CTkImage(Image.open('icons/closed_eye.png'), size=(20, 20)),
                               bg_color='white', fg_color='#FAFAFF', width=10, height=10, text='', hover_color='#FAFAFF',
                               command=show_password)
        closed_eye.place(relx=0.85, rely=0.1)

        self.forgot_password = CTkButton(self.login_frame, text='Forgot password?', text_color='#725cff', font=('roboto', 15),
                                         bg_color='white', fg_color='white', hover_color='white',
                                         command=self.forgot_password)
        self.forgot_password.pack(side=BOTTOM, pady=(15, 25))

        self.login_button = CTkButton(self.login_frame, text='Login', bg_color='white', fg_color='#725cff',
                                      corner_radius=10,
                                      width=250, height=35, hover_color='#7E6AFE', compound=RIGHT,
                                      border_color='gray50',
                                      image=CTkImage(Image.open('images/back_image.png')),
                                      font=('roboto', 15),
                                      command=lambda: self.main_window(None, self.window))

        self.login_button.pack(side=BOTTOM, pady=(30, 0))
        self.window.bind('<Return>', lambda event: self.main_window(event, window))
        # self.window.resizable(True, True)

    def main_window(self, event, window):

        self.window.iconbitmap('icons/home2.ico')
        self.window.title('Home')
        # if self.user_name_entry.get().strip() == '' or self.password_entry.get().strip() == '':
        #     self.unsuccessful_information('All fields are required')
        #     return

        self.window.after(0, lambda: window.wm_state('zoomed'))

        from main_window import MainWindow

        self.login_frame.pack_forget()
        self.side_frame_canvas.place_forget()
        self.background.config(bg='white')
        CTkLabel(self.background, text='Getting things ready for you . . .', bg_color='white', fg_color='#725cff',
                 corner_radius=15, width=150, height=40, font=('roboto', 15)).pack(side=TOP, pady=15)

        self.window.unbind('<Return>')

        def next_window():
            self.login_button.pack_forget()
            self.background.pack_forget()
            MainWindow(window)

        self.loading_gif(next_window)

    def loading_gif(self, function):
        def animate(index):
            if index < 20:  # Only continue the animation loop until index reaches 20
                frame = gif_frames[index]
                index = (index + 1) % len(gif_frames)
                label.configure(image=frame)
                label.after(50, animate, index)
            else:
                label.pack_forget()
                function()  # Call the provided function when index reaches 20
                return

        gif_path = "images/giphy.gif"
        gif = Image.open(gif_path)
        gif2 = ImageTk.PhotoImage(Image.open(gif_path))
        gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
        label = Label(self.background, image=gif2, bg='white', fg='white', text='', width=200, height=200)
        label.pack(fill=BOTH, expand=True, side=TOP)

        animate(0)  # Start the animation loop

    def success_information(self, info):
        global y, y28pyi
        y = 0
        y2 = 0.07

        def destroying_label():
            global y2
            if y2 >= -0.1:  # Continue animating while y is less than 0.4
                y2 -= 0.01
                correct_input.place(relx=0.35, rely=y2)
                self.window.after(4, destroying_label)
            else:
                correct_input.destroy()
                self.back_here()

        def animating_label():
            global y
            if y < 0.07:  # Continue animating while y is less than 0.4
                y += 0.01
                correct_input.place(relx=0.35, rely=y)
                self.window.after(5, animating_label)  # Call the function again after 10ms
            else:  # If y is 0.4 or more, stop animation
                correct_input.place(relx=0.35, rely=y)  # Ensure the label is placed
                # destroying_label()
                self.window.after(2000, destroying_label)

        correct_input = CTkLabel(self.window, text=f'   {info}  ', text_color='#725cff', bg_color='#e9edf2',
                                 fg_color='white', corner_radius=5, width=70, height=45, compound=LEFT,
                                 image=CTkImage(Image.open('icons/tick.png')), font=('roboto', 15))

        correct_input.place(relx=0.35, rely=0.3)
        animating_label()

    def unsuccessful_information(self, info):
        global y, y2
        y = 0
        y2 = 0.07

        def destroying_label():
            global y2
            if y2 >= -0.1:  # Continue animating while y is less than 0.4
                y2 -= 0.01
                invalid_input.place(relx=0.42, rely=y2)
                self.window.after(4, destroying_label)
            else:
                invalid_input.destroy()

        def animating_label():
            global y
            if y < 0.07:  # Continue animating while y is less than 0.4
                y += 0.01
                invalid_input.place(relx=0.42, rely=y)
                self.window.after(5, animating_label)  # Call the function again after 10ms
            else:  # If y is 0.4 or more, stop animation
                invalid_input.place(relx=0.42, rely=y)  # Ensure the label is placed
                # destroying_label()
                self.window.after(2000, destroying_label)

        invalid_input = CTkLabel(self.window, text=f'   {info}  ', text_color='red', bg_color='gray95',
                                 fg_color='#FFEEEE', font=('roboto', 15),
                                 corner_radius=10, width=70, height=45,
                                 image=CTkImage(Image.open('icons/cancel.png')),
                                 compound=LEFT)
        animating_label()

    def forgot_password(self):
        pass
    
    def back_here(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        Login_window(self.window)

def main():
    main_window = CTk()
    Login_window(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    main()

