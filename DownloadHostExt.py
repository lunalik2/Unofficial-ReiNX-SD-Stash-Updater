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
import urllib.request
import urllib.parse
import urllib.error
import re
import os
import winsound
from tkinter import *
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

#print("\n\nDone\n")

#winsound.PlaySound('resources\start.wav', winsound.SND_ASYNC)

'''class Window(Frame):

    def __init__(self, child = None):
        Frame.__init__(self, child)
        self.child = child
        self.init_window()

    def init_window(self):

        self.child.title("")

        self.pack(fill=BOTH, expand=1)

        

        exitButton = Button(self, text="Ok", command=self.client_exit)
        exitButton.place(x=100, y=20)

        text = Label(self, text="Download complete")
        text.pack()
        

        

        menu = Menu(self.child)
        self.child.config(menu=menu)


       
    
    def client_exit(self):
        exit()

        

root = Tk()
root.geometry("150x30")

app = Window(root)


root.mainloop()'''
exit()
