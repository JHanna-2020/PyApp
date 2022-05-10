from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import pygame
import time
from mutagen.mp3 import MP3

pygame.mixer.init()

def kataNiGreat():
    var = 2
    global topImg
    global audio

    def audio():
        x = 1
        if x <= 1:
            aLabel = Label(res, text="\nAudio")
            aLabel.pack();
            song_list = Listbox(res, bg="#e9e9e9", width=60, borderwidth=0, height=5)
            song1 = "/Volumes/My Passport/Programming/Python/PyApp/audio/Kata Ni Khoros (Great) Ibrahim Ayad.mp3"
            song1 = song1.replace("/Volumes/My Passport/Programming/Python/PyApp/audio/", "")
            song1 = song1.replace(".mp3", "")
            song2 = "/Volumes/My Passport/Programming/Python/PyApp/audio/Kata Nikhoros (Great) Farag Abdelmessih.mp3"
            song2 = song2.replace("/Volumes/My Passport/Programming/Python/PyApp/audio/", "")
            song2 = song2.replace(".mp3", "")

            def song_length():
                current_time = pygame.mixer.music.get_pos() / 1000
                mins_time = time.strftime('%M:%S', time.gmtime(current_time))

                statusBar.after(1000, song_length)

                current_song = song_list.curselection()
                song = song_list.get(current_song)
                song = f'/Volumes/My Passport/Programming/Python/PyApp/audio/{song}.mp3'
                song_mut = MP3(song)
                song_time = song_mut.info.length
                song_total = time.strftime('%M:%S', time.gmtime(song_time))

                statusBar.config(text=f'{mins_time}/{song_total}')

            def play():
                song = song_list.get(ACTIVE)
                song = f'/Volumes/My Passport/Programming/Python/PyApp/audio/{song}.mp3'
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(loops=0)
                song_length()

            def stop():
                pygame.mixer.music.stop()
                song_list.selection_clear(ACTIVE)

            global paused
            paused = False

            def pause(is_paused):
                global paused
                paused = is_paused
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

            def next_song():
                next_one = song_list.curselection()
                next_one = next_one[0] + 1
                song = song_list.get(next_one)
                song = f'/Volumes/My Passport/Programming/Python/PyApp/audio/{song}.mp3'
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(loops=0)
                song_list.selection_clear(0, END)
                song_list.activate(next_one)
                song_list.selection_set(next_one, last=None)

            def previous_song():
                next_one = song_list.curselection()
                next_one = next_one[0] - 1
                song = song_list.get(next_one)
                song = f'/Volumes/My Passport/Programming/Python/PyApp/audio/{song}.mp3'
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(loops=0)
                song_list.selection_clear(0, END)
                song_list.activate(next_one)
                song_list.selection_set(next_one, last=None)

            song_list.insert(END, song1)
            song_list.insert(END, song2)
            song_list.pack()
            backBtn = Button(res, text="⏪", borderwidth=0, command=previous_song)
            playBtn = Button(res, text="▶️", borderwidth=0, command=play)
            pauseBtn = Button(res, text="⏸️", borderwidth=0, command=lambda: pause(paused))
            forwardBtn = Button(res, text="⏩️", borderwidth=0, command=next_song)
            stopBtn = Button(res, text="⏹️", borderwidth=0, command=stop)
            statusBar = Label(res, text='00:00/00:00', bd=1, relief=GROOVE, anchor=E, bg="white", fg="black")
            statusBar.pack(ipady=2)
            backBtn.pack()
            playBtn.pack()
            pauseBtn.pack()
            forwardBtn.pack()
            stopBtn.pack()

    res = Toplevel()

    res.title("Kata Ni Khrous")
    res.geometry("1500x1500")

    cHeading = Font(family="CS Avva Shenouda", size=20)
    englishFont = Font(family="Helvetica", size=15)
    copticFont = Font(family="CS Avva Shenouda", size=18)
    khristosanestee = Label(res,
                            text="Kata ni,oroc `e]cwtem `erwou@ (`w nim naicumvwnia)=g e;nyou `enamasj. \nP=,=c aftwnf `ebol qen nye;mwout@ `nswrp `m`vouai `nte nicabbaton.\n Nimatoi `mper je me;nouj@ qa `T`anactacic `mPencwtyr@ qen pi`ehoou `nte }kuriaky.", font=copticFont)
    english_KA = Label(res,
                       text="All the choirs that I hear. (Oh what are these symphonies)3 that are coming to my ears! \n Christ rose from the dead, early on one Sunday.\n O soldiers, lie not about the Resurrection of our Savior on the Lord’s Day (Sunday).", font=englishFont)

    kaHeading = Label(res, text="Kata ni,oroc", font=cHeading)
    topImg = ImageTk.PhotoImage(Image.open("pic.png"))
    topLab = Label(res, image=topImg)
    topLab.pack()
    greek = Label(res, text="Coptic")
    english = Label(res, text="English")
    kaHeading.pack()
    greek.pack()
    khristosanestee.pack()
    english.pack()

    english_KA.pack()
    audio()
