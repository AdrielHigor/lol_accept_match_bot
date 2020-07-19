from tkinter import*
import tkinter
import Pmw
try:
    from GameBot.LoL_bot.LolBot import *
except ModuleNotFoundError:
    from LolBot import *

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.commands = Commands()

        self.var = tkinter.StringVar()
        self.var.set('None')
        self.lanes = Pmw.OptionMenu(master,
                                          labelpos='w',
                                          label_text='Choose your lane:',
                                          menubutton_textvariable=self.var,
                                          items=['None','Top', 'Jg', 'Mid', 'Adc', 'Sup'],
                                          menubutton_width=10,
                                          )
        self.lanes.pack(anchor='w', padx=10, pady=10)

        self.txt1 = Label(text="Champion:")
        self.txt1.place(bordermode=OUTSIDE, height=None, width=None, x=10, y=60)

        self.champion = Entry()
        self.champion.place(bordermode=OUTSIDE, height=25, width=200, x=80, y=60)

        self.Iniciar = Button(text="Start", command=self.start)
        self.Iniciar.place(bordermode=OUTSIDE, height=30, width=96, x=100, y=100)

    def start(self):
        self.commands.searchButton()
        while True:
            if(self.commands.imgGrab() == 11500):
                self.commands.acceptButton()
                self.commands.searchButton()
            elif(self.commands.imgGrab() == 1200):
                break
        aux = 0
        while aux !=7:
            aux += 1
            self.commands.textField()
            self.commands.selectLane(self.lanes.getcurselection())
        self.commands.champSearch(self.champion.get())



root = Tk()
app = Application(master=root)
app.master.title("LOL Bot")
app.master.minsize(300, 150)
app.mainloop()
root.destroy()
