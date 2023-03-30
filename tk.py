# # Import module
# from tkinter import *
#
# # Create object
# root = Tk()
#
# # Adjust size
# root.geometry("400x400")
#
# # Add image file
# bg = PhotoImage(file = "R.png")
#
# # Show image using label
# label1 = Label( root, image = bg)
# label1.place(x = 0, y = 0)
#
# label2 = Label( root, text = "Welcome")
# label2.pack(pady = 50)
#
# # Create Frame
# frame1 = Frame(root)
# frame1.pack(pady = 20 )
#
# # Add buttons
# button1 = Button(frame1,text="Exit")
# button1.pack(pady=20)
#
# button2 = Button( frame1, text = "Start")
# button2.pack(pady = 20)
#
# button3 = Button( frame1, text = "Reset")
# button3.pack(pady = 20)
#
# # Execute tkinter
# root.mainloop()

# ########################################################################################

import tkinter
background = "white"
okno = tkinter.Tk()
okno.title("Project")
okno.config(bg = "white")
platno = tkinter.Canvas(okno, height = 300, width = 300, bg = background, highlightthickness = 0)
platno.pack()
def background_color():
    background = vstup2.get()
    try:
        platno.config(bg = background)
    except:
        pass

tkinter.Label(okno,text = "Background color :", bg = "white", width = 30).pack()
vstup2 = tkinter.StringVar()
tkinter.Entry(okno,textvariable = vstup2, bg = "white").pack()
tkinter.Button(okno,width=30, text="Set the color of a background", command=background_color, relief = "flat", activebackground = "white", bd = 0, bg = "white").pack()

okno.mainloop()