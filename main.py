from tkinter import *
from tkinter import messagebox as msg
import csv
import tkinter
from tkinter import ttk
import os

os.system("cls")

def main():

    class BimeName():
        pass

    root = Tk()
    root.title("لیست بیمه نامه های خودرو، نمایندگی قلاوند")
    root.iconbitmap("bimehdana.ico")
    root.config(bg = "#355366")
    root.state('zoomed')
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    sec = Frame(main_frame)
    sec.pack(fill=X, side=BOTTOM)
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    x_scrollbar = ttk.Scrollbar(
        sec, orient=HORIZONTAL, command=my_canvas.xview)
    x_scrollbar.pack(side=BOTTOM, fill=X)
    y_scrollbar = ttk.Scrollbar(
        main_frame, orient=VERTICAL, command=my_canvas.yview)
    y_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(xscrollcommand=x_scrollbar.set)
    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.config(
        scrollregion=my_canvas.bbox(ALL)))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    bime_headers = ["ردیف",
    "شماره بیمه نامه",
    "کد رایانه بیمه نامه",
    "شماره پلاک",
    "بیمه گذار",
    "سال ساخت",
    "شماره شاسی",
    "وین",
    "شماره موتور",
    "تاریخ انقضای بیمه نامه",
    "کد ملی بیمه شده",
    "مبلغ توافق بیمه نامه",
    "مبلغ پرداخت شده",
    "تعداد اقساط",
    "تعداد اقساط باقی مانده",
    "مبلغ باقی مانده"]
    
    def new_bime_name(what):
        root.withdraw()
        new_bime_name_page = Toplevel()
        new_bime_name_page.state('zoomed')
        new_bime_name_page.config(bg = "#355366")

        #getting data in a very unefficient way...
        new_shomare_bime_name_label = Label(new_bime_name_page,text = "شماره بیمه نامه", font = "arial 14 bold").grid(row = 0, column = 0,padx=30, pady = 30, sticky = "nsew")
        new_shomare_bime_name = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_shomare_bime_name.grid(row = 1, column = 0, padx=30, pady = 30, sticky = "nsew")

        new_rayane_code_label = Label(new_bime_name_page,text = "کد رایانه", font = "arial 14 bold").grid(row = 0, column = 1,padx=30, pady = 30, sticky = "nsew")
        new_rayane_code = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_rayane_code.grid(row = 1, column = 1, padx=30, pady = 30, sticky = "nsew")

        new_shomare_pelak_label = Label(new_bime_name_page,text = "شماره پلاک", font = "arial 14 bold").grid(row = 0, column = 2,padx=30, pady = 30, sticky = "nsew")
        new_shomare_pelak = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_shomare_pelak.grid(row = 1, column = 2, padx=30, pady = 30, sticky = "nsew")

        new_bimeh_gozar_label = Label(new_bime_name_page,text = "بیمه گذار", font = "arial 14 bold").grid(row = 0, column = 3,padx=30, pady = 30, sticky = "nsew")
        new_bimeh_gozar = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_bimeh_gozar.grid(row = 1, column = 3, padx=30, pady = 30, sticky = "nsew")

        new_sale_sakht_label = Label(new_bime_name_page,text = "سال ساخت", font = "arial 14 bold").grid(row = 0, column =4,padx=30, pady = 30, sticky = "nsew")
        new_sale_sakht = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_sale_sakht.grid(row = 1, column =4, padx=30, pady = 30, sticky = "nsew")

        new_shomare_shasi_label = Label(new_bime_name_page,text = "شماره شاسی", font = "arial 14 bold").grid(row = 0, column = 5,padx=30, pady = 30, sticky = "nsew")
        new_shomare_shasi = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_shomare_shasi.grid(row = 1, column = 5, padx=30, pady = 30, sticky = "nsew")

        new_vin_label = Label(new_bime_name_page,text = "VIN", font = "arial 14 bold").grid(row = 0, column =6,padx=30, pady = 30, sticky = "nsew")
        new_vin = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_vin.grid(row = 1, column =6, padx=30, pady = 30, sticky = "nsew")

        new_shomare_motor_label = Label(new_bime_name_page,text = "شماره موتور", font = "arial 14 bold").grid(row = 0, column = 7,padx=30, pady = 30, sticky = "nsew")
        new_shomare_motor = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_shomare_motor.grid(row = 1, column = 7, padx=30, pady = 30, sticky = "nsew")

        new_tarikh_engheza_label = Label(new_bime_name_page,text = "تاریخ انقضای بیمه نامه", font = "arial 14 bold").grid(row = 2, column = 0,padx=30, pady = 30, sticky = "nsew")
        new_tarikh_engheza = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_tarikh_engheza.grid(row = 3, column = 0, padx=30, pady = 30, sticky = "nsew")

        new_code_meli_label = Label(new_bime_name_page,text = "کد ملی بیمه شده", font = "arial 14 bold").grid(row = 2, column = 1,padx=30, pady = 30, sticky = "nsew")
        new_code_meli = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_code_meli.grid(row = 3, column = 1, padx=30, pady = 30, sticky = "nsew")

        new_mablagh_label = Label(new_bime_name_page,text = "مبلغ بیمه نامه", font = "arial 14 bold").grid(row = 2, column = 2,padx=30, pady = 30, sticky = "nsew")
        new_mablagh = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_mablagh.grid(row = 3, column = 2, padx=30, pady = 30, sticky = "nsew")

        new_number_of_loan_label = Label(new_bime_name_page,text = "تعداد اقساط بیمه نامه", font = "arial 14 bold").grid(row = 2, column = 3,padx=30, pady = 30, sticky = "nsew")
        new_number_of_loan = Entry(new_bime_name_page, justify = CENTER, bd = 0)
        new_number_of_loan.grid(row = 3, column = 3, padx=30, pady = 30, sticky = "nsew")

        #submitting data into database
        def sabt_bime_name():
            if wh == "sales":
                with open("sales_data.csv", "w", newline = "", encoding = "utf-8-sig") as sales_file:
                    new_bime_data = ["",new_shomare_bime_name.get(),new_rayane_code.get(),new_shomare_pelak.get(),new_bimeh_gozar.get(),new_sale_sakht.get(),
                    new_shomare_shasi.get(),new_vin.get(),new_shomare_motor.get(),new_tarikh_engheza.get(),new_code_meli.get(),new_mablagh.get(),
                    "","","",new_number_of_loan.get()]
                    print(new_bime_data)
                    writer = csv.writer(sales_file)

            else:
                pass

        final_btn = Button(new_bime_name_page, text = "تایید و ثبت بیمه نامه", command = sabt_bime_name)
        final_btn.grid(row = 4, column = 0, padx=30, pady = 30, sticky = "nsew")

    def chosen(what):
        root.deiconify()
        root.state('zoomed')
        #getting user choice for what data to present
        global sales_data, badane_data, wh
        wh = what
        my_menu = Menu(root)
        root.config(menu=my_menu, bg = "#355366")
        second_frame.config(bg = "#355366")
        my_menu.add_command(label="ثبت بیمه نامه جدید", command = lambda: new_bime_name("sales"))

        #what if sales is chosen
        if what == "sales":
            with open("sales_data.csv", "r+",newline="", encoding="utf-8-sig") as sales_file:
                sales_reader = csv.reader(sales_file)
                temp = []
                for line in sales_reader:
                    temp.append(line)
                sales_data = temp[1::]
                sales_or_badane_fr.destroy()
        #what if badane is chosen
        elif what == "badane":
            with open("badane_data.csv", "r+",newline="",encoding="utf-8-sig") as badane_file:
                badane_reader = csv.reader(badane_file)
                temp = []
                for line in badane_reader:
                    temp.append(line)
                badane_data = temp[1::]
                sales_or_badane_fr.destroy()

        #actually showing data to user
        
        showLabel = Label(second_frame,text = "لیست بیمه نامه ها", font = "arial 14 bold", bg = "#FBFBFB", fg="#000000")
        showLabel.grid(row = 0, column = 0, sticky = "nsew", padx=10, pady = 50)
        c = 0
        for line in bime_headers:
            a = Label(second_frame,text = line, font = "arial 14 bold", bg = "#FBFBFB", fg="#000000")
            a.grid(row = 1, column = c, sticky = "nsew", padx = 10, pady = 10)
            c += 1

        
        
        
        
            
    #making setup    
    root.withdraw()
    sales_or_badane_fr = Toplevel()
    sales_or_badane_fr.config(bg = "#355366")
    sales_or_badane_fr.title("لطفا نوع بیمه نامه را انتخاب نمایید")
    sales_or_badane_fr.geometry(f"400x100+400+400")
    sales_button = Button(sales_or_badane_fr,text = "بیمه نامه شخص ثالث",font="arial 14", command= lambda: chosen("sales"))
    badane_button = Button(sales_or_badane_fr,text = "بیمه نامه بدنه", font="arial 14", command= lambda : chosen("badane"))
    sales_button.grid(row = 0, column = 0,sticky="nsew")
    badane_button.grid(row = 1, column = 0,sticky="nsew")

    root.mainloop()


main()