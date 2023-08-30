from tkinter import *
from tkinter import messagebox


# Functions 

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else: 
        messagebox.showwarning('warning', "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

# Creating a window

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('Python Guide')
ws.config(bg="#223441")
ws.resizable(width=False, height=False)

# Creating a frame
frame = Frame(ws)
frame.pack(pady=10)

# Listing Box
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness= 0,
    selectbackground ='#a6a6a6',
    activestyle="none"
)

lb.pack(side=LEFT, fill=BOTH)

# Adding dummy data

task_list = [
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take nap',
    'Learn something',
    'paint canvas']

for item in task_list:
    lb.insert(END, item)

# Adding scroll bars

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)


# Adding entry box
my_entry = Entry(
    ws, font=('times', 24)
)

my_entry.pack(pady = 20)

# Adding another frame for buttons
button_frame = Frame(ws)
button_frame.pack(pady = 20)


# Adding buttons

addTsk_btn = Button(
    button_frame,
    text = 'Add task',
    font = ('times 14'),
    bg = '#c5f776',
    padx = 20,
    pady = 10,
    command = newTask,
)

addTsk_btn.pack(fill = BOTH, expand =True, side = LEFT)

delTask_btn = Button(
    button_frame, 
    text = 'Delete Task',
    font = ('times 14'),
    bg = '#ff8b61',
    padx = 20,
    pady = 10,
    command= deleteTask
)

delTask_btn.pack(fill = BOTH, expand = True, side = LEFT)
ws.mainloop()
