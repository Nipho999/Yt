from pytube import YouTube
import colorama
from pytube.cli import on_progress
import os
import sys
import time
from colorama import Fore
from slowprint.slowprint import *
print('\033[1;34;50m \n     [๐ปโ โ โ โ โ โ แชแฉแK แOแแชแฎแ โ โ โ โ โ โ๐ป]')
slowprint(Fore.GREEN +"\n             โโโโโโโโโโโโโโโโโโโโ\n             โโโโโโโโโโโโโโโโโโโโ\n             โโโโโโโโโโโโโโโโโโโโ\n",0.2)
slowprint(Fore.YELLOW +"\n###############โโโโโโโโโโโโโโโโ############\n#โโโโโโโโโโโโโโโDARKโCODERโโโโโโโโโโโโโโโโ#\n#โโโโโโโโโโโโโโโโโโโ##โโโโโโโโโโโโโโโโโโโโ#\nโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ#",0.2)
slowprint(Fore.BLUE +"\n [+] script   : >> youtube-Downloader\n [+] Author   : >> Nipho101\n [+] Github   : >> Nipho999\n [+] Facebook : >> hohpin\n\n       -----Dark coders 4ever----",0.3)
slowprint(Fore.WHITE +"\n******************************************\n",0.3)
urlVid = input(Fore.RED + "\n[+]โโโโโโโโ ๐ฃ๐๐ฆ๐ง๐ ๐ฌ๐ข๐จ๐ง๐จ๐๐ ๐๐๐ก๐ BELOW โโโโโโ\n[+] : ")
myVid = YouTube(urlVid,on_progress_callback=on_progress)
slowprint(Fore.BLUE + "\n###### ๐ตโ ๐ฑโ ๐ชโ ๐ฆโ ๐ธโ ๐ชโ ๐ผโ ๐ฆโ ๐ฎโ ๐นโ.....",0.5)
slowprint(Fore.YELLOW + f">>title: {myVid.title}",0.4)
slowprint(Fore.WHITE + f">>Channel: {myVid.author}",0.4)
slowprint(Fore.GREEN + f">>Length: {myVid.length}",0.4)
slowprint(Fore.WHITE + f">>Views: {myVid.views}",0.4)
quality = int(input(Fore.RED + ">>choose available Video Quality:  1080 / 720 / 360 \n>>"))

slowprint(Fore.BLUE + "[+]>>Downloading video ..... please wait..",0.5)
if quality == 1080:
    stream = myVid.streams.get_by_itag(137)
    stream.download()
    slowprint(Fore.GREEN + ">>๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ฒ๐พ๐ผ๐ฟ๐ป๐ด๐๐ด...",0.7)
elif quality == 720:
    stream = myVid.streams.get_by_itag(22)
    stream.download()
    slowprint(Fore.GREEN + ">>๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ฒ๐พ๐ผ๐ฟ๐ป๐ด๐๐ด....",0.7)
elif quality == 360:
    stream = myVid.streams.get_by_itag(18)
    stream.download()
    slowprint(Fore.GREEN + ">>๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ฒ๐พ๐ผ๐ฟ๐ป๐ด๐๐ด...",0.7)

else: slowprint (Fore.YELLOW +"SOMETHING WENT WRONG",0.10 )
previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        print(liveprogress)
