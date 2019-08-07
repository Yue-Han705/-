import tkinter as tk
from PIL import ImageTk, Image
import random

class Application(tk.Frame):
    def __init__(self, master=None, title="毛毛腿"):
        super().__init__(master)
        master.title(title)

        # Modify the behaviour of the close button so that it does nothing upon clicking
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.master = master
        self.grid()
        self.create_widgets()

        # Place the window in the middle of the screen
        master.eval('tk::PlaceWindow %s center' % master.winfo_pathname(master.winfo_id()))
    
    def on_closing(self):
        pass

    def create_widgets(self):
        """Creates widgets of the root window."""
        # Display text
        self.likeyou_label = tk.Label(self, text="我喜欢你，有机会吗？", font=("Courier", 44))
        self.likeyou_label.grid(row=0, columnspan=2)

        # Display image
        photo = ImageTk.PhotoImage(Image.open("cat.jpeg"))
        self.likeyou_image = tk.Label(self, image=photo)
        self.likeyou_image.image = photo
        self.likeyou_image.grid(row=1, columnspan=2)

        # Display the two buttons
        self.yes_button = tk.Button(self, text="有", command=self.pop_up)
        self.yes_button.grid(row=2, column=0)
        self.no_button = tk.Button(self, text="没有")
        self.no_button.bind("<Enter>", self.move)
        self.no_button.grid(row=2, column=1)


    def pop_up(self):
        """Displays a popup window that has a button which allows user to close the program"""
        self.popup = tk.Toplevel()
        self.popup.title("ღ(´･ᴗ･`)")
        popup_width = 200
        popup_height = 50
        self.popup.geometry("{}x{}+{}+{}".format(popup_width, popup_height, 
                                                (self.master.winfo_screenwidth() - popup_width) // 2, 
                                                (self.master.winfo_screenheight() - popup_height) // 2))
        self.popup_label = tk.Label(self.popup, text="抱住!")
        self.popup_label.grid()
        self.quit_button = tk.Button(self.popup, text="Close", command=self.master.destroy)
        self.quit_button.grid()
    
    def move(self, _):
        """Moves the no button to somewhere else"""
        x_coord = random.uniform(0.1, 0.9)
        y_coord = random.uniform(0.1, 0.9)
        self.no_button.place(relx=x_coord, rely=y_coord)

root = tk.Tk()
app = Application(master=root)
app.mainloop()