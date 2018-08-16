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
#import multiprocessing
from tkinter import *
from PIL import Image, ImageTk

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
            closeButton.place(x=220, y=100)

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
            file.add_command(label='File Source', command=self.callback)
            file.add_command(label='Exit', command=self.client_exit)
            menu.add_cascade(label='File', menu=file)

            options = Menu(menu, tearoff = 0)
            options.add_command(label='Will be added soon')
            menu.add_cascade(label='Options', menu=options)

            about = Menu(menu, tearoff = 0)
            about.add_command(label='Report Bug', command=self.issues)
            about.add_command(label='My Discord', command=self.mydiscord)
            about.add_command(label='Reiswitched Discord', command=self.reidiscord)
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
#os.system ("CLS")

#Tk Frame         
class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("DownloadHost GUI")

        self.pack(fill=BOTH, expand=1)

        self.downloadButton = Button(self, text="Download", command=self.download_function)
        self.downloadButton.place(x=150, y=100)

        self.exitButton = Button(self, text="Cancel", command=self.client_exit)
        self.exitButton.place(x=290, y=100)

        text = Label(self, text="Unofficial ReiNX SD Stash Updater", font='Helvetica 18 bold')
        text.pack()
        self.text1 = Label(self, text="\nThe latest version of Darth Meteos' Super Special SD Stash is " + ver + ".\nWould you like to download it?")
        self.text1.pack()

        load = Image.open(os.getcwd() + '\\resources\\reinx.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=155)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu, tearoff = 0)
        file.add_command(label='File Source', command=self.callback)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        options = Menu(menu, tearoff = 0)
        options.add_command(label='Will be added soon')
        menu.add_cascade(label='Options', menu=options)

        about = Menu(menu, tearoff = 0)
        about.add_command(label='Report Bug', command=self.issues)
        about.add_command(label='My Discord', command=self.mydiscord)
        about.add_command(label='Reiswitched Discord', command=self.reidiscord)
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
        f.close()
        filename = os.getcwd() + '\\resources\\data.txt'
        filename2 = os.getcwd() + '\\resources\\data2.txt'
        os.remove(filename)
        os.remove(filename2)
        exit()

    

    def download_function(self):
        #self.worker
        winsound.PlaySound('resources\dl.wav', winsound.SND_ASYNC)
        root.withdraw()
        os.system('python DownloadHostExt.py &')
        #text = Label(self, text='\n         Download has completed       ', font='Helvetica 18 bold')
        #text.pack()
        winsound.PlaySound('resources\start.wav', winsound.SND_ASYNC)
        self.downloadButton.place_forget()
        self.exitButton.place_forget()
        self.text1.pack_forget()
        text2 = Label(self, text="\nThe latest version of Darth Meteos' Super Special SD Stash is " + ver + ".\nDownload has completed!")
        text2.pack()
        closeButton = Button(self, text="Close", command=self.client_exit)
        closeButton.place(x=220, y=100)
        root.deiconify()
        

    '''def worker(self):
        if __name__ == "__main__":
            files = ["DownloadHost GUI.py", "DownloadHostExt.py"]
        for i in files:
            p = multiprocessing.Process(target=worker, args=(i,))
            p.start()'''

        
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
root.iconbitmap(os.getcwd() + '\\resources\\reinx.ico')
root.geometry("490x430")

app = Window(root)


root.mainloop()

f.close()
filename = os.getcwd() + '\\resources\\data.txt'
filename2 = os.getcwd() + '\\resources\\data2.txt'
os.remove(filename)
os.remove(filename2)
exit()


