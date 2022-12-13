import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンがお")


root = tk.Tk()
root.title("難易度選択")
root.geometry("500x200")

button2 = tk.Button(root,text="簡単")
button2.bind("<1>",button_click)
button2.pack()



button = tk.Button(root,text="普通")
button.bind("<1>",button_click)
button.pack()

entry = tk.Entry(root,width=30)
entry.insert(tk.END,"(^^")

button2 = tk.Button(root,text="難しい")
button2.bind("<1>",button_click)
button2.pack()







entry.pack()

root.mainloop()