#Importing libraries. pillows for image stuff, tkinter for windows explorer

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

#function for opening windows explorer and then the original image

def Original():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk

#function for opening windows explorer and then the mask image

def Mask():
    mask_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if mask_path:
        img2 = Image.open(mask_path)
        img2 = img2.resize((100, 100))
        img2_tk = ImageTk.PhotoImage(img2)
        label2.config(image=img2_tk)
        label2.image = img2_tk


#create root window
window = tk.Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label = tk.Label(window,text = "Selecting Images")

#Top text
label2 = tk.Label(window,text = "  ")

#Original image selecting button       
button_og = tk.Button(window,text = "Select original image",command = Original)

#Mask image selecting button 
button_mask = tk.Button(window,text = "Select masked image",command = Mask)

#Exit button
button_exit = tk.Button(window,text = "Exit",command = exit) 


# Grid method is chosen for placing the widgets at respective positions in a table like structure by specifying rows and columns
label.grid(column = 49, row = 1)

label2.grid(column=51,row=1)

button_og.grid(column = 50, row = 4)

button_mask.grid(column=50,row=5)
  
button_exit.grid(column = 50,row = 6)  
# Let the window wait for any events
window.mainloop()
