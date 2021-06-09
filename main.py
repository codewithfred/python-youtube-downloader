import tkinter as tk
from tkinter import *
import pytube
from tkinter import messagebox, filedialog
  
def GUI():
    link_label = Label(root, text="YouTube link  :",bg="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)
   
    root.linkText = Entry(root, width=55, textvariable=video_Link)
    root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)
   
    destination_label = Label(root, text="Destination    :",bg="#E8D579")
    destination_label.grid(row=2, column=0, pady=5, padx=5)
   
    root.destinationText = Entry(root, width=40, textvariable=download_Path)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5)
   
    browse_B = Button(root, text="Browse",command=browseDirectory,width=10,bg="#05E8E0")
    browse_B.grid(row=2,column=2,pady=1,padx=1)
   
    Download_B = Button(root,text="Download", command=downloadVideo, width=20,bg="#05E8E0")
    Download_B.grid(row=3, column=1, pady=3, padx=3)

    my_Label = Label(text ="@Codewithfred", font = 'helvetica 15 bold', bg ='midnightblue' , 
                      width = '20',foreground="orchid1")
    my_Label.grid(row=4, column=1)
  
# Membuat fungsi browseDirectory() untuk browse directory dimana kita ingin simpan video / audionya
def browseDirectory():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_Path.set(download_Directory)
  
# Membuat fungsi downloadVideo() untuk mendownload video
def downloadVideo():
    # disini kita langsung mencari url yang diinput oleh user
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = pytube.YouTube(Youtube_link)
    videoStream = getVideo.streams.first()
    videoStream.download(download_Folder)
    messagebox.showinfo("SUCCESSFULLY", 
                        "DOWNLOADED AND SAVED IN\n" 
                        + download_Folder)

## Next content yak
def downloadVideoToAudio():
  pass

# Buat object dari tk class
root = tk.Tk()

root.geometry("440x120")
root.resizable(False, False)
root.title("YouTube_Video_Downloader")
root.config(background="#000000")
   
# Buat variable tkinter yang sudah di define
video_Link = StringVar()
download_Path = StringVar()
GUI()
root.mainloop()