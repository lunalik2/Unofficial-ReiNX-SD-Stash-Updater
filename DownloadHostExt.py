import sys
import time

#Credit to Bob for this next statement 
# Check that user is using Python 3
if (sys.version_info > (3, 5)):
    # Python 3 code in this block
    pass
else:
    # Python 2 code in this block
    print("\n\nError - Application launched with Python 3.4 or lower, please install the latest Python.\n")
    time.sleep(5)
    sys.exit()
    
import requests
import zipfile
import urllib.request
import urllib.parse
import urllib.error
import re
import os
import winsound
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file
from pathlib import Path

try:
    url = "https://www.google.com"
    urllib.request.urlopen(url)
except:
       print("No internet connection found :(\nTry again with an active connection.")
       time.sleep(2)
       exit()


my_file = Path("resources/data2.txt")
if not my_file.is_file():
       print("Launch DownloadHost GUI.pyw.")
       time.sleep(2)
       exit()
       
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

f = open('resources\data2.txt','r')
message = f.read()
string = (message)

find_urls_in_string = re.compile(regex, re.IGNORECASE)
url = find_urls_in_string.search(string)

if url is not None and url.group(0) is not None:
       url = url.group(0).strip()
ver = url[-6:]
if ver[-1:] is "0":
            ver = ver[:4]

os.system ("CLS")            
           
link = url
file_name = "Darth Meteos' Super Special SD Stash " + ver + ".zip"
with open(file_name, "wb") as f:
        print ("Downloading %s" % file_name + '\n')
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
                f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()

print("\n\nDone")
path = os.getcwd() + "\\Darth Meteos' Super Special SD Stash " + ver + ".zip"
path2 = os.getcwd() + "\\Darth Meteos' Super Special SD Stash "
zip_ref = zipfile.ZipFile(path, 'r')
zip_ref.extractall(path2 + ver)
zip_ref.close()

winsound.PlaySound('resources\warn.wav', winsound.SND_ASYNC)

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("DownloadHost GUI")

        self.pack(fill=BOTH, expand=1)

    
    
        button2 = Button(self, text="No", command=self.client_exit)
        button2.place(x=200, y=30)
        button1 = Button(self, text="Yes", command=self.browse_button)
        button1.place(x=100, y=30)

    def browse_button(self):
    # Allow user to select a directory and store it in global var
    # called folder_path
        global folder_path
        filename = filedialog.askdirectory(title = "Select the root of your SD card")
        folder_path.set(str(filename))
        if os.path.exists(filename):
            fromDirectory = os.getcwd() + "/Darth Meteos' Super Special SD Stash " + ver + "/SD Files"
            toDirectory = filename
            copy_tree(fromDirectory, toDirectory)
            fromDirectory = os.getcwd() + "/Darth Meteos' Super Special SD Stash " + ver + "/ReiNX.bin"
            toDirectory = os.getcwd()
            copy_file(fromDirectory, toDirectory)
            fromDirectory = os.getcwd() + "/Darth Meteos' Super Special SD Stash " + ver + "/README.txt"
            toDirectory = os.getcwd()
            copy_file(fromDirectory, toDirectory)
            exit()
        

    def client_exit(self):
        exit()

root = Tk()
root.geometry("300x100")
root.title("wm min/max")
root.resizable(0,0)
root.iconbitmap(os.getcwd() + '\\resources\\transparent.ico')
folder_path = StringVar()
lbl2 = Label(text="\nWould you like to place the files on your SD card?")
lbl2.pack()
app = Window(root)

root.mainloop()
