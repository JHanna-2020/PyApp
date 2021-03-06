from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import pygame
import time
from mutagen.mp3 import MP3

pygame.mixer.init()

def tonSeena():
    var=2
    global topImg
    global audio

    def audio():
        x = 1
        if x <= 1:
            aLabel = Label(res, text="\nAudio")
            aLabel.pack();
            song_list = Listbox(res, bg="#e9e9e9", width=60, borderwidth=0, height=5)
            song1 = "/Volumes/My Passport/Programming/Python/PyApp/audio/Ton Sina Ibrahim Ayad.mp3"
            song1 = song1.replace("/Volumes/My Passport/Programming/Python/PyApp/audio/", "")
            song1 = song1.replace(".mp3", "")
            song2 = "/Volumes/My Passport/Programming/Python/PyApp/audio/Ton Sina St. Mark JC Deacons.mp3"
            song2 = song2.replace("/Volumes/My Passport/Programming/Python/PyApp/audio/", "")
            song2 = song2.replace(".mp3", "")

            def song_length():
                current_time = pygame.mixer.music.get_pos() / 1000
                mins_time = time.strftime('%M:%S', time.gmtime(current_time))

                statusBar.after(1000, song_length)

                current_song = song_list.curselection()
                song = song_list.get(current_song)
                song = f'/Users/John/Documents/PyApp/audio/{song}.mp3'
                song_mut = MP3(song)
                song_time = song_mut.info.length
                song_total = time.strftime('%M:%S', time.gmtime(song_time))

                statusBar.config(text=f'{mins_time}/{song_total}')

            def play():
                song = song_list.get(ACTIVE)
                song = f'/Users/John/Documents/PyApp/audio/{song}.mp3'
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
                song = f'/Users/John/Documents/PyApp/audio/{song}.mp3'
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(loops=0)
                song_list.selection_clear(0, END)
                song_list.activate(next_one)
                song_list.selection_set(next_one, last=None)

            def previous_song():
                next_one = song_list.curselection()
                next_one = next_one[0] - 1
                song = song_list.get(next_one)
                song = f'/Users/John/Documents/PyApp/audio/{song}.mp3'
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(loops=0)
                song_list.selection_clear(0, END)
                song_list.activate(next_one)
                song_list.selection_set(next_one, last=None)

            song_list.insert(END, song1)
            song_list.insert(END, song2)
            song_list.pack()
            backBtn = Button(res, text="???", borderwidth=0, command=previous_song)
            playBtn = Button(res, text="??????", borderwidth=0, command=play)
            pauseBtn = Button(res, text="??????", borderwidth=0, command=lambda: pause(paused))
            forwardBtn = Button(res, text="??????", borderwidth=0, command=next_song)
            stopBtn = Button(res, text="??????", borderwidth=0, command=stop)
            statusBar = Label(res, text='00:00/00:00', bd=1, relief=GROOVE, anchor=E, bg="white", fg="black")
            statusBar.pack(ipady=2)
            backBtn.pack()
            playBtn.pack()
            pauseBtn.pack()
            forwardBtn.pack()
            stopBtn.pack()

    res = Toplevel()

    res.title("Ton Seena Narkhon")
    res.geometry("1500x1500")

    cHeading = Font(family="CS Avva Shenouda", size=20)
    englishFont = Font(family="Helvetica", size=15)
    copticFont = Font(family="CS Avva Shenouda", size=18)
    khristosanestee = Label(res,
                            text="Ton cunanar,on Logon Patri ke `Pneumati@\n ton ek par;enou te,;enta ic cwtyrian `ymon@ \n`anumnycwmen picti ke `prockunycwmen@ \n`oti yudokyce carki@ \n`anel;in en tw `ctauro@ ke ;anaton `upomine@ \nke `egire touc te;ne`w`o@ tac en ty endoxw `Anactaci autou.",
                            font=copticFont)
    english_KA = Label(res,
                       text="We the believers hymn and worship the Logos, \nwithout beginning with the Father and the Spirit,\n having been born of a virgin for our salvation,\n for He appeared in the flesh to ascend on the Cross.\n He persevered unto death and raised the dead through His glorious Resurrection.\n Ton seena-narkhon Loghon Patri kep-nevmati, \nton ek-partheno-tek-thenta ies sotee-reian emmon, \nanim-ne-somen pisti kep-ros-ke-ni-somen, \no-ti ev-zokee se sarkee, \nanil-theen entos-tavro ke thanton ee-pomene, \nke ee-giri tos teth-ne-o-oo, \ntas enti en-zoxso anastasi avto.",
                       font=englishFont)

    kaHeading = Label(res, text="Ton cunanar,on", font=cHeading)
    topImg = ImageTk.PhotoImage(Image.open("pic.png"))
    topLab = Label(res, image=topImg)
    topLab.pack()
    greek = Label(res, text="Greek")
    english = Label(res, text="English")
    kaHeading.pack()
    greek.pack()
    khristosanestee.pack()
    english.pack()

    english_KA.pack()
    audio()
