"""Creating a data base with SQLITE3 that record all of the entrie's information and that the program will use later."""

from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# This class creates a window that calculates DEWP, DEWT, BULBP, BULPT (master, m1, m2,title); m1 and m2 are strings


class Window1:

    def __init__(self, master, m1, m2, title):
        self.master = master
        self.frame = Toplevel(self.master, width=1400, height=1800)
        self.frame.geometry("+800+50")
        self.frame.config(bg="#404040")
        self.frame.resizable(0, 0)
        self.frame.title(title)
        self.labels = [m1, m2, "Lambda12: ", "Lambda21: ", "Tolerance: ", "Results: "]

        for i in range(len(self.labels)):
            if i != len(self.labels)-1:
                self.label = Label(self.frame, text=self.labels[i], bg="#404040", fg="#FFFFFF", font=("Arial", 12))
                self.label.grid(row=i, column=0, columnspan=2, pady=(10, 1), padx=(10, 1), sticky=E)
            else:
                self.space = Label(self.frame, text="    ", bg="#404040").grid(row=i, column=1, columnspan=2)
                self.label = Label(self.frame, text=self.labels[i], bg="#404040", fg="#FFFFFF", font=("Arial", 12))
                self.label.grid(row=i+1, column=0, columnspan=2, pady=(2, 0), padx=(8, 1), sticky=W)

                self.p1 = Entry(self.frame, width=20)
                self.p1.grid(row=0, column=2, columnspan=1, pady=(10, 1), sticky=W)
                self.p2 = Entry(self.frame, width=20)
                self.p2.grid(row=1, column=2, columnspan=1, pady=(10, 1), sticky=W)
                self.lambda12 = Entry(self.frame, width=20)
                self.lambda12.grid(row=2, column=2, columnspan=1, pady=(10, 1), sticky=W)
                self.lambda21 = Entry(self.frame, width=20)
                self.lambda21.grid(row=3, column=2, columnspan=1, pady=(10, 1), sticky=W)
                self.tolerance = Entry(self.frame, width=20)
                self.tolerance.grid(row=4, column=2, columnspan=1, pady=(10, 1), sticky=W)

                self.calculate_button = Button(self.frame, text="Calculate", command=self.calculate, width=10, fg="#CCC9DC", bg="#324A5F", cursor="hand2")
                self.calculate_button.grid(row=1, column=3, columnspan=1, padx=10, sticky=E)
                self.deleting_button = Button(self.frame, text="Delete", command=self.deleting, width=10, fg="#CCC9DC", bg="#324A5F", cursor="hand2")
                self.deleting_button.grid(row=2, column=3, columnspan=1, padx=10, sticky=E)

                self.results = Label(self.frame, text="", font=24, anchor="nw")
                self.results.config(bg="dark slate gray", fg="white", width=42, height=20, bd="2", relief="solid", justify=LEFT)
                self.results.grid(row=7, column=1, columnspan=3, rowspan=1, ipadx=2, pady=5, padx=10)

                self.returning_button = Button(self.frame, text="Return to main", command=self.returning, width=15, fg="#CCC9DC", bg="#324A5F", cursor="hand2")
                self.returning_button.grid(row=8, column=3, columnspan=1, pady=10, sticky=E, padx=10)
                messagebox.showinfo("IMPORTANT", "In order to ensure the reliability of the results\npress ALWAYS Delete button before entering\nnew data")
        # Create a database or connect to one
        # self.conn = sqlite3.connect("entries_book.db")
        # self.c = self.conn.cursor()
        # self.c.execute("""CREATE TABLE entries (
        # m1 real,
        # m2 real,
        # lambda12 real,
        # lamba21 real,
        # tolerance real
        # )""")
        # self.conn.commit()
        # self.conn.close()

    def propertycalc(self):
        try:
            if (isinstance(float(self.p1.get()), float) or isinstance(float(self.p2.get()), float) or
                    self.lisinstance(float(lambda12.get()), float) or self.lisinstance(float(lambda21.get()), float) or self.toisinstance(float(tolerance.get()), float)):
                self.totalll = (self.prop1 + self.prop2 + self.lam1) / (self.lam2 + self.toler)
                print(self.prop1, self.prop2, self.lam1, self.lam2, self.toler, "\n", self.totalll, "\n", self.A1,
                      self.B1, self.C1, self.RTC1, self.W1, self.TC1, self.PC1, self.ZC1, self.VC1, "\n", self.A2,
                      self.B2, self.C2, self.RTC2, self.W2, self.TC2, self.PC2, self.ZC2, self.VC2)
        except (TypeError):
            messagebox.showerror("Wrong data", "Please enter numbers only, and use decimal point 0.00000")
        except ValueError:
            messagebox.showinfo("Warning", "The data would not be stored until all the entries are correct")

    def calculate(self):

        self.conn2 = sqlite3.connect("combo_book.db")
        self.cu1 = self.conn2.cursor()

        self.conn = sqlite3.connect("entries_book.db")
        self.c = self.conn.cursor()
        try:
            if (isinstance(float(self.p1.get()), float) or isinstance(float(self.p2.get()), float) or
                    self.lisinstance(float(lambda12.get()), float) or self.lisinstance(float(lambda21.get()), float) or self.toisinstance(float(tolerance.get()), float)):
                self.c.execute("INSERT INTO entries VALUES (:p1, :p2, :lambda12, :lambda21, :tolerance)",
                               {
                                   'p1': self.p1.get(),
                                   'p2': self.p2.get(),
                                   'lambda12': self.lambda12.get(),
                                   'lambda21': self.lambda21.get(),
                                   'tolerance': self.tolerance.get()
                               })
        except Exception:
            messagebox.showerror("Wrong data", "Please enter numbers only, and use decimal point 0.00000")
        self.c.execute("SELECT *, oid FROM entries")
        self.records = self.c.fetchall()
        #  PRINT RECORDS WILL HAVE TO CHANGE TO THE OUTPUT OF THE PROPERTY FUNCTION ANDA THAT
        print_records = ""
        for record in self.records:
            self.prop1 = record[0]
            self.prop2 = record[1]
            self.lam1 = record[2]
            self.lam2 = record[3]
            self.toler = record[4]
            print_records += str(record[0]) + "\n" + str(record[1]) + "\n" + str(record[2]) + "\n" + str(record[3]) + "\n" + str(record[4]) + "\n"

        self.cu1.execute("SELECT *, oid FROM pureproperties1")
        self.recordsprop = self.cu1.fetchall()
        for record in self.recordsprop:
            self.A1 = record[0]
            self.B1 = record[1]
            self.C1 = record[2]
            self.RTC1 = record[3]
            self.W1 = record[4]
            self.TC1 = record[5]
            self.PC1 = record[6]
            self.ZC1 = record[7]
            self.VC1 = record[8]

        self.cu1.execute("SELECT *, oid FROM pureproperties2")
        self.recordsprop2 = self.cu1.fetchall()
        for record in self.recordsprop2:
            self.A2 = record[0]
            self.B2 = record[1]
            self.C2 = record[2]
            self.RTC2 = record[3]
            self.W2 = record[4]
            self.TC2 = record[5]
            self.PC2 = record[6]
            self.ZC2 = record[7]
            self.VC2 = record[8]

        # THE MATHEMICAL OPERATION BELLOW WOULD REPRESENT THE FUNCTION THAT COMPUTES THE PROPERTY THAT THE USER WANTS(DEWP, DEWT,BULBP,BULBT,FLASH)
        self.propertycalc()

        self.results1 = Label(self.frame, text=print_records, font=24, anchor="nw")
        self.results1.config(bg="dark slate gray", fg="white", width=42, height=20, bd="2", relief="solid", justify=LEFT)
        self.results1.grid(row=7, column=1, columnspan=3, rowspan=1, ipadx=2, pady=5, padx=10)

        self.conn.commit()
        self.conn.close()
        self.conn2.commit()
        self.conn2.close()

    def deleting(self):
        # Clearing the values of the data base and the entries.
        self.conn = sqlite3.connect("entries_book.db")
        self.c = self.conn.cursor()
        for recordd in range(20):
            self.c.execute("DELETE from entries WHERE oid = " + str(recordd))
        self.conn.commit()
        self.conn.close()
        self.p1.delete(0, END)
        self.p2.delete(0, END)
        self.lambda12.delete(0, END)
        self.lambda21.delete(0, END)
        self.tolerance.delete(0, END)
        self.results = Label(self.frame, text="", font=24, anchor="nw")
        self.results.config(bg="dark slate gray", fg="white", width=42, height=20, bd="2", relief="solid", justify=LEFT)
        self.results.grid(row=7, column=1, columnspan=3, rowspan=1, ipadx=2, pady=5, padx=10)

    def returning(self):
        self.deleting()
        self.frame.destroy()


# This class creates a window that calculates FLASH CALCULATIONS (master,m1,m2,m3,title); m1, m2 and m3 are strings
class Windowflash:

    def __init__(self, master, m1, m2, m3, title):
        self.master = master
        self.frame = Toplevel(self.master, width=1400, height=1800)
        self.frame.geometry("+800+50")
        self.frame.config(bg="#404040")
        self.frame.resizable(0, 0)
        self.frame.title(title)
        self.labels = [m1, m2, m3, "Lambda12: ", "Lambda21: ", "Tolerance: ", "Results: "]

        for i in range(len(self.labels)):
            if i != len(self.labels)-1:
                self.label = Label(self.frame, text=self.labels[i], bg="#404040", fg="#FFFFFF", font=("Arial", 12))
                self.label.grid(row=i, column=0, columnspan=2, pady=(10, 1), padx=(10, 1), sticky=E)
            else:
                self.space = Label(self.frame, text="    ", bg="#404040").grid(row=i, column=1, columnspan=2)
                self.label = Label(self.frame, text=self.labels[i], bg="#404040", fg="#FFFFFF", font=("Arial", 12))
                self.label.grid(row=i+1, column=0, columnspan=2, pady=(2, 0), padx=(8, 1), sticky=W)

                self.p1 = Entry(self.frame, width=20)
                self.p1.grid(row=0, column=2, columnspan=1, pady=(10, 1), sticky=W)
                self.p2 = Entry(self.frame, width=20)
                self.p2.grid(row=1, column=2, columnspan=1, pady=(10, 1), sticky=W)
                self.p3 = Entry(self.frame, width=20)
                self.p3.grid(row=2, column=2, columnspan=1, pady=(10, 1), sticky=W)
                self.lambda12 = Entry(self.frame, width=20)
                self.lambda12.grid(row=3, column=2, columnspan=1, pady=(10, 1), sticky=W)
                self.lambda21 = Entry(self.frame, width=20)
                self.lambda21.grid(row=4, column=2, columnspan=1, pady=(10, 1), sticky=W)
                self.tolerance = Entry(self.frame, width=20)
                self.tolerance.grid(row=5, column=2, columnspan=1, pady=(10, 1), sticky=W)

                self.calculate_button = Button(self.frame, text="Calculate", command=self.calculate, width=10, fg="#CCC9DC", bg="#324A5F", cursor="hand2")
                self.calculate_button.grid(row=1, column=3, columnspan=1, padx=10, sticky=E)
                self.deleting_button = Button(self.frame, text="Delete", command=self.deleting, width=10, fg="#CCC9DC", bg="#324A5F", cursor="hand2")
                self.deleting_button.grid(row=2, column=3, columnspan=1, padx=10, sticky=E)

                self.results = Label(self.frame, text="", font=24, anchor="nw")
                self.results.config(bg="dark slate gray", fg="white", width=42, height=20, bd="2", relief="solid", justify=LEFT)
                self.results.grid(row=8, column=1, columnspan=3, rowspan=1, ipadx=2, pady=5, padx=10)

                self.returning_button = Button(self.frame, text="Return to main", command=self.returning, width=15, fg="#CCC9DC", bg="#324A5F", cursor="hand2")
                self.returning_button.grid(row=9, column=3, columnspan=1, pady=10, sticky=E, padx=10)
                messagebox.showinfo("IMPORTANT", "In order to ensure the reliability of the results\npress ALWAYS Delete button before entering\nnew data")

        # Create a database or connect to one
        # self.conn = sqlite3.connect("entries_flash.db")
        # self.c = self.conn.cursor()
        # self.c.execute("""CREATE TABLE entriesflash (
        # m1 real,
        # m2 real,
        # m3 real,
        # lambda12 real,
        # lamba21 real,
        # tolerance real
        # )""")
        # self.conn.commit()
        # self.conn.close()

    def flashcalc(self):
        try:
            if (isinstance(float(self.p1.get()), float) or isinstance(float(self.p2.get()), float) or isinstance(float(self.p3.get()), float) or
                    self.lisinstance(float(lambda12.get()), float) or self.lisinstance(float(lambda21.get()), float) or self.toisinstance(float(tolerance.get()), float)):
                self.totalll = (self.prop1 + self.prop2 + self.lam1) / (self.lam2 + self.toler)
                print(self.prop1, self.prop2, self.lam1, self.lam2, self.toler, "\n", self.totalll, "\n", self.A1,
                      self.B1, self.C1, self.RTC1, self.W1, self.TC1, self.PC1, self.ZC1, self.VC1, "\n", self.A2,
                      self.B2, self.C2, self.RTC2, self.W2, self.TC2, self.PC2, self.ZC2, self.VC2)
        except (TypeError):
            messagebox.showerror("Wrong data", "Please enter numbers only, and use decimal point 0.00000")
        except ValueError:
            messagebox.showinfo("Warning", "The data would not be stored until all the entries are correct")

    def calculate(self):
        self.conn2 = sqlite3.connect("combo_book.db")
        self.cu1 = self.conn2.cursor()
        self.conn = sqlite3.connect("entries_flash.db")
        self.c = self.conn.cursor()
        try:
            if (isinstance(float(self.p1.get()), float) or isinstance(float(self.p2.get()), float) or isinstance(float(self.p3.get()), float) or
                    self.lisinstance(float(lambda12.get()), float) or self.lisinstance(float(lambda21.get()), float) or self.toisinstance(float(tolerance.get()), float)):
                self.c.execute("INSERT INTO entriesflash VALUES (:p1, :p2, :p3, :lambda12, :lambda21, :tolerance)",
                               {
                                   'p1': self.p1.get(),
                                   'p2': self.p2.get(),
                                   'p3': self.p3.get(),
                                   'lambda12': self.lambda12.get(),
                                   'lambda21': self.lambda21.get(),
                                   'tolerance': self.tolerance.get()
                               })
        except Exception:
            messagebox.showerror("Wrong data", "Please enter numbers only, and use decimal point 0.00000")

        self.c.execute("SELECT *, oid FROM entriesflash")
        self.records = self.c.fetchall()
        #  PRINT RECORDS WILL HAVE TO CHANGE TO THE OUTPUT OF THE PROPERTY FUNCTION ANDA THAT
        print_records = ""
        for record in self.records:
            self.prop1 = record[0]
            self.prop2 = record[1]
            self.prop3 = record[2]
            self.lam1 = record[3]
            self.lam2 = record[4]
            self.toler = record[5]
            print_records += str(record[0]) + "\n" + str(record[1]) + "\n" + str(record[2]) + "\n" + str(record[3]) + "\n" + str(record[4]) + "\n" + str(record[5]) + "\n"

        self.cu1.execute("SELECT *, oid FROM pureproperties1")
        self.recordsprop = self.cu1.fetchall()
        for record in self.recordsprop:
            self.A1 = record[0]
            self.B1 = record[1]
            self.C1 = record[2]
            self.RTC1 = record[3]
            self.W1 = record[4]
            self.TC1 = record[5]
            self.PC1 = record[6]
            self.ZC1 = record[7]
            self.VC1 = record[8]

        self.cu1.execute("SELECT *, oid FROM pureproperties2")
        self.recordsprop2 = self.cu1.fetchall()
        for record in self.recordsprop2:
            self.A2 = record[0]
            self.B2 = record[1]
            self.C2 = record[2]
            self.RTC2 = record[3]
            self.W2 = record[4]
            self.TC2 = record[5]
            self.PC2 = record[6]
            self.ZC2 = record[7]
            self.VC2 = record[8]

        # THE MATHEMICAL OPERATION BELLOW WOULD REPRESENT THE FUNCTION THAT COMPUTES THE PROPERTY THAT THE USER WANTS(DEWP, DEWT,BULBP,BULBT,FLASH)
        self.flashcalc()

        self.results1 = Label(self.frame, text=print_records, font=24, anchor="nw")
        self.results1.config(bg="dark slate gray", fg="white", width=42, height=20, bd="2", relief="solid", justify=LEFT)
        self.results1.grid(row=8, column=1, columnspan=3, rowspan=1, ipadx=2, pady=5, padx=10)

        self.conn.commit()
        self.conn.close()
        self.conn2.commit()
        self.conn2.close()

    def deleting(self):
        # Clearing the values of the data base and the entries.
        self.conn = sqlite3.connect("entries_flash.db")
        self.c = self.conn.cursor()
        for recordd in range(20):
            self.c.execute("DELETE from entriesflash WHERE oid = " + str(recordd))
        self.conn.commit()
        self.conn.close()
        self.p1.delete(0, END)
        self.p2.delete(0, END)
        self.p3.delete(0, END)
        self.lambda12.delete(0, END)
        self.lambda21.delete(0, END)
        self.tolerance.delete(0, END)
        self.results = Label(self.frame, text="", font=24, anchor="nw")
        self.results.config(bg="dark slate gray", fg="white", width=42, height=20, bd="2", relief="solid", justify=LEFT)
        self.results.grid(row=8, column=1, columnspan=3, rowspan=1, ipadx=2, pady=5, padx=10)

    def returning(self):
        self.deleting()
        self.frame.destroy()


class Windowbulbp(Window1):
    def propertycalc(self):
        try:
            if (isinstance(float(self.p1.get()), float) or isinstance(float(self.p2.get()), float) or
                    self.lisinstance(float(lambda12.get()), float) or self.lisinstance(float(lambda21.get()), float) or self.toisinstance(float(tolerance.get()), float)):
                self.totalll = (self.prop1 + self.prop2 + self.lam1) / (self.lam2 + self.toler)
                print(self.prop1, self.prop2, self.lam1, self.lam2, self.toler, "\n", self.totalll, "\n", self.A1,
                      self.B1, self.C1, self.RTC1, self.W1, self.TC1, self.PC1, self.ZC1, self.VC1, "\n", self.A2,
                      self.B2, self.C2, self.RTC2, self.W2, self.TC2, self.PC2, self.ZC2, self.VC2)
        except (TypeError):
            messagebox.showerror("Wrong data", "Please enter numbers only, and use decimal point 0.00000")
        except ValueError:
            messagebox.showinfo("Warning", "The data would not be stored until all the entries are correct")


class Windowdewp(Window1):
    def propertycalc(self):
        try:
            if (isinstance(float(self.p1.get()), float) or isinstance(float(self.p2.get()), float) or
                    self.lisinstance(float(lambda12.get()), float) or self.lisinstance(float(lambda21.get()), float) or self.toisinstance(float(tolerance.get()), float)):
                self.totalll = (self.prop1 + self.prop2 + self.lam1) / (self.lam2 + self.toler)
                print(self.prop1, self.prop2, self.lam1, self.lam2, self.toler, "\n", self.totalll, "\n", self.A1,
                      self.B1, self.C1, self.RTC1, self.W1, self.TC1, self.PC1, self.ZC1, self.VC1, "\n", self.A2,
                      self.B2, self.C2, self.RTC2, self.W2, self.TC2, self.PC2, self.ZC2, self.VC2)
        except (TypeError):
            messagebox.showerror("Wrong data", "Please enter numbers only, and use decimal point 0.00000")
        except ValueError:
            messagebox.showinfo("Warning", "The data would not be stored until all the entries are correct")


class Windowbulbt(Window1):
    def propertycalc(self):
        try:
            if (isinstance(float(self.p1.get()), float) or isinstance(float(self.p2.get()), float) or
                    self.lisinstance(float(lambda12.get()), float) or self.lisinstance(float(lambda21.get()), float) or self.toisinstance(float(tolerance.get()), float)):
                self.totalll = (self.prop1 + self.prop2 + self.lam1) / (self.lam2 + self.toler)
                print(self.prop1, self.prop2, self.lam1, self.lam2, self.toler, "\n", self.totalll, "\n", self.A1,
                      self.B1, self.C1, self.RTC1, self.W1, self.TC1, self.PC1, self.ZC1, self.VC1, "\n", self.A2,
                      self.B2, self.C2, self.RTC2, self.W2, self.TC2, self.PC2, self.ZC2, self.VC2)
        except (TypeError):
            messagebox.showerror("Wrong data", "Please enter numbers only, and use decimal point 0.00000")
        except ValueError:
            messagebox.showinfo("Warning", "The data would not be stored until all the entries are correct")


class Windowdewt(Window1):
    def propertycalc(self):
        try:
            if (isinstance(float(self.p1.get()), float) or isinstance(float(self.p2.get()), float) or
                    self.lisinstance(float(lambda12.get()), float) or self.lisinstance(float(lambda21.get()), float) or self.toisinstance(float(tolerance.get()), float)):
                self.totalll = (self.prop1 + self.prop2 + self.lam1) / (self.lam2 + self.toler)
                print(self.prop1, self.prop2, self.lam1, self.lam2, self.toler, "\n", self.totalll, "\n", self.A1,
                      self.B1, self.C1, self.RTC1, self.W1, self.TC1, self.PC1, self.ZC1, self.VC1, "\n", self.A2,
                      self.B2, self.C2, self.RTC2, self.W2, self.TC2, self.PC2, self.ZC2, self.VC2)
        except (TypeError):
            messagebox.showerror("Wrong data", "Please enter numbers only, and use decimal point 0.00000")
        except ValueError:
            messagebox.showinfo("Warning", "The data would not be stored until all the entries are correct")


# root = Tk()
# root.resizable(0, 0)
# # app = Window1(root, "P1:", "x1:", "Test Property")
# app1 = Windowflash(root, "P1:", "x1:", "z1", "flash")
# root.mainloop()
