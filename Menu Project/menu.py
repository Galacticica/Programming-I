'''
File: menu.py
Author: Reagan Zierke
Date: 9/17/2024
Description: This program creates a menu for a dessert company 
and allows the user to create an order
'''


import tkinter
from tkinter import *
import time
import threading
import random

#declare variables
coffee_items = ["Mocha", "Latte", "Espresso"]
icecream_items = ["Cone", "Shake", "Blend"]
icecream_flavors = ["Vanilla", "Chocolate", "Strawberry", "FOTD"]
dessert_items = ["Cookie", "Pie Slice", "Brownie"]
ordered_items = []
fotd_flavors = ["Mint", "Lemon", "OREO", "Orange", "Caramel", "Coffee", "Smore", "Pineapple", "Cherry", "Banana", "Cake", "Grape", "Pumpkin", "Watermelon", "Mystery"]

#create the menu gui
menu = tkinter.Tk()
menu.title= "Generic Dessert Store" #why doesn't this line work?

#background task that changes a flavor every 10 seconds
def random_flavor():
    while True:
        new_flavor = random.choice(fotd_flavors)
        icecream_flavors[3] = new_flavor
        time.sleep(10)

#gets all grid widgets
def get_grid_wigets(parent):
    widgets = []
    for child in parent.winfo_children():
        if child.grid_info():
            widgets.append(child)
    if len(widgets) > 0:
        widgets.pop(0)
    return widgets

#updates the gui for the main menu
def main_menu():
    widgets = get_grid_wigets(menu)
    for widget in widgets:
        widget.grid_forget()
    restaraunt_name = tkinter.Label(menu, text="Generic Dessert Store\u2122", width=25, height=2, font=('Helvetica bold',20), borderwidth=1, relief="solid")
    restaraunt_name.grid(row=0, column=0, columnspan=3)
    spacer1 = tkinter.Label(menu, text="")
    spacer1.grid(row=1)
    activate_coffee = tkinter.Button(menu, text="Coffee Menu", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=coffee_menu)
    activate_coffee.grid(row=2, column=1, columnspan=1)
    spacer2=spacer1
    spacer2.grid(row=3)
    activate_dessert = tkinter.Button(menu, text="Dessert Menu", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=dessert_menu)
    activate_dessert.grid(row=4, column=1, columnspan=1)
    spacer3=spacer1
    spacer3.grid(row=5)
    activate_icecream = tkinter.Button(menu, text="Ice Cream Menu", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=icecream_menu)
    activate_icecream.grid(row=6, column=1, columnspan=1)
    spacer4=spacer1
    spacer4.grid(row=7, rowspan=3)
    complete_order = tkinter.Button(menu, text="Complete Order", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=additional_comments)
    complete_order.grid(row=10, column=1, columnspan=1)

#shows that an item was added to the order
def add_item(item):
    ordered_items.append(tkinter.Label(menu, text=item, width=15, height=1, font=('Helvetica bold',13), borderwidth=0.2, relief="solid"))
    widgets = get_grid_wigets(menu)
    for widget in widgets:
        widget.grid_forget()
    added_item = tkinter.Label(menu, text=f"Added {item}", width=21, height=2, font=('Helvetica bold',15), borderwidth=1, relief="solid")
    added_item.grid(row=2, column=1, columnspan=1)
    menu.after(1000, main_menu)

#creates the gui for the coffee menu
def coffee_menu():
    widgets = get_grid_wigets(menu)
    for widget in widgets:
        widget.grid_forget()
    option1 = tkinter.Button(menu, text=f"{coffee_items[0]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(coffee_items[0]))
    option1.grid(row=2, column=1, columnspan=1)
    option2 = tkinter.Button(menu, text=f"{coffee_items[1]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(coffee_items[1]))
    option2.grid(row=4, column=1, columnspan=1)
    option3 = tkinter.Button(menu, text=f"{coffee_items[2]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(coffee_items[2]))
    option3.grid(row=6, column=1, columnspan=1)

#creates the gui for the icecream menu
def icecream_menu():
    widgets = get_grid_wigets(menu)
    for widget in widgets:
        widget.grid_forget()
    option1 = tkinter.Button(menu, text=f"{icecream_items[0]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:flavor_select(icecream_items[0]))
    option1.grid(row=2, column=1, columnspan=1)
    option2 = tkinter.Button(menu, text=f"{icecream_items[1]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:flavor_select(icecream_items[1]))
    option2.grid(row=4, column=1, columnspan=1)
    option3 = tkinter.Button(menu, text=f"{icecream_items[2]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:flavor_select(icecream_items[2]))
    option3.grid(row=6, column=1, columnspan=1)
    
    
#creates the gui for choosing the flavor of the icecream
def flavor_select(item):
    widgets = get_grid_wigets(menu)
    for widget in widgets:
        widget.grid_forget()
    current_fotd = icecream_flavors[3]
    option1 = tkinter.Button(menu, text=f"{icecream_flavors[0]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(icecream_flavors[0] + " " + item))
    option1.grid(row=2, column=1, columnspan=1)
    option2 = tkinter.Button(menu, text=f"{icecream_flavors[1]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(icecream_flavors[1] + " " + item))
    option2.grid(row=4, column=1, columnspan=1)
    option3 = tkinter.Button(menu, text=f"{icecream_flavors[2]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(icecream_flavors[2] + " " + item))
    option3.grid(row=6, column=1, columnspan=1)
    option4 = tkinter.Button(menu, text=f"{icecream_flavors[3]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(current_fotd + " " + item))
    option4.grid(row=8, column=1, columnspan=1)

#creates the gui for the dessert menu
def dessert_menu():
    widgets = get_grid_wigets(menu)
    for widget in widgets:
        widget.grid_forget()
    option1 = tkinter.Button(menu, text=f"{dessert_items[0]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(dessert_items[0]))
    option1.grid(row=2, column=1, columnspan=1)
    option2 = tkinter.Button(menu, text=f"{dessert_items[1]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(dessert_items[1]))
    option2.grid(row=4, column=1, columnspan=1)
    option3 = tkinter.Button(menu, text=f"{dessert_items[2]}", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="groove", state=NORMAL, command=lambda:add_item(dessert_items[2]))
    option3.grid(row=6, column=1, columnspan=1)

#allows the user to add any additional comments EX: Oat Milk
def additional_comments():
    widgets = get_grid_wigets(menu)
    for widget in widgets:
        widget.grid_forget()
    question_text = tkinter.Label(menu, text="Any additional comments? (Type no when finished)", width=37, height=1, font=('Helvetica bold',10), borderwidth=1, relief="solid")
    question_text.grid(row=1, column=0, columnspan=3)
    comment_box = tkinter.Entry(menu, width=20, font=('Helvetica bold',12), borderwidth=1, relief="solid")
    comment_box.grid(row=2, column=0, columnspan=3)
    comments = []
    character_limit = 15
    characters_left = tkinter.Label(menu, text=character_limit, width=2, height=2, font=('Helvetica bold',10), borderwidth=0.2, relief="solid")
    characters_left.grid(row=2, column=2)

    def add_comment(event):
        new_comment = comment_box.get()
        if new_comment.lower() == "no":
            display_receipt(comments)
        elif new_comment == "" and new_comment == " ":
            pass
        else:
            comments.append(tkinter.Label(menu, text=new_comment, width=15, height=1, font=('Helvetica bold',10), borderwidth=0.2, relief="solid"))
            comment_box.delete(0, 'end')

    def limit_characters(event):
        characters_left.config(text=character_limit - len(comment_box.get()))
        content = comment_box.get()
        if len(content) > character_limit:
            comment_box.delete(character_limit, 'end')

    comment_box.bind('<Return>', add_comment)
    comment_box.bind('<KeyRelease>', limit_characters)
    
#Displays the final order along with all comments
def display_receipt(comments):
    widgets = get_grid_wigets(menu)
    for widget in widgets:
        widget.grid_forget()
    item_label = tkinter.Label(menu, text="Items\nOrdered", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="solid")
    item_label.grid(row=2, column=0, columnspan=1)
    comment_label = tkinter.Label(menu, text="Additional\nComments", width=15, height=2, font=('Helvetica bold',15), borderwidth=1, relief="solid")
    comment_label.grid(row=2, column=2, columnspan=1)
    num_row = 3
    for item in ordered_items:
        item.grid(row=num_row, column=0, columnspan=1)
        num_row = num_row + 1
    num_row = 3
    for comment in comments:
        comment.grid(row=num_row, column=2, columnspan=1)
        num_row = num_row + 1










if __name__ == "__main__":

    threading.Thread(target=random_flavor, daemon=True).start()

    main_menu()
    menu.mainloop()
