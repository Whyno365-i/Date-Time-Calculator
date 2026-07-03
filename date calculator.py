from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def main():
    cal = DateCalculator()
    cal.mainloop()


class DateCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Date-Time Calculator')
        self.geometry('1100x700+250+50')

        frame = Frame(self)
        #frame.pack() is very important. fill='both': makes sure that the frame fills the entire space. #
        #expand=true: makes the frame grab more space when the window is resized 
        frame.pack(fill='both', expand=True)


class Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        for c in range(100):
            self.columnconfigure(c, weight=1)

        for r in range(100):
            self.rowconfigure(r, weight=1)

        #Path(...) turns the current script file into a Path object.
        #file is the path of the Python script itself.
        #resolve() makes it an absolute path.
        #with_name('Background.png') replaces the script’s filename with Background.png, so it points to the image file in the same folder.
        image_path = Path(__file__).resolve().with_name('Background.png')
        back_image = Image.open(image_path)
        back_image = back_image.resize((1100, 700))
        self.background_photo = ImageTk.PhotoImage(back_image)

        back_label = tk.Label(self, image=self.background_photo)
        back_label.place(x=0, y=0, relwidth=1, relheight=1)

        #TODO move over the objects
        #TODO add the validate functions and limit character amount (depends on box)
        #TODO make the time calculator with datetime
        #format years/months/day - year/month/day
        #left side
        self.label_Y_1= tk.Label(self, text='Y', font=('Arial', 25))
        self.label_Y_1.grid(row=49, column=15)

        self.years_1 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black')
        self.years_1.grid(row=50, column=15, padx=10, pady=10, sticky='')

        self.slash = tk.Label(self, text='/', font=('Arial', 25), fg= 'black')
        self.slash.grid(row=50, column=16, padx=10, pady=10, sticky='ew')

        self.label_M_1= tk.Label(self, text='M', font=('Arial', 25))
        self.label_M_1.grid(row=49, column=17)

        self.months_1 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black')
        self.months_1.grid(row=50, column=17, padx=10, pady=10, sticky='')

        self.slash2 = tk.Label(self, text='/', font=('Arial', 25), fg= 'black')
        self.slash2.grid(row=50, column=18, padx=10, pady=10, sticky='ew')

        self.label_D_1= tk.Label(self, text='D', font=('Arial', 25))
        self.label_D_1.grid(row=49, column=19)       

        self.days_1 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black')
        self.days_1.grid(row=50, column=19, padx=10, pady=10, sticky='')

        #arrow
        self.arrow= tk.Label(self, text='−', font=('Arial', 50))
        self.arrow.grid(row=50, column=23)

        #right side
        self.label_Y_2= tk.Label(self, text='Y', font=('Arial', 25))
        self.label_Y_2.grid(row=49, column=26)

        self.years_2 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black')
        self.years_2.grid(row=50, column=26, padx=10, pady=10, sticky='')

        self.slash3 = tk.Label(self, text='/', font=('Arial', 25), fg= 'black')
        self.slash3.grid(row=50, column=27, padx=10, pady=10, sticky='ew')

        self.label_M_2= tk.Label(self, text='M', font=('Arial', 25))
        self.label_M_2.grid(row=49, column=28)

        self.months_2 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black')
        self.months_2.grid(row=50, column=28, padx=10, pady=10, sticky='')

        self.slash4 = tk.Label(self, text='/', font=('Arial', 25), fg= 'black')
        self.slash4.grid(row=50, column=29, padx=10, pady=10, sticky='ew')

        self.label_D_2= tk.Label(self, text='D', font=('Arial', 25))
        self.label_D_2.grid(row=49, column=30)       

        self.days_2 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black')
        self.days_2.grid(row=50, column=30, padx=10, pady=10, sticky='')

if __name__ == '__main__':
    main()