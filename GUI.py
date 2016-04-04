from tkinter import *

root = Tk()
labelFont = "Helvetica"
titleFont = "Helvetica"
statusText = 'Idle...'


def add_drink():
    queue.insert(END, drinkList.get(drinkList.curselection()))


def remove_drink():
    queue.delete(queue.curselection())


def add_drink_to_list():
    if len(drinkToCreate.get()) > 0:
        drinkList.insert(END, drinkToCreate.get())
        drinkToCreate.delete(0, 50)


def remove_drink_from_list():
    drinkList.delete(drinkList.curselection())


def e1button():
    E1.grid(row=1, column=1)


def pour():
    pouring = True
    while pouring == 1:
        global statusText
        statusText = 'Pouring'
        pouring = False


E1 = Entry(root, bd=5)

# Lists
drinkList = Listbox(root, width=50, )
drinkList.insert(1, "Rum")
drinkList.insert(2, "Vodka")

queue = Listbox(root, width=50, )

# Create Buttons
AddButton = Button(root, text="Add drink to queue", command=add_drink, width=20)
RemoveButton = Button(root, text="Remove drink from queue", command=remove_drink, width=20)
AddDrinkToList = Button(root, text="Add drink to list", command=add_drink_to_list)
RemoveDrinkFromList = Button(root, text="Remove drink from list", command=remove_drink_from_list)

photo = PhotoImage(file="Title.gif")

# Create Labels
drinkLabel = Label(root, text="Drink List", relief=FLAT, font=(labelFont, 12))
queueLabel = Label(root, text="Queue", relief=FLAT, font=(labelFont, 12))
title = Label(root, image=photo, relief=FLAT, font=(titleFont, 28))
title.photo = photo
statusBar = Label(root, text=statusText, bd=1, relief=SUNKEN)

# Entries
drinkToCreate = Entry(root, )

# Menu
menu = Menu(root)
subMenu = Menu(menu)
menu.add_cascade(label='Options', menu=subMenu)
subMenu.add_command(label='Settings', command=None)

# Frames
statusFrame = Frame(root,)

# Grid Layout
root.config(menu=menu)
title.grid(row=0, column=0, columnspan=3)
drinkLabel.grid(row=1, column=0)
queueLabel.grid(row=1, column=2)
AddButton.grid(row=2, column=1, sticky=S)
drinkList.grid(row=2, rowspan=2, column=0)
queue.grid(row=2, rowspan=2, column=2)
RemoveButton.grid(row=3, column=1, stick=N)
AddDrinkToList.grid(row=4, column=0, sticky=W)
drinkToCreate.grid(row=4, column=0, sticky=E)
statusBar.grid(row=100, column=0, columnspan=4, sticky=W)
root.mainloop()

