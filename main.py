import tkinter as tk

root = tk.Tk()
root.geometry("1280x720")
label = tk.Label(root,text="はじめてのpython",font=("Arial",40))
label1 = tk.Label(root,text="はじめてのpython",font=("Arial",30))
label2 = tk.Label(root,text="はじめてのpython",font=("Arial",20))
label3 = tk.Label(root,text="はじめてのpython",font=("Arial",10))
# label.grid(row=0,column=0)
# label1.grid(row=1,column=1)
# label2.grid(row=2,column=2)
# label3.grid(row=3,column=3)
# label.place(x=0,y=0)
# label1.place(x=1,y=1)
# label2.place(x=2,y=2)
# label3.place(x=3,y=3)
# def button_click():
#     text = entry.get()
#     print(text)
# button = tk.Button(root,text="ボタン",font=("Arail",30),command=button_click())
# button.pack()
# entry = tk.Entry(root,font=("Arail",30))
# entry.grid(row=0,column=0)

#pngのみ
# load_image = tk.PhotoImage(file="スカル.png")#準備
# img = tk.Label(root,image=load_image)#作る
# img.pack()#配置

# #複数行のメッセージ
# msg = tk.Message(
#     root,
#     text="おはようおはようおはようおはようおはようおはようおはようおはよう",
#     bg="white",
#     font=("Arial",20),
#     width=300
# )
# msg.pack()

canvas = tk.Canvas(root,bg="black",width=500,height=500)
canvas.pack()
canvas.create_text(0,0,text="おはようおはよう",fill="white",font=("Arail",20),anchor="nw")
canvas.create_text(500,500,text="おはようおはよう",fill="white",font=("Arail",20),anchor="se")
root.mainloop()