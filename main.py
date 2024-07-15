from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('WorldCup 2022 Qatar')
        self.root.config(bg='white')
        self.root.geometry('500x500+0+0')

        self.bg = ImageTk.PhotoImage(file='C:/Users/Devraj/Desktop/junifor.png')
        bg = Label(self.root, image=self.bg).place(x=0, y=0, width=700, height=550)

        frame1 = Frame(self.root, bg='white')
        frame1.place(x=0, y=0, width=700, height=550)

        title = Label(frame1, text='WorldCup 2022 Qatar Teams', font=('times new roman', 20, 'bold'), bg='white',
                      fg='green').place(x=166, y=30)

        select_group = Label(frame1, text='SELECT GROUP', font=('times new roman', 15, 'bold'), bg='white',
                             fg='gray').place(x=50, y=100)
        self.cmb_select_group = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER)
        self.cmb_select_group['values'] = ('Select', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'All Groups')
        self.cmb_select_group.place(x=220, y=100, width=250)
        self.cmb_select_group.current(0)

        submitButton = Button(frame1, command=self.go_function, text='GO', bg='orange', fg='black')
        submitButton.place(x=480, y=100)

    def go_function(self):
        selected_group = self.cmb_select_group.get()
        if selected_group == 'A':
            print('Nepal', 'Japan')
        # Add other conditions for different groups if needed

# Create an instance of the Tkinter window
root = Tk()
obj = Register(root)
root.mainloop()
