import tkinter as tk
import random

def click_btn():
    label["text"] = random.choice(["大吉","中吉","小吉","凶"])
    label.update()


root = tk.Tk()
root.title("おみくじソフト")
root.resizable(False,False)
canvas = tk.Canvas(root,width=800,height=600)
canvas.pack()
gazou = tk.PhotoImage(file="C:/Users/kitarira/Documents/py_samples/py_samples/Chapter6/miko.png")
canvas.create_image(400,300,image=gazou)
label = tk.Label(root, text="？？", font=("Times New Roman", 120), bg="white")
label.place(x=380, y=60)
button = tk.Button(root, text="おみくじを引く", font=("Times New Roman", 36), command=click_btn, fg="skyblue")
button.place(x=360, y=400)
root.mainloop()