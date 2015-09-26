#!/usr/bin/python
__author__ = 'Ayush'

from tkinter import *
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import logging



class MetaDataMP3:
    def __init__(self, loc):
        try:
            self.audio = MP3(loc,ID3=EasyID3)
        except:
            root.destroy()
            newroot = Tk()
            newroot.title("Edit Metadata Error")
            newroot.geometry('400x100')
            Message(newroot,text="Invalid File Type!!!",width=400).pack(expand=YES,fill=X)
            newroot.mainloop()
        index = loc[::-1].index('/')
        index = len(loc) - index
        self.fn = loc[index:]
        self.src = loc
        try:
            self.artist = self.audio['artist'][0]
        except:
            self.artist = "Unknown"
        try:
            self.title = self.audio['title'][0]
        except:
            self.title = "Unknown"
        try:
            self.album = self.audio['album'][0]
        except:
            self.album = "Unknown"
        try:
            self.genre = self.audio['genre'][0]
        except:
            self.genre = "Unknown"


def save():
    file.audio["title"] = file.title  =  titlevar.get()
    file.audio["artist"] = file.artist  =  artistvar.get()
    file.audio["album"] = file.album  =  albumvar.get()
    file.audio["genre"] = file.genre  =  genrevar.get()
    file.audio.save()
    root.quit()

if __name__ == '__main__':
    root = Tk()

    file = MetaDataMP3(sys.argv[1])
    root.title("MetaData Edit: "+sys.argv[-1])

    titletag = Label(root,text="Title: ",anchor=E,width=10)
    artistag = Label(root,text="Artist: ",anchor=E,width=10)
    albumtag = Label(root,text="Album: ",anchor=E,width=10)
    genretag = Label(root,text="Genre: ",anchor=E,width=10)


    titlevar = StringVar()
    titlevar.set(file.title)
    entertitle = Entry(root,textvariable= titlevar,width=50)

    artistvar = StringVar()
    artistvar.set(file.artist)
    enterartist = Entry(root,textvariable= artistvar,width=50)

    albumvar = StringVar()
    albumvar.set(file.album)
    enteralbum = Entry(root,textvariable= albumvar,width=50)

    genrevar = StringVar()
    genrevar.set(file.genre)
    entergenre = Entry(root,textvariable= genrevar, width=50)

    titletag.grid(row=0)
    entertitle.grid(row=0,column=1)
    artistag.grid(row=1)
    enterartist.grid(row=1,column=1)
    albumtag.grid(row=2)
    enteralbum.grid(row=2,column=1)
    genretag.grid(row=3)
    entergenre.grid(row=3,column=1)

    ok = Button( root,text="Save",width=10,command = save)
    ok.grid(row=4,columnspan=2)

    root.mainloop()