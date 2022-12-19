from tkinter import*
import time

def Main():
    global root
    root = Tk()
    root.title('Stopwatch made b @Tahamidur Taief')
    width  = 500
    hight = 200
    screen_width = root.winfo_screenwidth()
    screen_hight = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_hight / 2) - (hight / 2)
    root.geometry('%dx%d+%d+%d' % (width, hight, x, y))
    top = Frame(root, width=400)
    top.pack(side=TOP)
    stopwatch=Stopwatch(root)
    stopwatch.pack(side=top)
    Buttom = Frame(root, width=400)
    Buttom.pack(side=BOTTOM)
    Start =  Button(BOTTOM, text='START', command=stopwatch.Start, width=10, hight= 3)
    Start.pack(side=LEFT)

    Stop = Button(BOTTOM, text='STOP', command=stopwatch.stop, width=10, hight= 3)
    Stop.pack(side=LEFT)

    Reset = Button(BOTTOM, text='RESET', command=stopwatch.Reset, width=10, hight= 3)
    Reset.pack(side=LEFT)

    Exit = Button(BOTTOM, text='EXIT', command=stopwatch.Exit, width=10, hight= 3)
    Exit.pack(side=LEFT)

    Title = Label(TOP, text='Stopwatch @T R T', font=('arial', 24), fg = 'white', g='black')
    Title.pack(fill = x)

    root.config(bg='sky')



class Stopwatch(Frame):

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=('times new roman', 45), fg='white', bg='black')
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=5, padx=10)

    def updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.time = self.after(50, self.updater)

    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d'% (minutes, seconds, miliSeconds))

    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 0

    def stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.start
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Exit(self):
        root.destroy()
        exit()

    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)

if __name__ == '__Main__':
    Main()

root.mainloop()