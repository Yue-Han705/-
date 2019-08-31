import tkinter as tk
from PIL import ImageTk, Image
import random
import sys
import os

WINDOW_TITLE = "毛毛腿"
LIKEYOU_PHOTO_NAME = "cat.jpeg"
POPUP_WIDTH = 200
POPUP_HEIGHT = 50

class Application(tk.Frame):
    def __init__(self, title, likeyou_photo_name, popup_width, popup_height, master=None):
        super().__init__(master)
        master.title(title)

        # Modify the behaviour of the close button so that it does nothing upon clicking
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.master = master
        self.title = title
        self.likeyou_photo_name = likeyou_photo_name
        self.popup_width = popup_width
        self.popup_height = popup_height

        self.grid()
        self.create_widgets()

        # Place the window in the middle of the screen
        master.eval('tk::PlaceWindow %s center' % master.winfo_pathname(master.winfo_id()))
    
    def get_image_path(self):
        try:
            wd = sys._MEIPASS
        except AttributeError:
            wd = os.getcwd()
        return os.path.join(wd, self.likeyou_photo_name)
    
    def on_closing(self):
        pass

    def create_widgets(self):
        self.display_likeyou_text()
        self.display_likeyou_image()
        self.display_buttons()

    def display_likeyou_text(self):
        self.likeyou_label = tk.Label(self, text="我喜欢你，有机会吗？", font=("Courier", 44))
        self.likeyou_label.grid(row=0, columnspan=2)
    
    def display_likeyou_image(self):
        likeyou_photo_data = ImageTk.PhotoImage(Image.open(self.get_image_path()))
        self.likeyou_image = tk.Label(self, image=likeyou_photo_data)
        self.likeyou_image.image = likeyou_photo_data
        self.likeyou_image.grid(row=1, columnspan=2)

    def display_buttons(self):
        self.display_yes_button()
        self.display_no_button()
    
    def display_yes_button(self):
        self.yes_button = tk.Button(self, text="有", command=self.pop_up)
        self.yes_button.grid(row=2, column=0)
    
    def display_no_button(self):
        self.no_button = tk.Button(self, text="没有")
        self.no_button.bind("<Enter>", self.move_no_button)
        self.no_button.grid(row=2, column=1)

    def pop_up(self):
        self.popup = tk.Toplevel()
        self.popup.title("ღ(´･ᴗ･`)")
        self.setup_popup_geometry()
        self.display_popup_widgets()
    
    def setup_popup_geometry(self):
        horizontal_centre = (self.master.winfo_screenwidth() - self.popup_width) // 2
        vertical_centre = (self.master.winfo_screenheight() - self.popup_height) // 2
        self.popup.geometry("{}x{}+{}+{}".format(
                self.popup_width, 
                self.popup_height, 
                horizontal_centre, 
                vertical_centre))

    def display_popup_widgets(self):
        self.display_popup_label()
        self.display_quit_button()
    
    def display_popup_label(self):
        self.popup_label = tk.Label(self.popup, text="抱住!")
        self.popup_label.grid()
    
    def display_quit_button(self):
        self.quit_button = tk.Button(self.popup, text="Close", command=self.master.destroy)
        self.quit_button.grid()
    
    def move_no_button(self, _):
        new_x_coord = random.uniform(0.1, 0.9)
        new_y_coord = random.uniform(0.1, 0.9)
        self.no_button.place(relx=new_x_coord, rely=new_y_coord)

root = tk.Tk()
app = Application(master=root, likeyou_photo_name=LIKEYOU_PHOTO_NAME, title=WINDOW_TITLE, popup_width=POPUP_WIDTH, popup_height=POPUP_HEIGHT)
app.mainloop()