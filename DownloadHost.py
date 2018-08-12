import sys
import requests
import urllib.request
import urllib.parse
import urllib.error
import re
import os

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

print("Unofficial ReiNX SD Stash Updater\n")

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
    
    saveFile = open('data.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))

infile = "data.txt"
outfile = "data2.txt"

delete_list = ["https://docs.google.com/document/d/", "https://lh4.googleusercontent.com/cExJiMXYxY501RVXRqxPDsCkH1kbjUNvL0693SUJomHZr_TQ6hV", '"><meta',]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()

f = open('data2.txt','r')
message = f.read()
string = (message)

find_urls_in_string = re.compile(regex, re.IGNORECASE)
url = find_urls_in_string.search(string)

if url is not None and url.group(0) is not None:
       url = url.group(0).strip()
ver = url[-6:]
if ver[-1:] is "0":
            ver = ver[:4]
            print("The latest version of Darth Meteos' Super Special SD Stash is " + ver + ".\n")

#Input Function
answer = None
while answer not in ("y", "n"):
    answer = input("Would you like to download it? [y/n]\n\n")
    
    if answer == "n":
        f.close()
        filename = os.getcwd() + '\\data.txt'
        filename2 = os.getcwd() + '\\data2.txt'
        os.remove(filename)
        os.remove(filename2)
        exit()
    elif answer == "y":

        print("")

#Download Function
        link = url
file_name = "Darth Meteos' Super Special SD Stash " + ver + ".zip"
with open(file_name, "wb") as f:
        print ("Downloading %s" % file_name)
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

#Cleaning Function
                filename = os.getcwd() + '\\data.txt'
                filename2 = os.getcwd() + '\\data2.txt'
                

os.remove(filename)
os.remove(filename2)

