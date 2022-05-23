# Imports
import os
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog

app = Tk()
app.title('YT Downloader')
# Assets
image_fundo = PhotoImage(
    file='D:\PROJETOS\TkinterGUI\YTloader\FundoImage.png')

# Func
fundo = Label(app, image=image_fundo)
fundo.pack()


def Widgets():
    link = Entry(
        width=75,
        textvariable=V_Link
    ).place(relx=0.19, rely=0.2877)

    download_path = Entry(
        width=56,
        textvariable=D_path
    ).place(relx=0.19, rely=0.492)

    browse_B = Button(
        text='Browse',
        fg='#ffffff',
        command=Browse,
        width=13,
        height=2,
        bg='#737373'
    ).place(relx=0.7844, rely=0.463)

    download_B = Button(
        text='Download',
        fg='#ffffff',
        command=Download,
        width=19,
        height=2,
        bg='#161C40'
    ).place(relx=.3822, rely=0.733)


def Browse():
    direct = filedialog.askdirectory(
        initialdir="Your directory Path"
    )

    D_path.set(direct)


def Download():
    YT_link = V_Link.get()
    folder = D_path.get()
    getVideo = YouTube(YT_link)
    vdStream = getVideo.streams.filter(only_audio=True).first()

    try:
        video = vdStream.download(folder)

        base, ext = os.path.splitext(video)
        nFile = base + '.mp3'
        os.rename(video, nFile)

        messagebox.showinfo('DOWNLOADED', 'Arquivo baixado com sucesso\n'
                            + folder)

    except FileExistsError as Erro:
        os.remove(video)
        messagebox.showerror('ERRO',
                             '''Não foi possível baixar o arquivo pois o mesmo ja existe neste local !!''')


# Configs
V_Link = StringVar()
D_path = StringVar()

app.geometry('600x290')
app.resizable(False, False)


Widgets()

app.mainloop()
