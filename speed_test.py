from tkinter import *

import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    # convert mbps
    down = str(round(sp.download()/(10**6), 3))+" Mbps"
    up = str(round(sp.upload()/(10**6), 3))+" Mbps"

    labdownspeed.config(text=down)
    labupspeed.config(text=up)


sp = Tk()
sp.title("Internet Speed")

sp.geometry("500x500")
sp.config(bg='green')

lab = Label(sp, text="Internet Speed Test",
            font=("Time New Roman", 33, "bold"), bg='green', fg='white')
lab.place(x=40, y=40)

labdown = Label(sp, text="download Speed",
                font=("Time New Roman", 20, "bold"), bg='green', fg='black')
labdown.place(x=120, y=100)

labdownspeed = Label(sp, text="00",
                     font=("Time New Roman", 20, "bold"), bg='green', fg='black')
labdownspeed.place(x=220, y=150)


labup = Label(sp, text="upload Speed",
              font=("Time New Roman", 20, "bold"), bg='green', fg='black')
labup.place(x=150, y=200)

labupspeed = Label(sp, text="00",
                   font=("Time New Roman", 20, "bold"), bg='green', fg='black')
labupspeed.place(x=220, y=250)


button = Button(sp, text="check Speed", font=(
    'Times New Roman', 30, 'bold'), relief=RAISED, bg='yellow', command=speedcheck)
button.place(x=120, y=300)


sp.mainloop()
