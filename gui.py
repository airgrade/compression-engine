import tkinter as tk
from compressmodule import compress, decompress

def compression(i:str, o:str):
    '''i => inputfile ,  o=>outputfile'''
    compress(i, o)
    

window = tk.Tk()
window.title("Compression Engine")
window.geometry("640x480")

#CREATE ENTRY FIELDS
input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
input_label = tk.Label(window, text="File to be compressed")
output_label = tk.Label(window, text="Compressed file name")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry.grid(row=0, column=1,padx=5, pady=5)
output_label.grid(row=1, column=0,padx=5, pady=5)
output_entry.grid(row=1, column=1,padx=5, pady=5)

#CREATE BUTTON FOR COMPRESS
compress_button = tk.Button(window, text="compress", command=lambda:compression(input_entry.get(), output_entry.get()))
compress_button.grid(row=2, column=1)

window.mainloop() 