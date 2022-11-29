
import tkinter as tk
import tkinter.messagebox as tkm


# 練習３
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get() # 数式の文字列
        res = eval(siki) # 数式文字列の評価
        entry.delete(0, tk.END) # 表示文字列の削除
        entry.insert(tk.END, res) # 結果の挿入
    else: # 「=」以外のボタン字
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        # 練習６
        entry.insert(tk.END, num)

    
# 練習１
root = tk.Tk()
root.geometry("650x662")

# 練習４
entry = tk.Entry(root, justify="right",fg="white",bg="brown", width=10, font=("",80))
entry.grid(row=0, column=0, columnspan=3)

# 練習２
r, c = 1, 0
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}",fg="white",bg="brown", width=10, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

# 練習５
operators = ["+"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}",fg="white",bg="brown", width=10, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

operators = ["="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}",fg="white",bg="brown", width=10, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

operators = ["-"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}",fg="white",bg="brown", width=10, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r -= 1
        c = 0

operators = ["*"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}",fg="white",bg="brown", width=10, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r *= 1
        c = 0

operators = ["/"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}",fg="white",bg="brown", width=10, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r /= 1
        c = 0



root.mainloop()