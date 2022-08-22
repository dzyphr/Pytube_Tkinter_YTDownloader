#latest as of jul 8 2022
import subprocess
import os.path
import threading
import pytube
import tkinter
from tkinter.messagebox import showinfo
from tkinter import ttk, scrolledtext as st
from pytube import YouTube, Playlist,  exceptions
class GUI(object):
    def __init__(self):
        self.main = tkinter.Tk()
        tk = tkinter
        #small window mode
        #self.main.geometry("350x850+700+200")
        #self.main.geometry("1920x1080")
        self.main.geometry("890x600")
        self.main.resizable(False, False)
        self.main.title('PyTubeTk')
        #self.main.config(bg=self.rgb((70, 0, 62)))
        self.main.config(bg="#332c23")
        self.main.grid()
        #progress bar
        self.pbstyle = ttk.Style()
        self.pbstyle.theme_use('alt')
        self.pbstyle.configure("custom.Horizontal.TProgressbar", foreground="#9F87AF", background="#88527F")
        self.pb = ttk.Progressbar(self.main, style="custom.Horizontal.TProgressbar" ,   mode='indeterminate', length=315, orient="horizontal")
        self.pb.grid(row=20, column=36, columnspan=11)
        #entry fields
        self.inFrame = ttk.Frame(self.main)
        self.YtLinkLabel = tk.Label(self.main, text="Paste your YouTube Playlist Link here:",  background="#332c23" ,fg="#B1DDF1")
        self.YtLinkLabel.grid(row=0, column=0)
        self.LINK = tkinter.StringVar()
        self.YtLinkEntry = tk.Entry(self.main, textvariable=self.LINK, width=50, background="#614344")
        self.YtLinkEntry.grid(row=0, column=34, columnspan=11)
        self.LIMIT = tkinter.StringVar()
        self.listlimitlabel = tk.Label(self.main, text="Limit the Number of Videos to Download or List:", background="#332c23", fg="#B1DDF1")
        self.listlimitlabel.grid(row=1, column=0,)
        self.listlimit = tk.Entry(self.main, textvariable=self.LIMIT, width=50, background="#614344")
        self.listlimit.grid(row=1, column=34, columnspan=11)
        self.DIRECTORY = tkinter.StringVar()
        self.dirEntryLabel = tk.Label(self.main, text="Playlist Download Directory Name:",  background="#332c23" ,fg="#B1DDF1")
        self.dirEntryLabel.grid(row=2, column=0,)
        self.directoryEntry = tk.Entry(self.main, textvariable=self.DIRECTORY, width=50, background="#614344")
        self.directoryEntry.grid(row=2, column=34, columnspan=11)
        self.audio = False;
        self.ogg = False;
        self.del_orig = False;
        #convert to ogg button
        self.conv_ogg = tk.Button(self.main, text="Convert .mp4 to .ogg", command=self.ConvertToOgg, bg="#9F87AF", activebackground="#88527F")
        self.conv_ogg.grid(row = 14, column =0)
        #format as audio button
        self.format_audio = tk.Button(self.main, text="Format as Audio", command=self.FormatAsAudio,  bg="#9F87AF", activebackground="#88527F")
        self.format_audio.grid(row = 13, column =0)
        #delete .mp4 original file
        self.delete_or = tk.Button(self.main, text="Delete original .mp4", command=self.del_orig_bool,  bg="#9F87AF", activebackground="#88527F")
        self.delete_or.grid(row = 15, column = 0)
        #download button
        self.download = tkinter.Button(self.main , text="Download", command=self.download_loop, bg="#9F87AF", activebackground="#88527F")
        self.download.grid(row = 21, column = 0)
        #list videos button
        self.list = tk.Button(self.main, text="Get List of Videos", command=self.list_loop,  bg="#9F87AF", activebackground="#88527F")
        self.list.grid(row = 7, column = 37,  )
        #clearlist button
        self.clearlist = tk.Button(self.main, text="Clear List", command=self.clearlist,  bg="#9F87AF", activebackground="#88527F")
        self.clearlist.grid(row=21, column=34)
        #list videos read only text
        self.text_area = st.ScrolledText(self.main ,width=79, font = ("Times New Roman", 11), background="#614344")
        self.text_area.grid(row=8, column=18, columnspan=20, rowspan=10)
        self.text_area.configure(state ='disabled')
        #format as audio text box
        self.format_status = st.ScrolledText(self.main,width=35, height=4, font = ("Times New Roman", 10), background="#614344")
        self.format_status.grid(row=16, column=0, columnspan = 1, rowspan=4)
        self.format_status.configure(state="disabled") 

    def rgb(self, rgb):
        return "#%02x%02x%02x" % rgb

    def regexErr(self):
        msgRegexMatchErr = "Entered Link didn't return a match"
        showinfo(title='RegexMatchError', message=msgRegexMatchErr)

    def unavailableErr(self):
        msgUnavailable = 'Selected Video Returned "Unavailable"'
        showinfo(title='Unavailable Video', message=msgUnavailable)
    
    def KeyErr(self):
        msgKeyErr = "Key Error returned indicating fields are empty\nAdd Link and Limit if using playlists"
        showinfo(title='KeyError', message=msgKeyErr)
    
    def del_orig_bool(self):
        if self.ogg == True: 
            if self.del_orig == False:
                self.del_orig = True
                if self.audio == True:
                    self.format_status.configure(state = 'normal')
                    self.format_status.insert(tkinter.INSERT, "deleting original .mp4\n")
                    self.format_status.configure(state = 'disabled')
            else:
                self.del_orig = False
                if self.audio == True:
                    self.format_status.configure(state = 'normal')
                    self.format_status.delete("1.0", "end")
                    self.format_status.insert(tkinter.INSERT, "downloading audio only .mp4\n")
                    self.format_status.configure(state = 'disabled')
                    if self.ogg == True:
                        self.format_status.configure(state = 'normal')
                        self.format_status.insert(tkinter.INSERT, "will convert audio only .mp4 into .ogg\n")
                        self.format_status.configure(state = 'disabled')

    def FormatAsAudio(self):
        if self.audio == False:
            self.audio = True
            self.format_status.configure(state = 'normal')
            self.format_status.insert(tkinter.INSERT, "downloading audio only .mp4\n")
            self.format_status.configure(state = 'disabled')
            if self.ogg == True:
                self.format_status.configure(state = 'normal')
                self.format_status.insert(tkinter.INSERT, "will convert audio only .mp4 into .ogg\n")
                self.format_status.configure(state = 'disabled')
                if self.del_orig == True:
                    self.format_status.configure(state = 'normal')
                    self.format_status.insert(tkinter.INSERT, "deleting original .mp4\n")
        else:
            self.audio = False
            self.format_status.configure(state = 'normal')
            self.format_status.delete("1.0", "end")
            self.format_status.configure(state = 'disabled')
    
    def ConvertToOgg(self):
        if self.ogg == False:
            self.ogg = True
            if self.audio == True:
                self.format_status.configure(state = 'normal')
                self.format_status.insert(tkinter.INSERT, "will convert audio only .mp4 into .ogg\n")
                self.format_status.configure(state = 'disabled')
                if self.del_orig == True:
                    self.format_status.configure(state = 'normal')
                    self.format_status.insert(tkinter.INSERT, "deleting original .mp4\n")
        else:
            self.ogg = False
            if self.audio == True:
                self.format_status.configure(state = 'normal')
                self.format_status.delete("1.0", "end")
                self.format_status.insert(tkinter.INSERT, "downloading audio only .mp4\n")
                self.format_status.configure(state = 'disabled')

            

    def getplaylist(self):
        i = 0
        limit = 0
        path = f'PlaylistDownload'
        if self.DIRECTORY.get() != "":
            path = f'{self.DIRECTORY.get()}'
        if os.path.exists(path) == False:
            os.mkdir(path)
        while self.audio == False:
            try:
                for video in self.pl:
                    YouTube(video).streams.get_highest_resolution().download(output_path=path)
                    i = i+1
                    if self.LIMIT.get() == "":
                        print("NO LIMIT SET")
                        limit = len(self.pl)
                    else:
                        limit = self.LIMIT.get()
                    if i == int(limit):
                        break
                    else:
                        continue

            except KeyError:
                self.KeyErr()
            
            if i == int(limit):
                break

        while self.audio == True:
            try:
                for video in self.pl:
                    YouTube(video).streams.filter(only_audio=True)[0].download(output_path=path)
                    i = i+1
                    if self.LIMIT.get() == "":
                        limit = len(self.pl)
                    else:
                        limit = self.LIMIT.get()
                    if i == int(limit):
                        break
                    else:
                        continue
            
            except KeyError:
                self.KeyErr()
            
            if i == int(limit):
                if self.ogg == True:
                    #print("conv oggs")
                    self.convert_ogg()
                break
    
    def convert_ogg(self):
        i = 0
        limit = 0
        for video in self.pl:
            if self.LIMIT.get() == "":
                limit = len(self.pl)
            else:
                limit = self.LIMIT.get()
            print(YouTube(video).title)
            title = (YouTube(video).title)
            i = i + 1
            atitle = title.replace('.', '')
            btitle = atitle.replace('\'', '')
            ctitle = btitle.replace('\"', '')
            dtitle = ctitle.replace(',', '')
            etitle = dtitle.replace('?', '')
            ftitle = etitle.replace('/', '')
            gtitle = ftitle.replace(':', '')
            htitle = gtitle.replace('|', '')
            ititle = htitle.replace('#', "")
            print("ititle:" , ititle)
            directory = self.DIRECTORY.get()
            ogg = directory + "/" + ititle + ".ogg"
            target = directory + "/" + ititle  + ".mp4" 
            print(target)
            if os.path.isfile(ogg) == False:
                out = subprocess.Popen(['./vid_to_ogg', target], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                stdout,stderr=out.communicate()
                str_stdout = str(stdout)
                str_stderr = str(stderr)
                print(str_stdout, str_stderr)
            if self.del_orig == True:
                os.remove(target)
            if i == int(limit):
                break
        #out = subprocess.Popen(['vid_to_ogg', ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def downloadmsg(self):
        self.msgDownloading = 'Click Ok To Start Downloading!'
        showinfo(title='Ready', message=self.msgDownloading)
    
    def getlist(self):
        i = 0
        limit = 0
        titles = []
        try:
            for video in self.pl:
                title = []
                title.append(YouTube(video).title)
                titles.append(title)
                print(title)
                self.text_area.configure(state ='normal')
                self.text_area.insert(tkinter.INSERT, title)
                self.text_area.insert(tkinter.INSERT, "\n")
                self.text_area.configure(state ='disabled')
                i = i+1
                if self.LIMIT.get() == "":
                    limit = len(self.pl)
                else:
                    limit = self.LIMIT.get()
                if len(titles) == int(limit):
                    break
                else:
                    continue
        except KeyError:
                self.KeyErr()
    
    def clearlist(self):
        self.text_area.configure(state ='normal')
        self.text_area.delete("1.0", "end")
        self.text_area.configure(state ='disabled')


    def check_thread_download(self):
        if self.secondarythread.is_alive():
            self.main.after(50, self.check_thread_download)
        else:
            self.pb.stop()
            self.msgFinished = 'Finished!'
            showinfo(title='download finished', message=self.msgFinished)
            self.pb.stop()

    def check_thread_list(self):
        if self.secondarythread.is_alive():
            self.main.after(50, self.check_thread_list)
        else:
            self.pb.stop()
            self.msgFinished = 'Finished!'
            showinfo(title='list finished', message=self.msgFinished)
            self.pb.stop()
    
    def download_loop(self):
        try:
            self.pl = Playlist(self.LINK.get()) #possibly .get()
        except pytube.exceptions.VideoUnavailable:
            self.unavailableErr()
        except pytube.exceptions.RegexMatchError:
            self.regexErr()
        except KeyError:
            self.KeyErr()
        else:
            self.downloadmsg()
            self.pb.start()
            self.secondarythread = threading.Thread(target=self.getplaylist)
            self.secondarythread.start()
            self.main.after(50, self.check_thread_download)
    
    def list_loop(self):
        try:
            self.pl = Playlist(self.LINK.get())
        except pytube.exceptions.VideoUnavailable:
            self.unavailableErr()
        except pytube.exceptions.RegexMatchError:
            self.regexErr()
        except KeyError:
            self.KeyErr()
        else:
            self.pb.start()
            self.secondarythread = threading.Thread(target=self.getlist)
            self.secondarythread.start()
            self.main.after(50, self.check_thread_list)

gui = GUI()
gui.main.mainloop()
