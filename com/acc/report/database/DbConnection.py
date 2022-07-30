from logging import root
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector 
from tkinter import ttk


class DbConnection(tk.Tk):

    myDb = mysql.connector.connect(

        host="localhost",
        user = "root",
        password = "linux#",
        database = "edp_report_vision"
    )

#without a buffered cursor, the results are "lazily" loaded
    sqlCursor = myDb.cursor(buffered=True)

    sqlCursor.execute("show databases")

    sqlCursor.execute("SELECT * FROM edp_report")
    print(sqlCursor.description)

    for desc in sqlCursor:
        print(desc.description)


    # for dbNames in sqlCursor:
    #     print(dbNames)

    print(myDb)
    # Database.py ends here

    # sqlCursor.close()
    # myDb.close()