import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import subprocess
import os

# Function tp start the Oculus option
def run_oculus():
    eye_path = os.path.join("Oculus", "main_oculus.py")
    subprocess.run(["python", eye_path])

# Function to start the Lingua option
def run_lingua():
    speak_path = os.path.join("Lingua", "main_lingua.py")
    subprocess.run(["python", speak_path])


# Menu
def main():
    root = tk.Tk() # New root window
    root.title("Ciclope")
    root.geometry("900x700")

    # Background setting
    image_path = "background.gif"  # Check that you have downloaded the .gif!
    image = Image.open(image_path)
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
   
    # Fonts setting
    title_font = font.Font(family='Helvetica', size=24, weight='normal')
    subtitle_font = font.Font(family='Helvetica', size=18, weight='normal')
    button_font = font.Font(family='Helvetica', size=14)
    credits_font = font.Font(family='Helvetica', size=10, weight='normal')
    
    # Titles setting
    title_label = tk.Label(root, text="WELCOME TO CICLOPE!", font=title_font, bg='lightblue')
    title_label.place(relx=0.75, rely=0.075, anchor='n')

    subtitle_label = tk.Label(root, text="Choose a function...", font=subtitle_font, bg='lightblue')
    subtitle_label.place(relx=0.5, rely=0.3, anchor='n')

    # Buttons setting
    btn1 = tk.Button(root, text="Oculus", font=button_font, bg='lightblue', fg='black', command=run_oculus)
    btn1.place(relx=0.25, rely=0.7, anchor='n')

    btn2 = tk.Button(root, text="Lingua", font=button_font, bg='lightblue', fg='black', command=run_lingua)
    btn2.place(relx=0.75, rely=0.7, anchor='n')

    # Credits
    credits_label = tk.Label(root, text="Odysseus in the Cave of Polyphemus - Jacob Jordaens (1593-1678) - Pushkin Museum", font=credits_font, bg='lightblue')
    credits_label.place(relx=0.5, rely=0.90, anchor='n')

    root.mainloop()

if __name__ == "__main__":
    main()

