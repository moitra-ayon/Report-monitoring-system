from logging import root
from tkinter import *
import tkinter as tk
from tkinter import messagebox
#import mysql.connector 
from tkinter import ttk
# from com.acc.report.database import

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("626x431")
       
        style = ttk.Style()
        style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
        monitor = ttk.Button(name="",text="Monitor",command=self.showReports,style="C.TButton")
        review = ttk.Button(name="",text="Review",command=self.selectReports,style="C.TButton")
        monitor.pack(pady=100)
        review.pack(pady=0)
    

    def selectReports(self):
        messagebox.showinfo("EDP", "All reports")


    def showReports(self):
        messagebox.showinfo("EDP", "Select reports")


# Main method 
if __name__ == "__main__":
    objectMain = Main()
    # objectMain.withdraw()
    objectMain.mainloop()