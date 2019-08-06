import tkinter as tk
from PIL import ImageTk, Image
import random

class Application(tk.Frame):
    def __init__(self, master=None, title="大妹子", width=500, height=800):
        super().__init__(master)

        # Configure the root window
        master.title(title)
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.laptop_width = master.winfo_screenwidth()
        self.laptop_height = master.winfo_screenheight()
        master.geometry("{}x{}+{}+{}".format(width, height, (self.laptop_width - width) // 2, (self.laptop_height - height) // 2))
        
        self.master = master
        self.pack()
        self.create_widgets()
    
    def on_closing(self):
        pass

    def create_widgets(self):
        # Display text
        self.likeyou_label = tk.Label(self, text="我喜欢你，有机会吗？", font=("Courier", 44))
        self.likeyou_label.pack()

        # Display image
        photo = ImageTk.PhotoImage(Image.open("cat.jpeg"))
        self.likeyou_image = tk.Label(self, image=photo)
        self.likeyou_image.image = photo
        self.likeyou_image.pack()

        # Display the two buttons
        self.yes_button = tk.Button(self, text="有", command=self.pop_up)
        self.yes_button.pack()
        self.no_button = tk.Button(self, text="没有")
        self.no_button.bind("<Enter>", self.reappear)
        self.no_button.place(x=0, y=0)

    def pop_up(self):
        # Display a popup window that allows user to close the window
        self.popup = tk.Toplevel()
        self.popup.title("ღ(´･ᴗ･`)")
        popup_width = 200
        popup_height = 50
        self.popup.geometry("{}x{}+{}+{}".format(popup_width, popup_height, 
            (self.laptop_width - popup_width) // 2, (self.laptop_height - popup_height) // 2))
        self.popup_label = tk.Label(self.popup, text="抱住!")
        self.popup_label.pack()
        self.quit_button = tk.Button(self.popup, text="Close", command=self.master.destroy)
        self.quit_button.pack()
    
    def reappear(self, _):
        self.no_button.place(x=10, y=10)

root = tk.Tk()
app = Application(master=root)
app.mainloop()