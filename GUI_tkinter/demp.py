import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")             # Tital bar for window
root.geometry("400x300+100+50")        # Size of Window  width x height + x_offset +y_offset   
label = tk.Label(root, text="Hello, Tkinter!") 
label.pack()                            #put the label component on window

label1 = tk.Label(root, text="Hello, Student!") 
label1.pack(side=tk.LEFT)             # Hello Student is display left justified
root.mainloop()
