from tkinter import *


def digitaldetect(str):
    if str == '':
        return False
    for i in str:
        if i < '0' or i > '9':
            return False
    return True


class Application(Frame):
    def __init__(self, master):
        self.blueteamname = ''
        self.redteamname = ''
        self.root = master
        self.count = False
        self.commited = False
        self.minset = 0
        self.secset = 0
        self.min = 0
        self.sec = 0
        self.bluescore = 0
        self.redscore = 0
        self.bluefoul = 0
        self.redfoul = 0
        self.roundnum = 0
        self.round = 1
        self.createcontrolinterface(self.root)
        self.createentry()
        self.createinfowindow()

    def createcontrolinterface(self, master):
        super().__init__(master)
        self.grid(row=0, column=0)
        self.bluenamelabel = Label(self, text="Blue",
                                   fg="blue",
                                   font="Consolas 20 bold")
        self.bluenamelabel.grid(row=0, column=0)

        self.hglabel = Label(self, text="VS",
                             fg="black",
                             font="Consolas 20 bold")
        self.hglabel.grid(row=0, column=1)

        self.rednamelabel = Label(self, text="Red",
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
        self.matchinfo.grid(row=1, column=1)
        self.roundlabel = Label(self.matchinfo, text='Round 1',
                                fg='black',
                                font="Consolas 20 bold")
        self.roundlabel.grid(row=0, column=0)
        self.timerlabel = Label(self.matchinfo, text='0:0',
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
        self.bluectl.grid(row=2, column=0)
        self.blue1btn = Button(self.bluectl,
                               text="1",
                               fg='white',
                               bg='blue',
                               padx=30,
                               pady=1,
                               font="Consolas 15 bold",
                               state='disable',
                               command=self.blueplus1)
        self.blue1btn.grid(row=0, column=0)
        self.blue2btn = Button(self.bluectl,
                               text="2",
                               fg='white',
                               bg='blue',
                               padx=30,
                               pady=1,
                               font="Consolas 15 bold",
                               state='disable',
                               command=self.blueplus2)
        self.blue2btn.grid(row=1, column=0)
        self.blue3btn = Button(self.bluectl,
                               text="3",
                               fg='white',
                               bg='blue',
                               padx=30,
                               pady=1,
                               font="Consolas 15 bold",
                               state='disable',
                               command=self.blueplus3)
        self.blue3btn.grid(row=2, column=0)
        self.bluefoulbtn = Button(self.bluectl,
                                  text="Foul",
                                  fg='white',
                                  bg='blue',
                                  padx=30,
                                  pady=1,
                                  font="Consolas 15 bold",
                                  state='disable',
                                  command=self.bluefouladd)
        self.bluefoulbtn.grid(row=3, column=0)
        self.matchctl = Frame(self)
        self.matchctl.grid(row=2, column=1)
        self.matchstartbtn = Button(self.matchctl, text="Start",
                                    width=15,
                                    height=3,
                                    font="Consolas 10 bold",
                                    state='disable',
                                    command=self.matchstart)
        self.matchstartbtn.grid(row=0, column=0)
        self.matchstopbtn = Button(self.matchctl, text="Stop",
                                   width=15,
                                   height=3,
                                   font="Consolas 10 bold",
                                   state='disable',
                                   command=self.matchstop)
        self.matchstopbtn.grid(row=1, column=0)
        self.redctl = Frame(self)
        self.redctl.grid(row=2, column=2)
        self.red1btn = Button(self.redctl,
                              text="1",
                              fg='white',
                              bg='red',
                              padx=30,
                              pady=1,
                              font="Consolas 15 bold",
                              state='disable',
                              command=self.redplus1)
        self.red1btn.grid(row=0, column=0)
        self.red2btn = Button(self.redctl,
                              text="2",
                              fg='white',
                              bg='red',
                              padx=30,
                              pady=1,
                              font="Consolas 15 bold",
                              state='disable',
                              command=self.redplus2)
        self.red2btn.grid(row=1, column=0)
        self.red3btn = Button(self.redctl,
                              text="3",
                              fg='white',
                              bg='red',
                              padx=30,
                              pady=1,
                              font="Consolas 15 bold",
                              state='disable',
                              command=self.redplus3)
        self.red3btn.grid(row=2, column=0)
        self.redfoulbtn = Button(self.redctl,
                                 text="Foul",
                                 fg='white',
                                 bg='red',
                                 padx=30,
                                 pady=1,
                                 font="Consolas 15 bold",
                                 state='disable',
                                 command=self.redfouladd)
        self.redfoulbtn.grid(row=3, column=0)

    def blueplus1(self):
        if self.count:
            self.bluescore += 1
            self.bluescorelabel['text'] = self.bluescore

    def blueplus2(self):
        if self.count:
            self.bluescore += 2
            self.bluescorelabel['text'] = self.bluescore

    def blueplus3(self):
        if self.count:
            self.bluescore += 3
            self.bluescorelabel['text'] = self.bluescore

    def bluefouladd(self):
        if self.count:
            self.bluefoul += 1
            self.bluefoullabel['text'] = self.bluefoul

    def redplus1(self):
        if self.count:
            self.redscore += 1
            self.redscorelabel['text'] = self.redscore

    def redplus2(self):
        if self.count:
            self.redscore += 2
            self.redscorelabel['text'] = self.redscore

    def redplus3(self):
        if self.count:
            self.redscore += 3
            self.redscorelabel['text'] = self.redscore

    def redfouladd(self):
        if self.count:
            self.redfoul += 1
            self.redfoullabel['text'] = self.redfoul

    def matchstart(self):
        self.count = True
        self.matchstartbtn['state'] = 'disabled'
        self.matchstopbtn['state'] = 'normal'
        self.blue1btn['state'] = 'normal'
        self.blue2btn['state'] = 'normal'
        self.blue3btn['state'] = 'normal'
        self.bluefoulbtn['state'] = 'normal'
        self.red1btn['state'] = 'normal'
        self.red2btn['state'] = 'normal'
        self.red3btn['state'] = 'normal'
        self.redfoulbtn['state'] = 'normal'
        self.timercount()

    def timercount(self):
        if self.count:
            if self.sec <= 0 and self.min <= 0:
                self.matchstop()
                self.round += 1
                self.roundlabel['text'] = 'Round ' + str(self.round)
                self.min = self.minset
                self.sec = self.secset
                self.timerlabel['text'] = str(self.min) + ':' + str(self.sec)
                if self.round > self.roundnum:
                    self.matchstartbtn['state'] = 'disabled'

            else:
                if self.sec < 0:
                    self.sec = 59
                    self.min -= 1
                self.timerlabel['text'] = str(self.min) + ':' + str(self.sec)
                self.sec -= 1
                self.timerlabel.after(1000, self.timercount)

    def matchstop(self):
        self.count = False
        self.matchstartbtn['state'] = 'normal'
        self.matchstopbtn['state'] = 'disabled'
        self.blue1btn['state'] = 'disabled'
        self.blue2btn['state'] = 'disabled'
        self.blue3btn['state'] = 'disabled'
        self.bluefoulbtn['state'] = 'disabled'
        self.red1btn['state'] = 'disabled'
        self.red2btn['state'] = 'disabled'
        self.red3btn['state'] = 'disabled'
        self.redfoulbtn['state'] = 'disabled'

    def createentry(self):
        self.subwindow = Frame(self)
        self.subwindow['borderwidth'] = 2
        self.subwindow['relief'] = 'groove'
        self.subwindow.grid(row=1, column=3)
        self.bluenameentrylabel = Label(self.subwindow,
                                        text="Blue Team Name")
        self.bluenameentrylabel.grid(row=0, column=0)
        self.bluenameentry = Entry(self.subwindow)
        self.bluenameentry.grid(row=0, column=1)
        self.rednameentrylabel = Label(self.subwindow,
                                       text="Red Team Name")
        self.rednameentrylabel.grid(row=1, column=0)
        self.rednameentry = Entry(self.subwindow)
        self.rednameentry.grid(row=1, column=1)
        self.roundentrylabel = Label(self.subwindow,
                                     text="Rounds")
        self.roundentrylabel.grid(row=2, column=0)
        self.roundentry = Entry(self.subwindow)
        self.roundentry.grid(row=2, column=1)
        self.timeentrylabel = Label(self.subwindow,
                                    text="Time of Round")
        self.timeentrylabel.grid(row=3, column=0)
        self.minentrylabel = Label(self.subwindow,
                                   text="Min")
        self.minentrylabel.grid(row=4, column=0)
        self.minentry = Entry(self.subwindow)
        self.minentry.grid(row=4, column=1)
        self.secentrylabel = Label(self.subwindow,
                                   text="Sec")
        self.secentrylabel.grid(row=5, column=0)
        self.secentry = Entry(self.subwindow)
        self.secentry.grid(row=5, column=1)
        self.commitbtn = Button(self.subwindow,
                                text='Commit',
                                command=self.inputcommit)
        self.commitbtn.grid(row=6, column=1)
        self.resetbtn = Button(self.subwindow,
                               text='Reset',
                               command=self.reset)
        self.resetbtn.grid(row=6, column=0)

    def inputcommit(self):
        self.matchstartbtn['state'] = 'normal'
        self.commitbtn['state'] = 'disable'
        self.blueteamname = 'Blue' if self.bluenameentry.get() == '' else self.bluenameentry.get()
        self.bluenamelabel['text'] = self.blueteamname
        self.redteamname = 'Red' if self.rednameentry.get() == '' else self.rednameentry.get()
        self.rednamelabel['text'] = self.redteamname
        self.roundnum = int(self.roundentry.get() if digitaldetect(self.roundentry.get()) else 1)
        self.roundlabel['text'] = 'Round ' + str(self.round)
        self.minset = self.min = int(self.minentry.get() if digitaldetect(self.minentry.get()) else 0)
        self.secset = self.sec = int(self.secentry.get() if digitaldetect(self.secentry.get()) else 0)
        self.timerlabel['text'] = str(self.min) + ':' + str(self.sec)
        self.infoupdate()

    def reset(self):
        self.blueteamname = ''
        self.bluenamelabel['text'] = 'Blue'
        self.redteamname = ''
        self.rednamelabel['text'] = 'Red'
        self.count = False
        self.commited = False
        self.minset = 0
        self.secset = 0
        self.min = 0
        self.sec = 0
        self.timerlabel['text'] = str(self.min) + ':' + str(self.sec)
        self.bluescore = 0
        self.bluescorelabel['text'] = self.bluescore
        self.redscore = 0
        self.redscorelabel['text'] = self.redscore
        self.bluefoul = 0
        self.bluefoullabel['text'] = self.bluefoul
        self.redfoul = 0
        self.redfoullabel['text'] = self.redfoul
        self.roundnum = 0
        self.round = 1
        self.roundlabel['text'] = 'Round 1'
        self.commitbtn['state'] = 'normal'
        self.matchstopbtn['state'] = 'disabled'
        self.blue1btn['state'] = 'disabled'
        self.blue2btn['state'] = 'disabled'
        self.blue3btn['state'] = 'disabled'
        self.bluefoulbtn['state'] = 'disabled'
        self.red1btn['state'] = 'disabled'
        self.red2btn['state'] = 'disabled'
        self.red3btn['state'] = 'disabled'
        self.redfoulbtn['state'] = 'disabled'
        self.matchstartbtn['state'] = 'disable'
        self.matchstopbtn['state'] = 'disable'
        self.inforeset()

    def createinfowindow(self):
        self.infowindow = Frame(self)
        self.infowindow.grid(row=2, column=3)
        self.infolabel = Label(self.infowindow, font="Consolas 15 bold")
        self.infolabel.grid(row=0, column=0)
        self.blueinfo = Label(self.infowindow)
        self.blueinfo.grid(row=1, column=0)
        self.redinfo = Label(self.infowindow)
        self.redinfo.grid(row=2, column=0)
        self.roundinfo = Label(self.infowindow)
        self.roundinfo.grid(row=3, column=0)
        self.mininfo = Label(self.infowindow)
        self.mininfo.grid(row=4, column=0)
        self.secinfo = Label(self.infowindow)
        self.secinfo.grid(row=5, column=0)

    def infoupdate(self):
        self.infolabel['text'] = 'Info'
        self.blueinfo['text'] = 'Blue Team Name : ' + str(self.blueteamname)
        self.redinfo['text'] = 'Red Team Name : ' + str(self.redteamname)
        self.roundinfo['text'] = 'Rounds : ' + str(self.roundnum)
        self.mininfo['text'] = 'Min : ' + str(self.minset)
        self.secinfo['text'] = 'Sec : ' + str(self.secset)

    def inforeset(self):
        self.infolabel['text'] = ''
        self.blueinfo['text'] = ''
        self.redinfo['text'] = ''
        self.roundinfo['text'] = ''
        self.mininfo['text'] = ''
        self.secinfo['text'] = ''


root = Tk()
app = Application(root)
mainloop()
