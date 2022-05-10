# packages
from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
from tkmacosx import Button

# Hymns
import CIR
import HN
import TS
import PR
import KAG
import ONN
import AYH
import CIRShort
root = Tk()


#   Home Screen


copticFont = Font(family="CS Avva Shenouda", size=16)
englishFont = Font(family="Helvetica", size=15)

season = Label(root, text="Reserrection", fg="blue")
root.title("Coptic Hymns")
root.iconbitmap("/Users/John/Documents/PyApp/icon.ico")
root.geometry("1000x1000")
season.grid(row=0, column=0)
var = 0

ressurection1 = Button(root, text="Hiten ", font=copticFont, bg="black", fg="white", command=lambda: [HN.hiten()])
ressurection2 = Button(root, text="<ere Tef`anactacic", font=copticFont, bg="black", fg="white", command=lambda: [PR.praxisResponse()])
ressurection3 = Button(root, text="Kata ni,oroc", font=copticFont, bg="black", fg="white", command=lambda: [KAG.kataNiGreat()])
ressurection4 = Button(root, text="`W nim nai", font=copticFont, bg="black", fg="white", command=lambda: [ONN.oNimNai()])
ressurection5 = Button(root, text="Ni,oroc tyrou", font=copticFont, bg="black", fg="white", command=lambda: [AYH.AllYouHeavenly()])
ressurection6 = Button(root, text="`<rictoc `anecty (2)", font=copticFont, bg="black", fg="white", command=lambda: [CIRShort.KA()])
ressurection7 = Button(root, text="`<rictoc `anecty", font=copticFont, bg="black", fg="white", command=lambda: [CIR.KA()])
ressurection8 = Button(root, text="Ton cunanar,on ", font=copticFont, bg="black", fg="white", command=lambda: [TS.tonSeena()])

lineBreak = Label(text="\n")


myImg1 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img1Label = Label(image=myImg1)
img1Label.grid(row=1, column=0)
ressurection1.grid(row=2, column=0)

myImg2 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img2Label = Label(image=myImg1)
img2Label.grid(row=1, column=1)
ressurection2.grid(row=2, column=1)

myImg3 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img3Label = Label(image=myImg1)
img3Label.grid(row=1, column=2)
ressurection3.grid(row=2, column=2)

myImg4 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img4Label = Label(image=myImg4)
img4Label.grid(row=1, column=3)
ressurection4.grid(row=2, column=3)

myImg5 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img5Label = Label(image=myImg1)
img5Label.grid(row=1, column=4)
ressurection5.grid(row=2, column=4)

lineBreak.grid(row=3, column=0)
myImg6 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img6Label = Label(image=myImg1)
img6Label.grid(row=4, column=1)
ressurection6.grid(row=5, column=1)

myImg7 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img7Label = Label(image=myImg1)
img7Label.grid(row=4, column=0)
ressurection7.grid(row=5, column=0)

myImg8 = ImageTk.PhotoImage(Image.open("Imgs/resImg.jpeg"))
img8Label = Label(image=myImg1)
img8Label.grid(row=4, column=2)
ressurection8.grid(row=5, column=2)

root.mainloop()


