import time
import sys

#Credit to Bob for this next statement 
# Check that user is using Python 3
if (sys.version_info > (3, 5)):
    # Python 3 code in this block
    pass
else:
    # Python 2 code in this block
    print("\n\nError - Application launched with Python 3.4 or lower, please install the latest Python, and rename this back to a .pyw.\n")
    time.sleep(1000)
    sys.exit()

import requests
import urllib.request
import urllib.parse
import urllib.error
import re
import os
import webbrowser
import winsound
import shutil
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

global dirdel
global zipdel

regex = r'('

    # Scheme (HTTP, HTTPS, FTP and SFTP):
regex += r'(?:(https?|s?ftp):\/\/)?'

    # www:
regex += r'(?:www\.)?'

regex += r'('

    # Host and domain (including ccSLD):
regex += r'(?:(?:[A-Z0-9][A-Z0-9-]{0,61}[A-Z0-9]\.)+)'

    # TLD:
regex += r'([A-Z]{2,6})'

    # IP Address:
regex += r'|(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

regex += r')'

    # Port:
regex += r'(?::(\d{1,5}))?'

    # Query path:
regex += r'(?:(\/\S+)*)'

regex += r')'      
        
print("If you are seeing this, you renamed this file to a .py. Congrats, you discovered an easter egg. Good job. I am proud of you. Join my discord found in the about tab in this program, and DM me to claim your prize.")

#HTML Parsing Function
try:
    url = "https://docs.google.com/document/d/1qDluUCn5zp1XtjCryjCUeaDKo4BzIPEGrq4VgnlPyNE/view"
    values = {}
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') # data should be bytes
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
    saveFile = open('resources\data.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except:
    winsound.PlaySound('resources\start.wav', winsound.SND_ASYNC)
    class Window(Frame):

        def __init__(self, master = None):
            Frame.__init__(self, master)
            self.master = master
            self.init_window()

        def init_window(self):

            self.master.title("DownloadHost GUI")

            self.pack(fill=BOTH, expand=1)

            closeButton = Button(self, text="Close", command=self.client_exit)
            closeButton.place(x=200, y=100)

            text = Label(self, text="Unofficial ReiNX SD Stash Updater", font='Helvetica 18 bold')
            text.pack()
            self.text1 = Label(self, text="\nThere is no internet connection. Retry with an active internet connection.")
            self.text1.pack()

            load = Image.open(os.getcwd() + '\\resources\\reinx.png')
            render = ImageTk.PhotoImage(load)

            img = Label(self, image=render)
            img.image = render
            img.place(x=0,y=155)

            menu = Menu(self.master)
            self.master.config(menu=menu)

            file = Menu(menu, tearoff = 0)
            file.add_command(label='Error')
            menu.add_cascade(label='File', menu=file)

            options = Menu(menu, tearoff = 0)
            options.add_command(label='Error')
            menu.add_cascade(label='Options', menu=options)

            about = Menu(menu, tearoff = 0)
            about.add_command(label='Error')
            menu.add_cascade(label='About', menu=about)

        def showImg(self):
            load = Image.open(os.getcwd() + '\\resources\\reinx.png')
            render = ImageTk.PhotoImage(load)

            img = Label(self, image=render)
            img.image = render
            img.place(x=0,y=155)

        def callback(self):
            webbrowser.open_new(r"https://docs.google.com/document/d/1qDluUCn5zp1XtjCryjCUeaDKo4BzIPEGrq4VgnlPyNE/view")

        def issues(self):
            webbrowser.open_new(r"https://github.com/lunalik2/Unofficial-ReiNX-SD-Stash-Updater/issues")

        def mydiscord(self):
            webbrowser.open_new(r"https://discord.gg/KFf4v6t")

        def reidiscord(self):
            webbrowser.open_new(r"https://discord.gg/NxpeNwz")
       
    
        def client_exit(self):
            exit()
        


    root = Tk()
    root.title("wm min/max")
    root.resizable(0,0)
    root.iconbitmap(os.getcwd() + '\\resources\\reinx.ico')
    root.geometry("490x430")

    app = Window(root)


    root.mainloop()

    

infile = "resources\data.txt"
outfile = "resources\data2.txt"

delete_list = ["https://docs.google.com/document/d/", "https://lh4.googleusercontent.com/cExJiMXYxY501RVXRqxPDsCkH1kbjUNvL0693SUJomHZr_TQ6hV", '"><meta',]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

f = open('resources\data2.txt','r')
message = f.read()
string = (message)
f.close()

find_urls_in_string = re.compile(regex, re.IGNORECASE)
url = find_urls_in_string.search(string)


if url is not None and url.group(0) is not None:
       url = url.group(0).strip()
ver = url[-6:]
if ver[-1:] is "0":
            ver = ver[:4]
            
winsound.PlaySound('resources\start.wav', winsound.SND_ASYNC)

#Tk Frame         
class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("DownloadHost GUI")

        self.pack(fill=BOTH, expand=1)

        f = open('resources\config.txt','r')
        config1 = f.read()
        config = config1
        print(config)
        if config[:1] is "1":
            dirdel = "false"
            dirdel1 = "Enable Delete SD Stash Folder"
        else:
            dirdel = "true"
            dirdel1 = "Disable Delete SD Stash Folder"
        if config[1:] is "1":
            zipdel = "false"
            zipdel1 = "Enable Delete SD Stash Zip"
        else:
            zipdel = "true"
            zipdel1 = "Disable Delete SD Stash Zip"
        
        self.downloadButton = Button(self, text="Download", command=self.download_function)
        self.downloadButton.place(x=140, y=100)

        self.exitButton = Button(self, text="Cancel", command=self.client_exit)
        self.exitButton.place(x=280, y=100)

        text = Label(self, text="Unofficial ReiNX SD Stash Updater", font='Helvetica 18 bold')
        text.pack()
        self.text1 = Label(self, text="\nThe latest version of Darth Meteos' Super Special SD Stash is " + ver + ".")
        self.text1.pack()
        self.text2 = Label(self, text="Would you like to download it?")
        self.text2.pack()
        text3 = Label(self, text="Program by Lunalik, ReiNX by the Reiswitched Team")
        text3.config(font=("Courier", 7))
        text3.place(x=230, y=135)

        load = Image.open(os.getcwd() + '\\resources\\reinx.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=155)

        self.menubar = Menu(self.master)

        self.file = Menu(self.menubar, tearoff = 0)
        self.file.add_command(label='File Source', command=self.callback)
        self.file.add_command(label='Exit', command=self.client_exit)
        self.menubar.add_cascade(label='File', menu=self.file)

        self.options = Menu(self.menubar, tearoff = 0)
        self.options.add_command(label=dirdel1, command=self.dir_toggle)
        self.options.add_command(label=zipdel1, command=self.zip_toggle)
        self.menubar.add_cascade(label='Options', menu=self.options)

        self.tools = Menu(self.menubar, tearoff = 0)
        self.tools.add_command(label='ReiNX Custom Splash Script', command=self.splash)
        self.menubar.add_cascade(label='Tools', menu=self.tools)

        self.about = Menu(self.menubar, tearoff = 0)
        self.about.add_command(label='Report Bug', command=self.issues)
        self.about.add_command(label='My Discord', command=self.mydiscord)
        self.about.add_command(label='Reiswitched Discord', command=self.reidiscord)
        self.menubar.add_cascade(label='About', menu=self.about)

        self.master.config(menu=self.menubar)

    def splash(self):
        winsound.PlaySound('resources\dl.wav', winsound.SND_ASYNC)
        root.withdraw()
        os.system('python CustomSplash.pyw &')
        winsound.PlaySound('resources\start.wav', winsound.SND_ASYNC)
        root.deiconify()

    def dir_toggle(self):
        f = open('resources\config.txt','r')
        config1 = f.read()
        f.close()
        f = open('resources\config.txt','w')
        config = config1
        if config[:1] is "1":
            config2 = str("2") + str(config[1:])
            print(config2)
            f.write(str(config2))
            dirdel = "true"
            dirdel1 = "Disable Delete SD Stash Folder"
            self.options.entryconfig(0, label="Disable Delete SD Stash Folder")
            
        else:
            config2 = str("1") + str(config[1:])
            print(config2)
            f.write(str(config2))
            dirdel = "false"
            dirdel1 = "Enable Delete SD Stash Folder"
            self.options.entryconfig(0, label="Enable Delete SD Stash Folder")

    def zip_toggle(self):
        f = open('resources\config.txt','r')
        config1 = f.read()
        f.close()
        f = open('resources\config.txt','w')
        config = config1
        if config[1:] is "1":
            config2 =  str(config[:1]) + str("2")
            print(config2)
            f.write(str(config2))
            zipdel = "true"
            zipdel1 = "Disable Delete SD Stash Zip"
            self.options.entryconfig(1, label="Disable Delete SD Stash Zip")
            
        else:
            config2 = str(config[:1]) + str("1")
            print(config2)
            f.write(str(config2))
            dirdel = "false"
            dirdel1 = "Enable Delete SD Stash Zip"
            self.options.entryconfig(1, label="Enable Delete SD Stash Zip")
        
    def callback(self):
        webbrowser.open_new(r"https://docs.google.com/document/d/1qDluUCn5zp1XtjCryjCUeaDKo4BzIPEGrq4VgnlPyNE/view")

    def issues(self):
        webbrowser.open_new(r"https://github.com/lunalik2/Unofficial-ReiNX-SD-Stash-Updater/issues")

    def mydiscord(self):
        webbrowser.open_new(r"https://discord.gg/KFf4v6t")

    def reidiscord(self):
        webbrowser.open_new(r"https://discord.gg/NxpeNwz")
       
    
    def client_exit(self):
        f.close()
        filename = os.getcwd() + '\\resources\\data.txt'
        filename2 = os.getcwd() + '\\resources\\data2.txt'
        os.remove(filename)
        os.remove(filename2)
        exit()

    

    def download_function(self):
        winsound.PlaySound('resources\dl.wav', winsound.SND_ASYNC)
        root.withdraw()
        os.system('python DownloadHostExt.py &')
        winsound.PlaySound('resources\start.wav', winsound.SND_ASYNC)
        self.downloadButton.place_forget()
        self.exitButton.place_forget()
        self.text2.pack_forget()
        text3 = Label(self, text="Download has completed!")
        text3.pack()
        closeButton = Button(self, text="Close", command=self.client_exit)
        closeButton.place(x=200, y=100)
        f = open('resources\config.txt','r')
        config1 = f.read()
        config = config1
        print(config)
        if config[:1] is "1":
            dirdel = "false"
        else:
            dirdel = "true"
        if config[1:] is "1":
            zipdel = "false"
        else:
            zipdel = "true"
        if dirdel is 'true':
            shutil.rmtree(os.getcwd() + "\\Darth Meteos' Super Special SD Stash " + ver)
        if zipdel is 'true':
            os.remove(os.getcwd() + "\\Darth Meteos' Super Special SD Stash " + ver + ".zip")
        root.deiconify()

        
import atexit
@atexit.register
def exit1():
        f.close()
        filename = os.getcwd() + '\\resources\\data.txt'
        filename2 = os.getcwd() + '\\resources\\data2.txt'
        os.remove(filename)
        os.remove(filename2)
        exit()

root = Tk()
root.title("wm min/max")
root.resizable(0,0)
root.iconbitmap(os.getcwd() + '\\resources\\reinx.ico')
root.geometry("490x450")

app = Window(root)


    

root.mainloop()

f.close()
filename = os.getcwd() + '\\resources\\data.txt'
filename2 = os.getcwd() + '\\resources\\data2.txt'
os.remove(filename)
os.remove(filename2)
exit()


