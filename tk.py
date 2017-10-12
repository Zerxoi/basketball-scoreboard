from tkinter import *

root = Tk()

v = IntVar()

master = Frame(root)
master.grid(row=0, column=0)
Label(master, text="Blue Team",
      fg="blue",
      font="Consolas 20 bold").grid(row=0, column=0)
Label(master, text="-->",
      fg="black",
      font="Consolas 20 bold").grid(row=0, column=1)
Label(master, text="Red Team",
      fg="red",
      font="Consolas 20 bold").grid(row=0, column=2)
blueinfo = Frame(master)
blueinfo.grid(row=1, column=0)
Label(blueinfo, text='100',
      fg='blue',
      font="Consolas 60 bold").grid(row=0, column=0)
Label(blueinfo, text='+++-',
      fg='black',
      font="Consolas 20 bold").grid(row=1, column=0)
Label(blueinfo, text='3',
      fg='black',
      font="Consolas 40 bold").grid(row=2, column=0)
matchinfo = Frame(master)
matchinfo.grid(row=1, column=1)
Label(matchinfo, text='Round 2',
      fg='black',
      font="Consolas 20 bold").grid(row=0, column=0)
Label(matchinfo, text='12:00',
      fg='green',
      font="Consolas 40 bold"
      ).grid(row=1, column=0)
Label(matchinfo, text='24',
      fg='brown',
      font="Consolas 30 bold"
      ).grid(row=2, column=0)
redinfo = Frame(master)
redinfo.grid(row=1, column=2)
Label(redinfo, text='098',
      fg='red',
      font="Consolas 60 bold").grid(row=0, column=0)
Label(redinfo, text='++--',
      fg='black',
      font="Consolas 20 bold").grid(row=1, column=0)
Label(redinfo, text='2',
      fg='black',
      font="Consolas 40 bold").grid(row=2, column=0)

bluectl = Frame(master)
bluectl.grid(row=3, column=0)
Button(bluectl, text="1",
       padx=30,
       pady=2,
       font="Consolas 20 bold").grid(row=0, column=0)
Button(bluectl, text="2",
       padx=30,
       pady=2,
       font="Consolas 20 bold").grid(row=1, column=0)
Button(bluectl, text="3",
       padx=30,
       pady=2,
       font="Consolas 20 bold").grid(row=2, column=0)

matchctl = Frame(master)
matchctl.grid(row=3, column=1)
Button(matchctl, text="Start",
       width=15,
       height=3,
       font="Consolas 10 bold").grid(row=0, column=0)
Button(matchctl, text="Stop",
       width=15,
       height=3,
       font="Consolas 10 bold").grid(row=1, column=0)

Button(matchctl, text="Overtime",
       width=15,
       height=3,
       font="Consolas 10 bold").grid(row=2, column=0)

redctl = Frame(master)
redctl.grid(row=3, column=2)
Button(redctl, text="1",
       padx=30,
       pady=2,
       font="Consolas 20 bold").grid(row=0, column=0)
Button(redctl, text="2",
       padx=30,
       pady=2,
       font="Consolas 20 bold").grid(row=1, column=0)
Button(redctl, text="3",
       padx=30,
       pady=2,
       font="Consolas 20 bold").grid(row=2, column=0)


root.mainloop()
