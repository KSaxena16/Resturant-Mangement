from tkinter import *
import time
import random
import datetime

#creating main window
m = Tk()
m.geometry("1600x8000")  #Size of the main window
m.title("Resturant Management System")

frame1 = Frame(m, width=1600, relief=SUNKEN)
frame1.pack(side=TOP)

frame2 = Frame(m, height=700, width=800, relief=SUNKEN)
frame2.pack(side=LEFT)

heading_lbl = Label(frame1, text="TEQUILA MOCKINGBIRD", font=('Lato light', 50, 'bold'), fg='blue')
heading_lbl.grid(row=0,column=0)

localtime = time.asctime()

#shows the time
time_lbl = Label(frame1, text=localtime, font=('Helvitica', 30,'bold'), fg='green')
time_lbl.grid(row=1, column=0)

rand = StringVar()
fries = StringVar()
lunch = StringVar()
burger = StringVar()
pizza = StringVar()
cheese = StringVar()
drink = StringVar()
cost = StringVar()
service = StringVar()
tax = StringVar()
subtotal = StringVar()
total = StringVar()

#labels followed by entries
lbl_order = Label(frame2, text="Order No.  ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_order.grid(row=0, column=0)
order_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=rand)
order_entry.grid(row=0, column=1)

lbl_fries = Label(frame2, text="Fries ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_fries.grid(row=1, column=0)
fries_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=fries)
fries_entry.grid(row=1, column=1)

lbl_lunch = Label(frame2, text="Lunch ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_lunch.grid(row=2, column=0)
lunch_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=lunch)
lunch_entry.grid(row=2, column=1)

lbl_burger = Label(frame2, text="Burger ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_burger.grid(row=3, column=0)
burger_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=burger)
burger_entry.grid(row=3, column=1)

lbl_pizza = Label(frame2, text="Pizza ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_pizza.grid(row=4, column=0)
pizza_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=pizza)
pizza_entry.grid(row=4, column=1)

lbl_cheese = Label(frame2, text="Cheese burger ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_cheese.grid(row=5, column=0)
cheese_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=cheese)
cheese_entry.grid(row=5, column=1)

lbl_drink = Label(frame2, text="Drinks ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_drink.grid(row=0, column=2)
drink_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=drink)
drink_entry.grid(row=0, column=3)

lbl_cost = Label(frame2, text="Cost ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_cost.grid(row=1, column=2)
cost_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=cost)
cost_entry.grid(row=1, column=3)

lbl_service = Label(frame2, text="Service charge ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_service.grid(row=2, column=2)
service_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=service)
service_entry.grid(row=2, column=3)

lbl_tax = Label(frame2, text="Tax ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_tax.grid(row=3, column=2)
tax_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=tax)
tax_entry.grid(row=3, column=3)

lbl_subtotal = Label(frame2, text="Subtotal ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_subtotal.grid(row=4, column=2)
subtotal_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=subtotal)
subtotal_entry.grid(row=4, column=3)

lbl_total = Label(frame2, text="Total ",font=('arial', 16, 'bold'), fg='purple', bd=16, anchor='w')
lbl_total.grid(row=5, column=2)
total_entry = Entry(frame2, font=('arial', 16, 'bold'), bd=10, justify='right', insertwidth=4, textvariable=total)
total_entry.grid(row=5, column=3)

#Price calculation function
def PRICE():
    p = Tk()
    p.title("Price List")
    p.geometry("500x220+0+0")

    lbl = Label(p,font=('arial',15,'bold'),text="ITEM", fg="black", bd=5)
    lbl.grid(row=0,column=0)
    lbl = Label(p,font=('arial',15,'bold'),text="__________",fg="white",anchor=W)
    lbl.grid(row=0,column=2)
    lbl = Label(p,font=('arial',15,'bold'),text="Price", fg='black', anchor=W)
    lbl.grid(row=0,column=3)
    lbl = Label(p,font=('arial',15,'bold'),text="Fries", fg='black', anchor=W)
    lbl.grid(row=1,column=0)
    lbl = Label(p,font=('arial',15,'bold'),text="180", fg='black', anchor=W)
    lbl.grid(row=1,column=3)
    lbl = Label(p,font=('arial',15,'bold'),text="Lunch", fg='black', anchor=W)
    lbl.grid(row=2,column=0)
    lbl = Label(p,font=('arial',15,'bold'),text="180", fg='black', anchor=W)
    lbl.grid(row=2,column=3)
    lbl = Label(p,font=('arial',15,'bold'),text="Burger", fg='black', anchor=W)
    lbl.grid(row=3,column=0)
    lbl = Label(p,font=('arial',15,'bold'),text="80", fg='black', anchor=W)
    lbl.grid(row=3,column=3)
    lbl = Label(p,font=('arial',15,'bold'),text="Pizza", fg='black', anchor=W)
    lbl.grid(row=4,column=0)
    lbl = Label(p,font=('arial',15,'bold'),text="220", fg='black', anchor=W)
    lbl.grid(row=4,column=3)
    lbl = Label(p,font=('arial',15,'bold'),text="Cheese burger", fg='black', anchor=W)
    lbl.grid(row=5,column=0)
    lbl = Label(p,font=('arial',15,'bold'),text="120", fg='black', anchor=W)
    lbl.grid(row=5,column=3)
    lbl = Label(p,font=('arial',15,'bold'),text="Drinks", fg='black', anchor=W)
    lbl.grid(row=6,column=0)
    lbl = Label(p,font=('arial',15,'bold'),text="140", fg='black', anchor=W)
    lbl.grid(row=6,column=3)

    p.mainloop()

#Total cost calculation function
def TOTAL():
    x = random.randint(10998,299080)
    randomRef = str(x)
    rand.set(randomRef)

    if(fries.get()==""):
        Cofries = 0
    else:
        Cofries = float(fries.get())

    if(lunch.get()==""):
        Colunch = 0
    else:
        Colunch = float(lunch.get())

    if(burger.get()==""):
        Coburger = 0
    else:
        Coburger = float(burger.get())

    if(pizza.get()==""):
        Copizza = 0
    else:
        Copizza = float(pizza.get())

    if(cheese.get()==""):
        Cocheese = 0
    else:
        Cocheese = float(cheese.get())

    if(drink.get()==""):
        Codrink = 0
    else:
        Codrink = float(drink.get())


    cost_of_fries = Cofries * 180
    cost_of_lunch = Colunch * 180
    cost_of_burger = Colunch * 80
    cost_of_pizza = Copizza * 220
    cost_of_cheese = Cocheese * 120
    cost_of_drink = Codrink * 140

    Cost_of_meal = "Rs.", str('%.2f'%(cost_of_fries + cost_of_lunch + cost_of_burger + cost_of_pizza + cost_of_cheese + cost_of_drink))
    Ser_charge = ((cost_of_fries + cost_of_lunch + cost_of_burger + cost_of_pizza + cost_of_cheese + cost_of_drink) / 99)
    Pay_tax = ((cost_of_fries + cost_of_lunch + cost_of_burger + cost_of_pizza + cost_of_cheese + cost_of_drink) * 0.2)
    Total_cost = (cost_of_fries + cost_of_lunch + cost_of_burger + cost_of_pizza + cost_of_cheese + cost_of_drink)

    Service = "Rs.", str('%.2f'%Ser_charge)
    Overall_cost = "Rs.", str('%.2f'%(Pay_tax+Total_cost+Ser_charge))
    Paid_tax = "Rs.", str('%.2f'%Pay_tax)

    cost.set(Cost_of_meal)
    service.set(Service)
    tax.set(Paid_tax)
    subtotal.set(Cost_of_meal)
    total.set(Overall_cost)


#Reset function
def Reset():
    rand.set("")
    fries.set("")
    lunch.set("")
    burger.set("")
    pizza.set("")
    cheese.set("")
    drink.set("")
    cost.set("")
    service.set("")
    tax.set("")
    subtotal.set("")
    total.set("")

#Exit function
def Exit():
    m.destroy()

#CONTROLLING BUTTONS
price_btn = Button(frame2, text="Price ", relief=RAISED, font=('arial',16,'bold'), fg='brown',width=10,padx=16, pady=8,bd=16,command=PRICE)
price_btn.grid(row=7, column=0)

total_btn = Button(frame2, text="Total ", relief=RAISED, font=('arial',16,'bold'), fg='brown',width=10,padx=16, pady=8,bd=16,command=TOTAL)
total_btn.grid(row=7, column=1)

reset_btn = Button(frame2, text="Reset ", relief=RAISED, font=('arial',16,'bold'), fg='brown',width=10,padx=16, pady=8,bd=16,command=Reset)
reset_btn.grid(row=7, column=2)

exit_btn = Button(frame2, text="Exit ", relief=RAISED, font=('arial',16,'bold'), fg='brown',width=10,padx=16, pady=8,bd=16,command=Exit)
exit_btn.grid(row=7, column=3)

m.mainloop()