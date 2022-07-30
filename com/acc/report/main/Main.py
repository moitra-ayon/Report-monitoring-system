from logging import root
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector 
from tkinter import ttk

class Main:

    style = ttk.Style()
    style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

    def selectReports(self):
        messagebox.showinfo("EDP", "All reports")

    def showReports(self):
        messagebox.showinfo("EDP", "Select reports")

    #Report Display Window
    # def reviewReport():
    #     win = Toplevel(root)
    #     win.geometry("626x431")

    def Show_Page(self):
        program = tk.Tk()
        program.title("My Tkinter app")
        program.geometry("626x431")
        monitor = ttk.Button(name="",text="Monitor",command=self.showReports,style="C.TButton")
        monitor.pack(pady=100)
        review = ttk.Button(name="",text="Review",command=self.selectReports,style="C.TButton")
        review.pack(pady=0)
        program.mainloop()
    
# Main method 
if __name__ == "__main__":
    objectMain = Main()
    objectMain.Show_Page()











# setting tkinter window size
# root.geometry("%dx%d" % (width, height))
# root.attributes('-fullscreen',True)
# monitor = Button(root, text="Monitor", command=showReports, padx=50)
# review = Button(root, text="Review", command=reviewReport, padx=54)
# btn = ttk.Button(text="Sample")
# btn.pack()
# CREATE TABLE `edp_report_vision`.`edp_report` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `report` VARCHAR(256) NULL,
#   `reviewer` VARCHAR(45) NOT NULL,
#   `status` VARCHAR(12) BINARY NULL,
#   `remarks` VARCHAR(512) NULL,
#   `date` DATE NULL,
#   `approved` VARCHAR(12) BINARY NULL,
#   PRIMARY KEY (`id`));