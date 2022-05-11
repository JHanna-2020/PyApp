from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import pygame
import time
from mutagen.mp3 import MP3
pygame.mixer.init()

def AllYouHeavenly():
    global topImg
    global audio

    def audio():
        x = 1
        if x <= 1:
            aLabel = Label(res, text="\nAudio")
            aLabel.pack();
            song_list = Listbox(res, bg="#e9e9e9", width=60, borderwidth=0, height=5)
            song1 = "/Volumes/My Passport/Programming/Python/PyApp/audio/All you heavenly orders Ibrahim Ayad (Arabic).mp3"
            song1 = song1.replace("/Volumes/My Passport/Programming/Python/PyApp/audio/", "")
            song1 = song1.replace(".mp3", "")
            song2 = "/Volumes/My Passport/Programming/Python/PyApp/audio/All you heavenly orders St. Mark JC Deacons Partial (Arabic).mp3"
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

    res.title("Ya kol al sofoof")
    res.geometry("1500x1500")

    cHeading = Font(family="CS Avva Shenouda", size=20)
    englishFont = Font(family="Helvetica", size=11)
    eHeading = Font(family="Helvetica", size=20)
    copticFont = Font(family="CS Avva Shenouda", size=18)
    khristosanestee = Label(res,
                        text="+ Ya kol al sofoof al sama-eyeen,\n ratelo le-eelahena be naghamat el-tasbeeh,\n wabe-tahegoo ma'na al-yowma fareheen, \nbe-keyamat El-Sayed El-Maseeh. \n+ Al-yowma qud kamalat el-nobowat, \nwa qud tamat akwalol-aba'a el-awaleen, \nbe qeyamat El-Rabe men baynel-amwat,\n wa howa badol mod-tuge'een.\n+ Qud kamal-Rabo methlol-na-em,\n wa kal sa-mely men al-khamra,\n wa wahabana al-na-'eem el-da-em,\n wa 'atukna men al-‘obodeyatel-mora.\n+ Wa sabal-gahima sabian,\n wa hatama abwa-bahol-nohas,\n wa qassar mataresahol-hadida kasran,\n wa abdala lanal-'oqobata bel-khalas.\n+ Wa a'ada Adam elal-ferdos,\n be-farahen wa bahga wa mascara,\n howa wa banehe alzeena kano fel-hobos,\n mahalel na'em dof'a okhra.\n+ Alyawman-tasharat a'lamol khalas,\n wa tagadadat al-ag-sam wal-arwah,\n wafazal-moo-menona bel-safhee 'an el-qasas,\n wa magdo Allahe be-tasabehe wal-afrah.\n+ Alyawmab-tahagat ebnat Dawood,\n wa tahal-lalat qolobol-rosolel-ubrar,\n henama basharata-hom el-neswa be-tamam el-maw'ood,\n wa ma same'oho minal-mala-e-katel-ut-haar.\n+ Enna Yaso'al Masseha qud qam,\n laysa howa ha-hona kama taran,\n faza-habat el-neswa wa basharat-talamezahol-keram,\n be-qeiamat khaleq el-baraiah ag-ma'en.\n+ Wa zahar le-talamezaho wa-ab-hagahom,\n be-bahaa nazaroho motagal-leian,\n be-magde laho-taho wa af-rahom,\n lamma shaha-doho hayyan.\n+ Nosabeha-ho wa nozed ref-'ataho,\n wa na'-taref be-magde qeya-matehe,\n wa nash-koroho 'ala 'azeme ne'-matehe,\n le-an elal-abadee rah-matehe.", font=englishFont)
    kaHeading = Label(res, text="Ya kol al sofoof", font=eHeading)
    topImg = ImageTk.PhotoImage(Image.open("pic.png"))
    topLab = Label(res, image=topImg)
    topLab.pack()
    greek = Label(res, text="Coptic")
    english = Label(res, text="English")
    kaHeading.pack()



    khristosanestee.pack()


    audio()
