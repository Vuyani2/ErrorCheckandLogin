from tkinter import *
from tkinter import messagebox


def qualification():
    amount = entryamount.get()
    try:
        amount = int(amount)
        if amount > 5000:
            messagebox.showinfo("STATUS FEEDBACK","Congratulation. You Qualify to go to Malaysia")
        else:
            messagebox.showinfo("STATUS FEEDBACK","You don't qualify")
    except ValueError:
        messagebox.showinfo("Error","please enter number as amount")





def clear_entry():

    entryamount.delete(0, 'end')



def ExitApplication():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


root = Tk()
root.title("Password and username Verification")
root.geometry("500x400")
root.config(bg='#8dc63f')
frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

entryamount = Entry(frame,)
entryamount.grid(row=3, column=1, pady=5)

lblamount = Label(frame, text="please enter amount in your account")
lblamount.grid(row=2, column=1)

reset_btn = Button(frame, text='clear', bg='#8dc63f', command=clear_entry)
reset_btn.grid(row=6, column=2, pady=8)

exit_btn = Button(frame, text='Exit', bg='#8dc63f', command=ExitApplication)
exit_btn.grid(row=5, column=2, pady=5)

cal_btn = Button(frame, text='Check Qualification', bg='#8dc63f', command=qualification)
cal_btn.grid(row=4, column=1, pady=5)
root.mainloop()