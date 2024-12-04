import tkinter as tk
from compressmodule import compress, decompress

def compression(i:str, o:str):
    '''i => inputfile ,  o=>outputfile'''
    compress(i, o)
    
def decompression(i:str, o:str):
    '''i= compressed file, o= decompressed file'''
    decompress(i, o)
    
window = tk.Tk()
window.title("Compression Engine")
window.geometry("640x480")

#CREATE ENTRY FIELDS FOR COMPRESS
input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
input_label = tk.Label(window, text="File to be compressed")
output_label = tk.Label(window, text="Compressed file name")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry.grid(row=0, column=1,padx=5, pady=5)
output_label.grid(row=1, column=0,padx=5, pady=5)
output_entry.grid(row=1, column=1,padx=5, pady=5)

#CREATE ENTRY FIELDS FOR DECOMPRESS
d_input_entry = tk.Entry(window)
d_output_entry = tk.Entry(window)
d_input_label = tk.Label(window, text="Load compressed file")
d_output_label = tk.Label(window, text="Decompressed file name")
d_input_label.grid(row=3, column=0, padx=5, pady=5)
d_input_entry.grid(row=3, column=1,padx=5, pady=5)
d_output_label.grid(row=4, column=0,padx=5, pady=5)
d_output_entry.grid(row=4, column=1,padx=5, pady=5)

#CREATE BUTTON FOR COMPRESS
compress_button = tk.Button(window, text="compress", command=lambda:compression(input_entry.get(), output_entry.get()))
compress_button.grid(row=2, column=1, padx=5, pady=5)

#CREATE BUTTON FOR DECOMPRESS
decompress_button = tk.Button(window, text="Decompress", command= lambda: decompression(d_input_entry.get(), d_output_entry.get()))
decompress_button.grid(row=5, column=1)

window.mainloop() 