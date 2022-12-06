import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンがお")


root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")
button = tk.Button(root,text="押すな")
button.bind("<1>",button_click)
button.pack()


entry = tk.Entry(root,width=30)
entry.insert(tk.END,"ふががががぴよ")

entry.pack()


tkm.showinfo("asasasasa")
root.mainloop()