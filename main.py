from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font

import CIR
import HN
import TS
import PR

root = Tk()


#   Home Screen


copticFont = Font(family="CS Avva Shenouda", size=20)

season = Label(root, text="Reserrection", fg="blue")
root.title("Coptic Hymns")
root.iconbitmap("/Users/John/Documents/PyApp/icon.ico")
root.geometry("1000x1000")
season.grid(row=0, column=0)
var = 0

ressurection1 = Button(root, text="`<rictoc `anecty", font=copticFont, command=lambda: [CIR.KA()])
ressurection2 = Button(root, text="Ton cunanar,on ", font=copticFont, command=lambda: [TS.tonSeena()])
ressurection3 = Button(root, text="Hiten ", font=copticFont, command=lambda: [HN.hiten()])
ressurection4 = Button(root, text="<ere Tef`anactacic", font=copticFont, command=lambda: [PR.praxisResponse()])

myImg4 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img4Label = Label(image=myImg4)
img4Label.grid(row=1, column=0)
ressurection4.grid(row=2, column=1)


myImg1 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img1Label = Label(image=myImg1)
img1Label.grid(row=1, column=1)
ressurection1.grid(row=2, column=2)

myImg2 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img2Label = Label(image=myImg1)
img2Label.grid(row=1, column=2)
ressurection2.grid(row=2, column=3)

myImg3 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img3Label = Label(image=myImg1)
img3Label.grid(row=1, column=3)
ressurection3.grid(row=2, column=0)
root.mainloop()
