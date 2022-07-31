from logging import root
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector 
from tkinter import ttk

class Main:

    program = Tk()

    def selectReports(self):
        messagebox.showinfo("EDP", "All reports")

    def showReports(self):
        messagebox.showinfo("EDP", "Select reports")

    # Report Display Window
    def reviewReport(self):
        win = Toplevel(self.program)
        win.geometry("626x431")

    def Show_Page(self):
        # program = Tk()
        self.program.title("My Tkinter app")
        style = ttk.Style()
        style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
        self.program.geometry("626x431")
        monitor = ttk.Button(name="",text="Monitor",command=self.reviewReport,style="C.TButton")
        monitor.pack(pady=100)
        review = ttk.Button(name="",text="Review",command=self.selectReports,style="C.TButton")
        review.pack(pady=0)
        self.program.mainloop()
    
# Main method 
if __name__ == "__main__":
    objectMain = Main()
    objectMain.Show_Page()
