from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from dateutil.relativedelta import relativedelta


def main():
    cal = DateCalculator()
    cal.mainloop()


class DateCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Date-Time Calculator')
        self.geometry('1100x700+250+50')

        self.style= ttk.Style()
        self.style.configure('bgcolor.TFrame', background= 'blue')

        frame = Frame(self, style= 'bgcolor.TFrame')
        #frame.pack() is very important. fill='both': makes sure that the frame fills the entire space. #
        #expand=true: makes the frame grab more space when the window is resized 
        frame.pack(fill='both', expand=True)


class Frame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.change3= 3

        for c in range(100):
            self.columnconfigure(c, weight=1)

        for r in range(100):
            self.rowconfigure(r, weight=1)

        #Path(...) turns the current script file into a Path object.
        #file is the path of the Python script itself.
        #resolve() makes it an absolute path.
        #with_name('Background.png') replaces the script’s filename with Background.png, so it points to the image file in the same folder.

        #I am not doing this because I can't figure out how to make the boxes of the label transparent
        # image_path = Path(__file__).resolve().with_name('Background.png')
        # back_image = Image.open(image_path)
        # back_image = back_image.resize((1100, 700))
        # self.background_photo = ImageTk.PhotoImage(back_image)

        # back_label = tk.Label(self, image=self.background_photo)
        # back_label.place(x=0, y=0, relwidth=1, relheight=1)

        #TODO add the validate functions and limit character amount (depends on box)

        def validate_Y_M(c):
            #c= character

            if c== '':
                return True
            
            for char in c:
                if (not char.isdigit()):
                    return False

            if len(c) == 3:
                return False
            
            if int(c) > 12:
                return False

            return True
        
        def validate_D(c):
            #c= character

            if c== '':
                return True
            
            for char in c:
                if (not char.isdigit()):
                    return False

            if len(c) == 3:
                return False
            
            if int(c) > 31:
                return False

            return True

        self.validate_cmd= ((self.register(validate_Y_M)), '%P')
        self.validate_cmd_D= ((self.register(validate_D)), '%P')

        #TODO make the time calculator with datetime

        #validation types:
        #key= triggers at every click of a button
        #foucus= triggers when you click off or on the entry
        #focusin= only triggers when entry is clicked
        #focusout= only triggers when entry is clicked off
        #all= triggers all the types above
        #none= disables validation (defalt)

        self.add_sub()

    def add_sub(self):
        #Title
        self.label_T= tk.Label(self, text='Date-Time Calculator', font= ('Arial', 50),  bg= 'blue')
        self.label_T.grid(row= 25, column=32, columnspan=30)

        #format years/months/day - year/month/day
        #left side
        self.label_Y_1= tk.Label(self, text='Y', font=('Arial', 25), bg= 'blue')
        self.label_Y_1.grid(row=49, column=38)

        self.years_1 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd)
        self.years_1.grid(row=50, column=38, padx=10, pady=10, sticky='')

        self.slash = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash.grid(row=50, column=39, padx=10, pady=10, sticky='ew')

        self.label_M_1= tk.Label(self, text='M', font=('Arial', 25), bg= 'blue')
        self.label_M_1.grid(row=49, column=40)

        self.months_1 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black',  validate= 'key', validatecommand= self.validate_cmd)
        self.months_1.grid(row=50, column=40, padx=10, pady=10, sticky='')

        self.slash2 = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash2.grid(row=50, column=41, padx=10, pady=10, sticky='ew')

        self.label_D_1= tk.Label(self, text='D', font=('Arial', 25), bg= 'blue')
        self.label_D_1.grid(row=49, column=42)       

        self.days_1 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black',  validate= 'key', validatecommand= self.validate_cmd_D)
        self.days_1.grid(row=50, column=42, padx=10, pady=10, sticky='')

        #addition sign and change oper button
        style= ttk.Style()
        style.configure('medium.TButton', font= ('Arial', 15))

        self.change2= ttk.Button(self, text= 'Change operator', style= 'medium.TButton', command=self.change_oper)
        self.change2.grid(row=51, column=46)

        self.add= tk.Label(self, text='+', font=('Arial', 50), bg= 'blue')
        self.add.grid(row=50, column=46)

        #right side
        self.label_Y_2= tk.Label(self, text='Y', font=('Arial', 25), bg= 'blue')
        self.label_Y_2.grid(row=49, column=49)

        self.years_2 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd)
        self.years_2.grid(row=50, column=49, padx=10, pady=10, sticky='')

        self.slash3 = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash3.grid(row=50, column=50, padx=10, pady=10, sticky='ew')

        self.label_M_2= tk.Label(self, text='M', font=('Arial', 25), bg= 'blue')
        self.label_M_2.grid(row=49, column=51)

        self.months_2 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd)
        self.months_2.grid(row=50, column=51, padx=10, pady=10, sticky='')

        self.slash4 = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash4.grid(row=50, column=52, padx=10, pady=10, sticky='ew')

        self.label_D_2= tk.Label(self, text='D', font=('Arial', 25), bg= 'blue')
        self.label_D_2.grid(row=49, column=53)       

        self.days_2 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd_D)
        self.days_2.grid(row=50, column=53, padx=10, pady=10, sticky='')

        #calculate
        style= ttk.Style()
        style.configure('big.TButton', font=('Arial', 25))

        self.cal= ttk.Button(self, text='Calculate', style='big.TButton', command= self.add_sub_cal)
        self.cal.grid(row=52, column=46)


    def change_oper(self):
        
        if self.change3 % 2==0:
            self.sub.destroy()
            self.add= tk.Label(self, text='+', font=('Arial', 50), bg= 'blue')
            self.add.grid(row=50, column=46)
            self.change3+=1
        else:
            self.add.destroy()
            self.sub= tk.Label(self, text='−', font=('Arial', 50), bg= 'blue')
            self.sub.grid(row=50, column=46)
            self.change3+=1

    def add_sub_cal(self):
        years_1= int(self.years_1.get())             
        years_2= int(self.years_2.get())
        months_1= int(self.months_1.get())
        months_2= int(self.months_2.get())
        days_1= int(self.days_1.get())
        days_2= int(self.days_2.get())

        time_1= relativedelta(years= years_1, months=months_1, days= days_1)
        time_2= relativedelta(years= years_2, months= months_2, days= days_2)

        change_4= self.change3-1

        if change_4 %2 ==0:
            add_time= time_1 + time_2
            print(add_time)
        
        else:
            sub_time= time_1 - time_2
            print(sub_time)


if __name__ == '__main__':
    main()