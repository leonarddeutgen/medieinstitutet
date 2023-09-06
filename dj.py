import customtkinter as ctk

root = ctk.CTk()
root.title('DJ_Stockholm')
root.geometry('400x400')


frame1 = ctk.CTkFrame(root,height=200, width=400,)
frame1.pack()
button1 = ctk.CTkButton(frame1, text='Mac & Eddy', height=100, width=300, fg_color='yellow', text_color='black')
button1.pack()

frame2 = ctk.CTkFrame(root,height=200, width=400,)
frame2.pack()
button2 = ctk.CTkButton(frame2, text='Ögat', height=100, width=300, fg_color='pink', text_color='black')
button2.pack()

frame3 = ctk.CTkFrame(root,height=200, width=400,)
frame3.pack()
button3 = ctk.CTkButton(frame3, text='Kvartesfesten', height=100, width=300, fg_color='blue', text_color='black')
button3.pack()


frame4 = ctk.CTkFrame(root,height=200, width=400,)
frame4.pack()
button4 = ctk.CTkButton(frame4, text='Funky lovers', height=100, width=300, fg_color='lightgreen', text_color='black')
button4.pack()




root.mainloop()