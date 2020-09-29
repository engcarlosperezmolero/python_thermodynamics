from tkinter import *
from tkinter import ttk
import pandas as pd
import sqlite3

ctea = pd.read_csv("ctteanto.csv")
ctpp = pd.read_csv("PureProperties.csv")
ctes = ctea.merge(ctpp)

names = ctes["Nombre"].tolist()
names.insert(0, "Select a component")


def cuadro(parent, r, c, rs):
    label = Label(parent, font=24)
    label.config(bg="dark slate gray", fg="white", width=20, height=5, bd="2", relief="solid", justify=LEFT)
    label.grid(row=r, column=c, rowspan=rs, ipadx=2)


def combof1(parent, r, c):
    """Establece que sucede en la interfaz cada vez que sucede el evento de
       seleccionar un nuevo componente de el Combobox."""
    # conn = sqlite3.connect("combo_book.db")
    # c = conn.cursor()
    # c.execute("""CREATE TABLE pureproperties1 (
    #     A real,
    #     B real,
    #     C real,
    #     RTC real,
    #     W real,
    #     TC real,
    #     PC real,
    #     ZC real,
    #     VC real
    #     )""")
    # conn.commit()
    # conn.close()

    def imprime(event):

        if combobo.get() != "Select a component":
            compo_1 = ctes[ctes["Nombre"] == combobo.get()]
            conn = sqlite3.connect("combo_book.db")
            cu1 = conn.cursor()

            for recordd in range(20):
                    cu1.execute("DELETE from pureproperties1 WHERE oid = " + str(recordd))

            cu1.execute("INSERT INTO pureproperties1 VALUES (:A1, :B1, :C1, :RTC1, :W1, :TC1, :PC1, :ZC1, :VC1)",
                        {
                            'A1': compo_1.iloc[0, 1],
                            'B1': compo_1.iloc[0, 2],
                            'C1': compo_1.iloc[0, 3],
                            'RTC1': compo_1.iloc[0, 4],
                            'W1': compo_1.iloc[0, 5],
                            'TC1': compo_1.iloc[0, 6],
                            'PC1': compo_1.iloc[0, 7],
                            'ZC1': compo_1.iloc[0, 8],
                            'VC1': compo_1.iloc[0, 9]
                        })

            cu1.execute("SELECT *, oid FROM pureproperties1")
            records = cu1.fetchall()
            print(records)

            #  PRINT RECORDS WILL HAVE TO CHANGE TO THE OUTPUT OF THE PROPERTY FUNCTION ANDA THAT
            print_records = ""
            for record in records:
                A1 = record[0]
                B1 = record[1]
                C1 = record[2]
                RTC1 = record[3]
                W1 = record[4]
                TC1 = record[5]
                PC1 = record[6]
                ZC1 = record[7]
                VC1 = record[8]

            conn.commit()
            conn.close()

            a = "A= "+str(A1)+"\nB= "+str(B1)+"\nC= "+str(C1)+"\nTemperature Range\n(Celsius)= "+str(RTC1)
            b = "w= "+str("{:.3f}".format(W1))+"\nTemp. crit. (K)= "+str(TC1)+"\nP. crit.(bar)= "+str(PC1)+"\nZc= "+str("{:.3f}".format(ZC1))+"\nVol. crit.(cc/mol)="+str(VC1)

            label = Label(parent, text=a, font=24, anchor="nw")
            label.config(bg="dark slate gray", fg="white", width=20, height=5, bd="2", relief="solid", justify=LEFT)
            label.grid(row=r+3, column=c, ipadx=2)

            label = Label(parent, text=b, font=24, anchor="nw")
            label.config(bg="dark slate gray", fg="white", width=20, height=5, bd="2", relief="solid", justify=LEFT)
            label.grid(row=r+6, column=c, ipadx=2)
        else:
            label = Label(parent, font=24, anchor="nw")
            label.config(bg="dark slate gray", fg="white", width=20, height=5, bd="2", relief="solid", justify=LEFT)
            label.grid(row=r+3, column=c, ipadx=2)

            label = Label(parent, font=24, anchor="nw")
            label.config(bg="dark slate gray", fg="white", width=20, height=5, bd="2", relief="solid", justify=LEFT)
            label.grid(row=r+6, column=c, ipadx=2)

    combobo = ttk.Combobox(parent, values=names, state="readonly")
    combobo.current(0)
    combobo.bind("<<ComboboxSelected>>", imprime)
    combobo.grid(row=r, column=c, sticky=W+E)


def combof2(parent, r, c):
    """Establece que sucede en la interfaz cada vez que sucede el evento de
       seleccionar un nuevo componente de el Combobox."""
    # conn = sqlite3.connect("combo_book.db")
    # c = conn.cursor()
    # c.execute("""CREATE TABLE pureproperties2 (
    #     A real,
    #     B real,
    #     C real,
    #     RTC real,
    #     W real,
    #     TC real,
    #     PC real,
    #     ZC real,
    #     VC real
    #     )""")
    # conn.commit()
    # conn.close()

    def imprime(event):

        if combobo.get() != "Select a component":
            compo_1 = ctes[ctes["Nombre"] == combobo.get()]
            conn2 = sqlite3.connect("combo_book.db")
            cu1 = conn2.cursor()

            for recordd in range(20):
                cu1.execute("DELETE from pureproperties2 WHERE oid = " + str(recordd))

            cu1.execute("INSERT INTO pureproperties2 VALUES (:A2, :B2, :C2, :RTC2, :W2, :TC2, :PC2, :ZC2, :VC2)",
                        {
                            'A2': compo_1.iloc[0, 1],
                            'B2': compo_1.iloc[0, 2],
                            'C2': compo_1.iloc[0, 3],
                            'RTC2': compo_1.iloc[0, 4],
                            'W2': compo_1.iloc[0, 5],
                            'TC2': compo_1.iloc[0, 6],
                            'PC2': compo_1.iloc[0, 7],
                            'ZC2': compo_1.iloc[0, 8],
                            'VC2': compo_1.iloc[0, 9]
                        })

            cu1.execute("SELECT *, oid FROM pureproperties2")
            records2 = cu1.fetchall()
            print(records2)
            #  PRINT RECORDS WILL HAVE TO CHANGE TO THE OUTPUT OF THE PROPERTY FUNCTION ANDA THAT
            print_records2 = ""
            for record in records2:
                A2 = record[0]
                B2 = record[1]
                C2 = record[2]
                RTC2 = record[3]
                W2 = record[4]
                TC2 = record[5]
                PC2 = record[6]
                ZC2 = record[7]
                VC2 = record[8]

            conn2.commit()
            conn2.close()

            a = "A= "+str(A2)+"\nB= "+str(B2)+"\nC= "+str(C2)+"\nTemperature Range\n(Celsius)= "+str(RTC2)
            b = "w= "+str("{:.3f}".format(W2))+"\nTemp. crit. (K)= "+str(TC2)+"\nP. crit.(bar)= "+str(PC2)+"\nZc= "+str("{:.3f}".format(ZC2))+"\nVol. crit.(cc/mol)="+str(VC2)

            label = Label(parent, text=a, font=24, anchor="nw")
            label.config(bg="dark slate gray", fg="white", width=20, height=5, bd="2", relief="solid", justify=LEFT)
            label.grid(row=r+3, column=c, ipadx=2)

            label = Label(parent, text=b, font=24, anchor="nw")
            label.config(bg="dark slate gray", fg="white", width=20, height=5, bd="2", relief="solid", justify=LEFT)
            label.grid(row=r+6, column=c, ipadx=2)
        else:
            label = Label(parent, font=24, anchor="nw")
            label.config(bg="dark slate gray", fg="white", width=20, height=5, bd="2", relief="solid", justify=LEFT)
            label.grid(row=r+3, column=c, ipadx=2)

            label = Label(parent, font=24, anchor="nw")
            label.config(bg="dark slate gray", fg="white", width=20, height=5, bd="2", relief="solid", justify=LEFT)
            label.grid(row=r+6, column=c, ipadx=2)

    combobo = ttk.Combobox(parent, values=names, state="readonly")
    combobo.current(0)
    combobo.bind("<<ComboboxSelected>>", imprime)
    combobo.grid(row=r, column=c, sticky=W+E)
