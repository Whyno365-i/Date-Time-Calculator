#from pathlib import Path: Only need if using image in the background
#from PIL import Image, ImageTk: Also only need if using image in the background
import tkinter as tk
from tkinter import ttk
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

        def validate_add_sub(c):
            #c= character

            if c== '':
                return True
            
            for char in c:
                if (not char.isdigit()):
                    return False

            if len(c) == 4:
                return False
            

            return True

        def validate_between_times_M(c):
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

        def validate_between_times_D(c):
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
        
        def validate_between_times_Y(c):
            #c= character

            if c== '':
                return True
            
            for char in c:
                if (not char.isdigit()):
                    return False

            if len(c) == 5:
                return False
            
            return True
        


        self.validate_cmd= ((self.register(validate_add_sub)), '%P')
        self.validate_cmd_M= ((self.register(validate_between_times_M)), '%P')
        self.validate_cmd_D= ((self.register(validate_between_times_D)), '%P')
        self.validate_cmd_Y= ((self.register(validate_between_times_Y)), '%P')


        #TODO make the time calculator with datetime

        #validation types:
        #key= triggers at every click of a button
        #foucus= triggers when you click off or on the entry
        #focusin= only triggers when entry is clicked
        #focusout= only triggers when entry is clicked off
        #all= triggers all the types above
        #none= disables validation (defalt)

        self.home_screen()

    def destroy_method(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    
    def home_screen(self):
        for c in range(100):
            self.columnconfigure(c, weight=1, uniform='cols')

        for r in range(100):
            self.rowconfigure(r, weight=1, uniform= 'rows')

        style= ttk.Style()
        style.configure('home.TButton', font= ('Arial', 20))

        self.add_sub_button= ttk.Button(self, text='Add and Sub Mode', style='home.TButton', command= lambda: (self.destroy_method(self), self.after(50, self.add_sub)))
        self.add_sub_button.grid(row=40, column=25, ipady=50, columnspan=5, rowspan=5)

        self.between_time= ttk.Button(self, text= 'Between Two Time\n          Mode', style='home.TButton', command= lambda: (self.destroy_method(self), self.after(50, self.between_times)))
        self.between_time.grid(row=40, column=75, columnspan=5, rowspan=5, ipady=35)

        self.exit= ttk.Button(self, text= 'Exit', style='home.TButton', command= self.master.destroy)
        self.exit.grid(row=60, column=50, rowspan=5, columnspan=5, ipady=50, ipadx=40)
    
    def between_times(self):
        for c in range(20):
            self.columnconfigure(c, weight=1, uniform='cols')


        for c in range(21, 100):
            self.columnconfigure(c, weight=3, uniform='cols')

        for r in range(100):
            self.rowconfigure(r, weight=1, uniform= 'rows')
        #Title
        self.title= tk.Label(self, text='Date-Time Calculator', font= ('Arial', 50),  bg= 'blue')
        self.title.grid(row= 25, column=25, padx=(100, 0), columnspan=75, rowspan= 15)
        
        #format month/day/year - month/day/year
        #left side

        #TODO make validation
        self.label_M_1= tk.Label(self, text='M', font=('Arial', 25), bg= 'blue')
        self.label_M_1.grid(row=41, column=36, columnspan=10, rowspan=10)

        self.months_1 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black',  validate= 'key', validatecommand= self.validate_cmd_M)
        self.months_1.grid(row=50, column=36, sticky='', columnspan=10, rowspan=10)

        self.slash = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash.grid(row=50, column=44, sticky='', columnspan=3, rowspan=10)

        self.label_D_1= tk.Label(self, text='D', font=('Arial', 25), bg= 'blue')
        self.label_D_1.grid(row=41, column=45, rowspan=10, columnspan=10)       

        self.days_1 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black',  validate= 'key', validatecommand= self.validate_cmd_D)
        self.days_1.grid(row=50, column=45, sticky='', rowspan=10, columnspan=10)

        self.slash2 = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash2.grid(row=50, column=52, sticky='ew', columnspan=3, rowspan=10)

        self.label_Y_1= tk.Label(self, text='Y', font=('Arial', 25), bg= 'blue')
        self.label_Y_1.grid(row=41, column=54, columnspan=10, rowspan=10)

        self.years_1 = tk.Entry(self, font=('Arial', 25), width=4, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd_Y)
        self.years_1.grid(row=50, column=54, sticky='', columnspan=10, rowspan=10)

        #addition sign and change oper button
        style= ttk.Style()
        style.configure('medium.TButton', font= ('Arial', 15))

        self.subtract= tk.Label(self, text='−', font=('Arial', 50), bg= 'blue')
        self.subtract.grid(row=50, column=62, columnspan=10, rowspan=10)

        #right side

        self.label_M_2= tk.Label(self, text='M', font=('Arial', 25), bg= 'blue')
        self.label_M_2.grid(row=41, column=68, columnspan=10, rowspan=10)

        self.months_2 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd_M)
        self.months_2.grid(row=50, column=68, sticky='', columnspan=10, rowspan=10)

        self.slash3 = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash3.grid(row=50, column=76, sticky='ew', columnspan=3, rowspan=10)

        self.label_D_2= tk.Label(self, text='D', font=('Arial', 25), bg= 'blue')
        self.label_D_2.grid(row=41, column=77, columnspan=10, rowspan=10)       

        self.days_2 = tk.Entry(self, font=('Arial', 25), width=2, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd_D)
        self.days_2.grid(row=50, column=77, sticky='', columnspan=10, rowspan=10)

        self.slash4 = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash4.grid(row=50, column=84, sticky='ew', columnspan=3, rowspan=10)

        self.label_Y_2= tk.Label(self, text='Y', font=('Arial', 25), bg= 'blue')
        self.label_Y_2.grid(row=41, column=86, columnspan=10, rowspan=10)

        self.years_2 = tk.Entry(self, font=('Arial', 25), width=4, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd_Y)
        self.years_2.grid(row=50, column=86, sticky='', columnspan=10, rowspan=10)

        #calculate
        style= ttk.Style()
        style.configure('big.TButton', font=('Arial', 25))

        self.cal= ttk.Button(self, text='Calculate', style='big.TButton', command= self.between_times_cal)
        self.cal.grid(row=59, column=58, pady=60, columnspan=17, rowspan=2)

        #output
        self.output1= tk.Label(self, text= '0 years, 0 months, 0 days', font= ('Arial', 20), bg='blue') 
        self.output1.grid(row=60, column=52, columnspan=30, rowspan=5)

        #back button
        self.back= ttk.Button(self, text='back', style='medium.TButton', command= lambda: (self.destroy_method(self),self.after(50, self.home_screen) ))
        self.back.grid(row=100, column= 100)

    def add_sub(self):
        for c in range(100):
            self.columnconfigure(c, weight=1, uniform='cols')

        for r in range(100):
            self.rowconfigure(r, weight=1, uniform= 'rows')
        #Title
        self.label_T= tk.Label(self, text='Date-Time Calculator', font= ('Arial', 50),  bg= 'blue')
        self.label_T.grid(row= 25, column=18, columnspan=75, rowspan= 15)

        #format years/months/day +/- year/month/day
        #left side
        self.label_Y_1= tk.Label(self, text='Y', font=('Arial', 25), bg= 'blue')
        self.label_Y_1.grid(row=41, column=22, columnspan=10, rowspan=10)

        self.years_1 = tk.Entry(self, font=('Arial', 25), width=3, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd)
        self.years_1.grid(row=50, column=22, sticky='', columnspan=10, rowspan=10)

        self.slash = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash.grid(row=50, column=30, sticky='', columnspan=3, rowspan=10)

        self.label_M_1= tk.Label(self, text='M', font=('Arial', 25), bg= 'blue')
        self.label_M_1.grid(row=41, column=31, columnspan=10, rowspan=10)

        self.months_1 = tk.Entry(self, font=('Arial', 25), width=3, highlightthickness= 3, highlightbackground='black', highlightcolor='black',  validate= 'key', validatecommand= self.validate_cmd)
        self.months_1.grid(row=50, column=31, sticky='', columnspan=10, rowspan=10)

        self.slash2 = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash2.grid(row=50, column=39, sticky='ew', columnspan=3, rowspan=10)

        self.label_D_1= tk.Label(self, text='D', font=('Arial', 25), bg= 'blue')
        self.label_D_1.grid(row=41, column=40, rowspan=10, columnspan=10)       

        self.days_1 = tk.Entry(self, font=('Arial', 25), width=3, highlightthickness= 3, highlightbackground='black', highlightcolor='black',  validate= 'key', validatecommand= self.validate_cmd)
        self.days_1.grid(row=50, column=40, sticky='', rowspan=10, columnspan=10)

        #addition sign and change oper button
        style= ttk.Style()
        style.configure('medium.TButton', font= ('Arial', 15))

        self.change2= ttk.Button(self, text= 'Change operator', style= 'medium.TButton', command=self.change_oper)
        self.change2.grid(row=59, column=47, columnspan=17, rowspan=10)

        self.add= tk.Label(self, text='+', font=('Arial', 50), bg= 'blue')
        self.add.grid(row=50, column=50, columnspan=10, rowspan=10)

        #right side
        self.label_Y_2= tk.Label(self, text='Y', font=('Arial', 25), bg= 'blue')
        self.label_Y_2.grid(row=41, column=61, columnspan=10, rowspan=10)

        self.years_2 = tk.Entry(self, font=('Arial', 25), width=3, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd)
        self.years_2.grid(row=50, column=61, sticky='', columnspan=10, rowspan=10)

        self.slash3 = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash3.grid(row=50, column=69, sticky='ew', columnspan=3, rowspan=10)

        self.label_M_2= tk.Label(self, text='M', font=('Arial', 25), bg= 'blue')
        self.label_M_2.grid(row=41, column=70, columnspan=10, rowspan=10)

        self.months_2 = tk.Entry(self, font=('Arial', 25), width=3, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd)
        self.months_2.grid(row=50, column=70, sticky='', columnspan=10, rowspan=10)

        self.slash4 = tk.Label(self, text='/', font=('Arial', 40), fg= 'black', bg= 'blue')
        self.slash4.grid(row=50, column=78, sticky='ew', columnspan=3, rowspan=10)

        self.label_D_2= tk.Label(self, text='D', font=('Arial', 25), bg= 'blue')
        self.label_D_2.grid(row=41, column=79, columnspan=10, rowspan=10)       

        self.days_2 = tk.Entry(self, font=('Arial', 25), width=3, highlightthickness= 3, highlightbackground='black', highlightcolor='black', validate= 'key', validatecommand= self.validate_cmd)
        self.days_2.grid(row=50, column=79, sticky='', columnspan=10, rowspan=10)

        #calculate
        style= ttk.Style()
        style.configure('big.TButton', font=('Arial', 25))


        self.cal= ttk.Button(self, text='Calculate', style='big.TButton', command= self.add_sub_cal)
        self.cal.grid(row=70, column=47, columnspan=17, rowspan=2)

        #output
        self.output1= tk.Label(self, text= '0 years, 0 months, 0 days', font= ('Arial', 20), bg='blue') 
        self.output1.grid(row=77, column=41, columnspan=30, rowspan=5)

        #back button
        self.back= ttk.Button(self, text='back', style='medium.TButton', command= lambda: (self.destroy_method(self),self.after(50, self.home_screen) ))
        self.back.grid(row=100, column= 100, columnspan=20, rowspan=10)

    def between_times_cal(self):

        

        if self.years_1.get() == '' or self.years_2.get() == '' or self.months_1.get() == '' or self.months_2.get() == '' or self.days_1.get() == '' or self.days_2.get() == '':
            error2= tk.Label(self, text= 'please enter numbers in all boxes', font= ('Arial', 20), bg='blue')
            error2.grid(row=65, column=47, columnspan=40, rowspan=2)
            self.after(3000, error2.destroy)
        
        elif int(self.years_1.get())== 0 or int(self.years_2.get())== 0 or int(self.months_1.get())== 0 or int(self.months_2.get())== 0 or int(self.days_1.get())== 0 or int(self.days_2.get())== 0:
            error3= tk.Label(self, text= 'please put a number greater than zero', font= ('Arial', 20), bg='blue')
            error3.grid(row=65, column=30, padx= (100, 0), columnspan=70, rowspan=2)
            self.after(3000, error3.destroy)
        
        else:
            time1= datetime(int(self.years_1.get()),int(self.months_1.get()), int(self.days_1.get()))
            time2= datetime(int(self.years_2.get()),int(self.months_2.get()), int(self.days_2.get()))

            result_year= time1.year - time2.year
            result_month= time1.month -time2.month
            result_day= time1.day - time2.day 

            if result_year < 0 or result_month < 0 or result_day < 0:
                error= tk.Label(self, text= 'time cannot be negative', font= ('Arial', 20), bg='blue')
                error.grid(row=65, column=52, columnspan=30, rowspan=2)
                self.after(3000, error.destroy)
            
            else:
                if self.output1.winfo_exists():
                    self.output1.destroy
                
                if hasattr(self, 'output2') and self.output2 and self.output2.winfo_exists():
                    self.output2.destroy()

                self.output2= tk.Label(self, text= f'{result_year} years, {result_month} months, {result_day} days', font= ('Arial', 20), bg='blue') 
                self.output2.grid(row=60, column=52, columnspan=30, rowspan=5)



    def change_oper(self):
        if self.change3 % 2==0:
            self.sub.destroy()
            self.add= tk.Label(self, text='+', font=('Arial', 50), bg= 'blue')
            self.add.grid(row=50, column=50, columnspan=10, rowspan=10)
            self.change3+=1
        else:
            self.add.destroy()
            self.sub= tk.Label(self, text='−', font=('Arial', 50), bg= 'blue')
            self.sub.grid(row=50, column=50, columnspan=10, rowspan=10)
            self.change3+=1

    def add_sub_cal(self):
        if self.years_1.get() == '':
            years_1= 0
        else:
            years_1= int(self.years_1.get())       

        if self.years_2.get() == '':
            years_2=0
        else:      
            years_2= int(self.years_2.get())
        
        if self.months_1.get() == '':
            months_1= 0
        
        else:
            months_1= int(self.months_1.get())
        
        if self.months_2.get() == '':
            months_2=0

        else:
            months_2= int(self.months_2.get())
        
        if self.days_1.get() == '':
            days_1=0
        
        else:
            days_1= int(self.days_1.get())
        
        if self.days_2.get() == '':
            days_2=0
        
        else:
            days_2= int(self.days_2.get())

        time_1= relativedelta(years= years_1, months=months_1, days= days_1)
        time_2= relativedelta(years= years_2, months= months_2, days= days_2)

        change_4= self.change3-1

        if change_4 % 2 == 0:
            if self.output1.winfo_exists():
                self.output1.destroy()
            
            elif hasattr(self, 'output2') and self.output2 and self.output2.winfo_exists():
                self.output2.destroy()

            else:
                self.output3.destroy()

            add_time= time_1 + time_2
            years= add_time.years
            months= add_time.months
            days= add_time.days

            self.output2= tk.Label(self, text= f'{years} years, {months} months, {days} days', font= ('Arial', 20), bg='blue') 
            self.output2.grid(row=77, column=41, columnspan=30, rowspan=5)      

        else:
            sub_time= time_1 - time_2
            years= sub_time.years
            months= sub_time.months
            days= sub_time.days
            if years < 0 or months < 0 or days < 0:
                error= tk.Label(self, text= 'time cannot be negative', font= ('Arial', 20), bg='blue')
                error.grid(row=90, column=40, columnspan=30, rowspan=2)
                self.after(3000, error.destroy)
            
            else:
                if self.output1.winfo_exists():
                    self.output1.destroy()
                
                elif hasattr(self, 'output3') and self.output3 and self.output3.winfo_exists():
                    self.output3.destroy()
                
                else:
                    self.output2.destroy()

                self.output3= tk.Label(self, text= f'{years} years, {months} months, {days} days', font= ('Arial', 20), bg='blue') 
                self.output3.grid(row=77, column=41, columnspan=30, rowspan=5)    
                


if __name__ == '__main__':
    main()