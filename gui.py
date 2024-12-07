import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog #this allows you to open up any file in your computer

def open_file():
    '''This function will open a file in the compter and return the path of that file'''
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file ")
    return filename
    
def compression(i:str, o:str):
    '''i => inputfile ,  o=>outputfile'''
    compress(i, o)
    
def decompression(i:str, o:str):
    '''i= compressed file, o= decompressed file'''
    decompress(i, o)
    
window = tk.Tk()
window.title("Compression Engine")
window.geometry("640x480")



#CREATE BUTTON FOR COMPRESS
compress_button = tk.Button(window, text="compress", command=lambda:compression(open_file(), "compressedoutput1.txt"))
compress_button.pack()

#CREATE BUTTON FOR DECOMPRESS
decompress_button = tk.Button(window, text="Decompress", command= lambda: decompression(open_file(), "decompressedout1"))
decompress_button.pack()

window.mainloop() 