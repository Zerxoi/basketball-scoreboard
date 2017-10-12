from tkinter import *

root = Tk()

# v = IntVar()
#
# Label(root,
#       text="""Choose a
# programming language:""",
#       justify = LEFT,
#       padx = 20).pack()
# Radiobutton(root,
#             text="Python",
#             padx = 20,
#             variable=v,
#             value=1).pack(anchor=W)
# Radiobutton(root,
#             text="Perl",
#             padx = 20,
#             variable=v,
#             value=2).pack(anchor=W)
#
# Label(root,  textvariable=v).pack()
#
# mainloop()

preview = Frame(root)
preview.pack()

previewtop = Frame(preview)
previewtop.pack(side = 'top')

previewtop1 = Frame(previewtop)
previewtop1.pack(side = 'left')

previewtop2 = Frame(previewtop)
previewtop2.pack(side = 'left')

previewtop3 = Frame(previewtop)
previewtop3.pack(side = 'left')

previewmid = Frame(preview)
previewmid.pack(side = 'top')

previewmid1 = Frame(previewmid)
previewmid1.pack(side = 'left')

previewmid1t = Frame(previewmid1)
previewmid1t.pack()

previewmid1b = Frame(previewmid1)
previewmid1b.pack()

previewmid2 = Frame(previewmid)
previewmid2.pack(side = 'left')

previewmid2t = Frame(previewmid2)
previewmid2t.pack()

previewmid2b = Frame(previewmid2)
previewmid2b.pack()

previewmid3 = Frame(previewmid)
previewmid3.pack(side = 'left')

previewmid3t = Frame(previewmid3)
previewmid3t.pack()

previewmid3b = Frame(previewmid3)
previewmid3b.pack()

previewbtm = Frame(preview)
previewbtm.pack(side = 'top')

previewbtm1 = Frame(previewbtm)
previewbtm1.pack(side = 'left', fill = X)

previewbtm2 = Frame(previewbtm)
previewbtm2.pack(side = 'left')

previewbtm3 = Frame(previewbtm)
previewbtm3.pack(side = 'left', fill = X)

controller = Frame(root)
controller.pack()

controllertop = Frame(controller)
controllertop.pack()

controllertop1 =  Frame(controllertop)
controllertop1.pack(side =  'left')

controllertop2 =  Frame(controllertop)
controllertop2.pack(side =  'left')

controllertop3 =  Frame(controllertop)
controllertop3.pack(side =  'left')

controllermid = Frame(controller)
controllermid.pack()

Label(previewtop1,
      text = "Blue Team",
      fg = "blue",
      font = "Helvetica 20 bold").pack()

Label(previewtop3,
      text = "Red Team",
      fg = "red",
      font = "Helvetica 20 bold").pack()

Label(previewmid1t,
      text="100",
      fg = "blue",
      font = "Helvetica 90 bold").pack()

Label(previewmid1b,
      text="[x] [x] [x] [ ]",
      fg = "blue",
      font = "Helvetica 10 bold").pack()

Label(previewmid2t,
      text="第1场",
      fg = "black",
      font = "Helvetica 20 bold").pack()

Label(previewmid2t,
      text="12:00",
      fg = "black",
      font = "Helvetica 20 bold").pack()

Label(previewmid3t,
      text="098",
      fg = "red",
      font = "Helvetica 90 bold").pack()

Label(previewmid3b,
      text="[x] [x] [ ] [ ]",
      fg = "red",
      font = "Helvetica 10 bold").pack()

Label(previewbtm1,
      text = '3',
      fg = 'blue',
      font = "Helvetica 50 bold").pack()

Label(previewbtm2,
      text = '24',
      fg = 'green',
      font = "Helvetica 50 bold").pack()

Label(previewbtm3,
      text = '2',
      fg = 'red',
      font = "Helvetica 50 bold").pack()

Button(controllertop1,
       text="1",
       fg = 'white',
       bg = 'blue',
       font = "Helvetica 30 bold").pack(side = 'left')

Button(controllertop1,
       text="2",
       fg = 'white',
       bg = 'blue',
       font="Helvetica 30 bold").pack(side = 'left')

Button(controllertop1,
       text="3",
       fg = 'white',
       bg = 'blue',
       font="Helvetica 30 bold").pack(side = 'left')

Button(controllertop3,
       text="1",
       fg = 'white',
       bg = 'red',
       font="Helvetica 30 bold").pack(side = 'right')

Button(controllertop3,
       text="2",
       fg = 'white',
       bg = 'red',
       font="Helvetica 30 bold").pack(side = 'right')

Button(controllertop3,
       text="3",
       fg = 'white',
       bg = 'red',
       font="Helvetica 30 bold").pack(side = 'right')



root.mainloop()