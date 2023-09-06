import customtkinter as ctk

#Window
root =ctk.CTk()
root.title('Customtkinter app')
root.geometry('600x400')

#Label
label1 = ctk.CTkLabel( 
    root, 
    text='A ctk label',
    fg_color= ('red', 'blue'),
    text_color='white', 
    corner_radius = 10
    )
label1.pack()

button1 =ctk.CTkButton(
    root, 
    text='Dark mode',
    fg_color='black',
    hover_color= 'red',
    command = lambda: ctk.set_appearance_mode('dark')
    )
button1.pack(pady=20)

button2 =ctk.CTkButton(
    root, 
    text='Light mode',
    fg_color='black',
    hover_color= 'red',
    command = lambda: ctk.set_appearance_mode('Light')
    )

button2.pack(pady = 20)



root.mainloop()