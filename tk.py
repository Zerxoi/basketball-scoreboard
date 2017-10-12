from tkinter import *

class Application(Frame):
    def __init__(self, master):
        self.blueteamname = ''
        self.redteamname = ''
        self.bluescore = 0
        self.redscore = 0
        self.bluefoul = 0
        self.redfoul = 0
        self.round = 1
        self.createcontrolinterface(master)
        self.createsubwindow()

    def createsubwindow(self):
        self.sub = Tk()
        self.top = Frame(self.sub)
        self.top.pack()
        self.bluenameentrylabel = Label(self.top,
                                        text="Blue Team Name:" if self.blueteamname == '' else self.blueteamname)
        self.bluenameentrylabel.grid(row=0, column=0)
        self.bluenameentry = Entry(self.top)
        self.bluenameentry.grid(row=0, column=1)
        self.rednameentrylabel = Label(self.top,
                                       text="Red Team Name:" if self.blueteamname == '' else self.blueteamname)
        self.rednameentrylabel.grid(row=1, column=0)
        self.rednameentry = Entry(self.top)
        self.rednameentry.grid(row=1, column=1)
        self.btm = Frame(self.sub)
        self.btm.pack()
        self.commitbtn = Button(self.btm, text='Commit', command=self.inputcommit)
        self.commitbtn.pack()

    def inputcommit(self):
        self.blueteamname = self.bluenameentry.get()
        self.redteamname = self.rednameentry.get()

    def createcontrolinterface(self, master):
        super().__init__(master)
        self.pack()
        self.bluenamelabel = Label(self, text="Blue Team" if self.blueteamname=='' else self.blueteamname,
                                   fg="blue",
                                   font="Consolas 20 bold")
        self.bluenamelabel.grid(row=0, column=0)

        self.hglabel = Label(self, text="VS",
                             fg="black",
                             font="Consolas 20 bold")
        self.hglabel.grid(row=0, column=1)

        self.rednamelabel = Label(self, text="Red Team" if self.redteamname=='' else self.redteamname,
                                  fg="red",
                                  font="Consolas 20 bold")
        self.rednamelabel.grid(row=0, column=2)
        self.blueinfo = Frame(self)
        self.blueinfo.grid(row=1, column=0)
        self.bluescorelabel = Label(self.blueinfo,
                                    text=self.bluescore,
                                    fg='blue',
                                    font="Consolas 60 bold")
        self.bluescorelabel.grid(row=0, column=0)
        self.bluefoullabel = Label(self.blueinfo,
                                   text=self.bluefoul,
                                   fg='black',
                                   font="Consolas 20 bold")
        self.bluefoullabel.grid(row=1, column=0)
        self.matchinfo = Frame(self)
        self. matchinfo.grid(row=1, column=1)
        self.roundlabel = Label(self.matchinfo, text='Round ' + str(self.round),
                                fg='black',
                                font="Consolas 20 bold")
        self.roundlabel.grid(row=0, column=0)
        self.timerlabel = Label(self.matchinfo, text='00:00',
                                fg='green',
                                font="Consolas 40 bold")
        self.timerlabel.grid(row=1, column=0)
        self.redinfo = Frame(self)
        self.redinfo.grid(row=1, column=2)
        self.redscorelabel = Label(self.redinfo,
                                   text=self.redscore,
                                   fg='red',
                                   font="Consolas 60 bold")
        self.redscorelabel.grid(row=0, column=0)
        self.redfoullabel = Label(self.redinfo,
                                  text=self.redfoul,
                                  fg='black',
                                  font="Consolas 20 bold")
        self.redfoullabel.grid(row=2, column=0)
        self.bluectl = Frame(self)
        self.bluectl.grid(row=3, column=0)
        self.blue1btn = Button(self.bluectl,
                               text="1",
                               fg='white',
                               bg='blue',
                               padx=30,
                               pady=1,
                               font="Consolas 15 bold",
                               command=self.blueplus1)
        self.blue1btn.grid(row=0, column=0)
        self.blue2btn = Button(self.bluectl,
                               text="2",
                               fg='white',
                               bg='blue',
                               padx=30,
                               pady=1,
                               font="Consolas 15 bold",
                               command=self.blueplus2)
        self.blue2btn.grid(row=1, column=0)
        self.blue3btn = Button(self.bluectl,
                               text="3",
                               fg='white',
                               bg='blue',
                               padx=30,
                               pady=1,
                               font="Consolas 15 bold",
                               command=self.blueplus3)
        self.blue3btn.grid(row=2, column=0)
        self.bluefoulbtn = Button(self.bluectl,
                                  text="Foul",
                                  fg='white',
                                  bg='blue',
                                  padx=30,
                                  pady=1,
                                  font="Consolas 15 bold",
                                  command=self.bluefouladd)
        self.bluefoulbtn.grid(row=3, column=0)
        self.matchctl = Frame(self)
        self.matchctl.grid(row=3, column=1)
        self.matchstartbtn = Button(self.matchctl, text="Start",
                                    width=15,
                                    height=3,
                                    font="Consolas 10 bold")
        self.matchstartbtn.grid(row=0, column=0)
        self.matchstopbtn = Button(self.matchctl, text="Stop",
                                   width=15,
                                   height=3,
                                   font="Consolas 10 bold")
        self.matchstopbtn.grid(row=1, column=0)
        self.redctl = Frame(self)
        self.redctl.grid(row=3, column=2)
        self.red1btn = Button(self.redctl,
                              text="1",
                              fg='white',
                              bg='red',
                              padx=30,
                              pady=1,
                              font="Consolas 15 bold",
                              command=self.redplus1)
        self.red1btn.grid(row=0, column=0)
        self.red2btn = Button(self.redctl,
                              text="2",
                              fg='white',
                              bg='red',
                              padx=30,
                              pady=1,
                              font="Consolas 15 bold",
                              command=self.redplus2)
        self.red2btn.grid(row=1, column=0)
        self.red3btn = Button(self.redctl,
                              text="3",
                              fg='white',
                              bg='red',
                              padx=30,
                              pady=1,
                              font="Consolas 15 bold",
                              command=self.redplus3)
        self.red3btn.grid(row=2, column=0)
        self.redfoulbtn = Button(self.redctl,
                                 text="Foul",
                                 fg='white',
                                 bg='red',
                                 padx=30,
                                 pady=1,
                                 font="Consolas 15 bold",
                                 command=self.redfouladd)
        self.redfoulbtn.grid(row=3, column=0)

    def blueplus1(self):
        self.bluescore += 1
        self.bluescorelabel['text'] = self.bluescore

    def blueplus2(self):
        self.bluescore += 2
        self.bluescorelabel['text'] = self.bluescore

    def blueplus3(self):
        self.bluescore += 3
        self.bluescorelabel['text'] = self.bluescore

    def bluefouladd(self):
        self.bluefoul += 1
        self.bluefoullabel['text'] = self.bluefoul

    def redplus1(self):
        self.redscore += 1
        self.redscorelabel['text'] = self.redscore

    def redplus2(self):
        self.redscore += 2
        self.redscorelabel['text'] = self.redscore

    def redplus3(self):
        self.redscore += 3
        self.redscorelabel['text'] = self.redscore

    def redfouladd(self):
        self.redfoul += 1
        self.redfoullabel['text'] = self.redfoul


root = Tk()
app = Application(root)
root.mainloop()
