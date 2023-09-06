import tkinter as tk
from tkinter import messagebox

class green_box:
    def __init__(self,):
        self.root = tk.Tk()
        self.root.title('My_Greenbox')
        self.root.geometry('1000x800')

        self.label = tk.Label(self.root, text='PUO_Finder', font=('Arial', 18), background='white',)
        self.label.pack(padx=10, pady=10, fill='both',side='top')

        #Frame 1 start
        self.frame1 =tk.Frame(self.root)
        self.frame1.pack(side='top')

        #BOX1
        self.label_frame1 = tk.LabelFrame(self.frame1, text='BOX 1', font=('Arial',15))
        self.label_frame1.pack(side='left')
        self.label1 = tk.Label(self.label_frame1, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label1.pack(side='top')
        self.clear_button = tk.Button(self.label_frame1, text='Radera', font=('Arial',10), command=self.clear_label1)
        self.clear_button.pack(side='bottom')

        #BOX2
        self.label_frame2 = tk.LabelFrame(self.frame1, text='BOX 2', font=('Arial', 15))
        self.label_frame2.pack(side='left')
        self.label2 = tk.Label(self.label_frame2, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label2.pack(side='top')
        self.clear_button = tk.Button(self.label_frame2, text='Radera', font=('Arial', 10), command=self.clear_label2)
        self.clear_button.pack(side='bottom')

        #BOX3
        self.label_frame3 =tk.LabelFrame(self.frame1, text='BOX3', font=('Arial', 15))
        self.label_frame3.pack(side='left')
        self.label3 = tk.Label(self.label_frame3, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label3.pack(side='top')
        self.clear_button = tk.Button(self.label_frame3, text='Radera', font=('Arial', 10), command=self.clear_label3)
        self.clear_button.pack(side='bottom')

        #BOX4
        self.label_frame4 = tk.LabelFrame(self.frame1, text='BOX 4', font=('Arial', 15))
        self.label_frame4.pack(side='left')
        self.label4 = tk.Label(self.label_frame4, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label4.pack(side='top')
        self.clear_button = tk.Button(self.label_frame4, text='Radera', font=('Arial', 10), command=self.clear_label4)
        self.clear_button.pack(side='bottom')

        #BOX5
        self.label_frame5 = tk.LabelFrame(self.frame1, text='BOX 5', font=('Arial', 15))
        self.label_frame5.pack(side='left')
        self.label5 = tk.Label(self.label_frame5, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label5.pack(side='top')
        self.clear_button = tk.Button(self.label_frame5, text='Radera', font=('Arial', 10), command=self.clear_label5)
        self.clear_button.pack(side='bottom')

        #Frame 2 start
        self.frame2 =tk.Frame(self.root)
        self.frame2.pack(side='top')

        #BOX6
        self.label_frame6 = tk.LabelFrame(self.frame2, text='BOX 6', font=('Arial',15))
        self.label_frame6.pack(side='left')
        self.label6 = tk.Label(self.label_frame6, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label6.pack(side='top')
        self.clear_button = tk.Button(self.label_frame6, text='Radera', font=('Arial', 10), command=self.clear_label6)
        self.clear_button.pack(side='bottom')

        #BOX7
        self.label_frame7 = tk.LabelFrame(self.frame2, text='BOX 7', font=('Arial', 15))
        self.label_frame7.pack(side='left')
        self.label7 = tk.Label(self.label_frame7, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label7.pack(side='top')
        self.clear_button = tk.Button(self.label_frame7, text='Radera', font=('Arial', 10), command=self.clear_label7)
        self.clear_button.pack(side='bottom')

        #BOX8
        self.label_frame8 =tk.LabelFrame(self.frame2, text='BOX8', font=('Arial', 15))
        self.label_frame8.pack(side='left')
        self.label8 = tk.Label(self.label_frame8, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label8.pack(side='top')
        self.clear_button = tk.Button(self.label_frame8, text='Radera', font=('Arial', 10), command=self.clear_label8)
        self.clear_button.pack(side='bottom')

        #BOX9
        self.label_frame9 = tk.LabelFrame(self.frame2, text='BOX 9', font=('Arial', 15))
        self.label_frame9.pack(side='left')
        self.label9 = tk.Label(self.label_frame9, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label9.pack(side='top')
        self.clear_button = tk.Button(self.label_frame9, text='Radera', font=('Arial', 10), command=self.clear_label9)
        self.clear_button.pack(side='bottom')

        #BOX10
        self.label_frame10 = tk.LabelFrame(self.frame2, text='BOX 10', font=('Arial', 15))
        self.label_frame10.pack(side='left')
        self.label10 = tk.Label(self.label_frame10, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label10.pack(side='top')
        self.clear_button = tk.Button(self.label_frame10, text='Radera', font=('Arial', 10), command=self.clear_label10)
        self.clear_button.pack(side='bottom')

        #Frame 3 start
        self.frame3 =tk.Frame(self.root)
        self.frame3.pack(side='top')

        #BOX11
        self.labelframe11 = tk.LabelFrame(self.frame3, text='BOX 11', font=('Arial', 15))
        self.labelframe11.pack(side='left')
        self.label11 = tk.Label(self.labelframe11, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label11.pack(side='top')
        self.clear_button = tk.Button(self.labelframe11, text='Radera', font=('Arial', 10), command=self.clear_label11)
        self.clear_button.pack(side='bottom')

        #BOX12
        self.labelframe12 = tk.LabelFrame(self.frame3, text='BOX 12', font=('Arial', 15))
        self.labelframe12.pack(side='left')
        self.label12 = tk.Label(self.labelframe12, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label12.pack(side='top')
        self.clear_button = tk.Button(self.labelframe12, text='Radera', font=('Arial', 10), command=self.clear_label12)
        self.clear_button.pack(side='bottom')

        #BOX13
        self.labelframe13 = tk.LabelFrame(self.frame3, text='BOX 13', font=('Arial', 15))
        self.labelframe13.pack(side='left')
        self.label13 = tk.Label(self.labelframe13, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label13.pack(side='top')
        self.clear_button = tk.Button(self.labelframe13, text='Radera', font=('Arial', 10), command=self.clear_label13)
        self.clear_button.pack(side='bottom')

        #BOX14
        self.labelframe14 = tk.LabelFrame(self.frame3, text='BOX 14', font=('Arial', 15))
        self.labelframe14.pack(side='left')
        self.label14 = tk.Label(self.labelframe14, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label14.pack(side='top')
        self.clear_button = tk.Button(self.labelframe14, text='Radera', font=('Arial', 10), command=self.clear_label14)
        self.clear_button.pack(side='bottom')

        #BOX15
        self.labelframe15 = tk.LabelFrame(self.frame3, text='BOX 15', font=('Arial', 15))
        self.labelframe15.pack(side='left')
        self.label15 = tk.Label(self.labelframe15, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label15.pack(side='top')
        self.clear_button = tk.Button(self.labelframe15, text='Radera', font=('Arial', 10), command=self.clear_label15)
        self.clear_button.pack(side='bottom')

        #Frame 4 start
        self.frame4 =tk.Frame(self.root)
        self.frame4.pack(side='top')

        #BOX16
        self.labelframe16 = tk.LabelFrame(self.frame4, text='BOX 16', font=('Arial', 15))
        self.labelframe16.pack(side='left')
        self.label16 = tk.Label(self.labelframe16, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label16.pack(side='top')
        self.clear_button = tk.Button(self.labelframe16, text='Radera', font=('Arial', 10), command=self.clear_label16)
        self.clear_button.pack(side='bottom')

        #BOX17
        self.labelframe17 = tk.LabelFrame(self.frame4, text='BOX 17', font=('Arial', 15))
        self.labelframe17.pack(side='left')
        self.label17 = tk.Label(self.labelframe17, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label17.pack(side='top')
        self.clear_button = tk.Button(self.labelframe17, text='Radera', font=('Arial', 10), command=self.clear_label17)
        self.clear_button.pack(side='bottom')

        #BOX18
        self.labelframe18 = tk.LabelFrame(self.frame4, text='BOX 18', font=('Arial', 15))
        self.labelframe18.pack(side='left')
        self.label18 = tk.Label(self.labelframe18, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label18.pack(side='top')
        self.clear_button = tk.Button(self.labelframe18, text='Radera', font=('Arial', 10), command=self.clear_label18)
        self.clear_button.pack(side='bottom')

        #BOX19
        self.labelframe19 = tk.LabelFrame(self.frame4, text='BOX 19', font=('Arial', 15))
        self.labelframe19.pack(side='left')
        self.label19 = tk.Label(self.labelframe19, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label19.pack(side='top')
        self.clear_button = tk.Button(self.labelframe19, text='Radera', font=('Arial', 10), command=self.clear_label19)
        self.clear_button.pack(side='bottom')

        #BOX20
        self.labelframe20 = tk.LabelFrame(self.frame4, text='BOX 20', font=('Arial', 15))
        self.labelframe20.pack(side='left')
        self.label20 = tk.Label(self.labelframe20, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label20.pack(side='top')
        self.clear_button = tk.Button(self.labelframe20, text='Radera', font=('Arial', 10), command=self.clear_label20)
        self.clear_button.pack(side='bottom')


        #Start på rad 20 till 40

        #Frame 5
        self.frame5 = tk.Frame(self.root)
        self.frame5.pack( side='top')


        #BOX21
        self.label_frame21 = tk.LabelFrame(self.frame5, text='BOX 21', font=('Arial',15))
        self.label_frame21.pack(side='left')
        self.label21 = tk.Label(self.label_frame21, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label21.pack(side='top')
        self.clear_button = tk.Button(self.label_frame21, text='Radera', font=('Arial',10), command=self.clear_label21)
        self.clear_button.pack(side='bottom')

        #BOX22
        self.label_frame22 = tk.LabelFrame(self.frame5, text='BOX 22', font=('Arial', 15))
        self.label_frame22.pack(side='left')
        self.label22 = tk.Label(self.label_frame22, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label22.pack(side='top')
        self.clear_button = tk.Button(self.label_frame22, text='Radera', font=('Arial', 10), command=self.clear_label22)
        self.clear_button.pack(side='bottom')

        #BOX23
        self.label_frame23 =tk.LabelFrame(self.frame5, text='BOX23', font=('Arial', 15))
        self.label_frame23.pack(side='left')
        self.label23 = tk.Label(self.label_frame23, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label23.pack(side='top')
        self.clear_button = tk.Button(self.label_frame23, text='Radera', font=('Arial', 10), command=self.clear_label23)
        self.clear_button.pack(side='bottom')

        #BOX24
        self.label_frame24 = tk.LabelFrame(self.frame5, text='BOX 24', font=('Arial', 15))
        self.label_frame24.pack(side='left')
        self.label24 = tk.Label(self.label_frame24, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label24.pack(side='top')
        self.clear_button = tk.Button(self.label_frame24, text='Radera', font=('Arial', 10), command=self.clear_label24) 
        self.clear_button.pack(side='bottom')

        #BOX25
        self.label_frame25 = tk.LabelFrame(self.frame5, text='BOX 25', font=('Arial', 15))
        self.label_frame25.pack(side='left')
        self.label25 = tk.Label(self.label_frame25, text='', font=('Arial', 20), background='lightgreen',borderwidth=1, relief='solid')
        self.label25.pack(side='top')
        self.clear_button = tk.Button(self.label_frame25, text='Radera', font=('Arial', 10), command=self.clear_label25) 
        self.clear_button.pack(side='bottom')


        #Frame 6
        self.frame6 = tk.Frame(self.root)
        self.frame6.pack(side='top')

        # BOX26
        self.label_frame26 = tk.LabelFrame(self.frame6, text='BOX 26', font=('Arial', 15))
        self.label_frame26.pack(side='left')
        self.label26 = tk.Label(self.label_frame26, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label26.pack(side='top')
        self.clear_button = tk.Button(self.label_frame26, text='Radera', font=('Arial', 10), command=self.clear_label26) 
        self.clear_button.pack(side='bottom')
        
        # BOX27
        self.label_frame27 = tk.LabelFrame(self.frame6, text='BOX 27', font=('Arial', 15))
        self.label_frame27.pack(side='left')
        self.label27 = tk.Label(self.label_frame27, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label27.pack(side='top')
        self.clear_button = tk.Button(self.label_frame27, text='Radera', font=('Arial', 10), command=self.clear_label27) 
        self.clear_button.pack(side='bottom')
        
        # BOX28
        self.label_frame28 = tk.LabelFrame(self.frame6, text='BOX 28', font=('Arial', 15))
        self.label_frame28.pack(side='left')
        self.label28 = tk.Label(self.label_frame28, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label28.pack(side='top')
        self.clear_button = tk.Button(self.label_frame28, text='Radera', font=('Arial', 10), command=self.clear_label28) 
        self.clear_button.pack(side='bottom')
        
        # BOX29
        self.label_frame29 = tk.LabelFrame(self.frame6, text='BOX 29', font=('Arial', 15))
        self.label_frame29.pack(side='left')
        self.label29 = tk.Label(self.label_frame29, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label29.pack(side='top')
        self.clear_button = tk.Button(self.label_frame29, text='Radera', font=('Arial', 10), command=self.clear_label29) 
        self.clear_button.pack(side='bottom')
        
        # BOX30
        self.label_frame30 = tk.LabelFrame(self.frame6, text='BOX 30', font=('Arial', 15))
        self.label_frame30.pack(side='left')
        self.label30 = tk.Label(self.label_frame30, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label30.pack(side='top')
        self.clear_button = tk.Button(self.label_frame30, text='Radera', font=('Arial', 10), command=self.clear_label30) 
        self.clear_button.pack(side='bottom')

        #Frame7
        self.frame7 = tk.Frame(self.root)
        self.frame7.pack(side='top')

        # BOX31
        self.label_frame31 = tk.LabelFrame(self.frame7, text='BOX 31', font=('Arial', 15))
        self.label_frame31.pack(side='left')
        self.label31 = tk.Label(self.label_frame31, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label31.pack(side='top')
        self.clear_button = tk.Button(self.label_frame31, text='Radera', font=('Arial', 10), command=self.clear_label31) 
        self.clear_button.pack(side='bottom')
        
        # BOX32
        self.label_frame32 = tk.LabelFrame(self.frame7, text='BOX 32', font=('Arial', 15))
        self.label_frame32.pack(side='left')
        self.label32 = tk.Label(self.label_frame32, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label32.pack(side='top')
        self.clear_button = tk.Button(self.label_frame32, text='Radera', font=('Arial', 10), command=self.clear_label32) 
        self.clear_button.pack(side='bottom')
        
        # BOX33
        self.label_frame33 = tk.LabelFrame(self.frame7, text='BOX 33', font=('Arial', 15))
        self.label_frame33.pack(side='left')
        self.label33 = tk.Label(self.label_frame33, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label33.pack(side='top')
        self.clear_button = tk.Button(self.label_frame33, text='Radera', font=('Arial', 10), command=self.clear_label33) 
        self.clear_button.pack(side='bottom')
        
        # BOX34
        self.label_frame34 = tk.LabelFrame(self.frame7, text='BOX 34', font=('Arial', 15))
        self.label_frame34.pack(side='left')
        self.label34 = tk.Label(self.label_frame34, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label34.pack(side='top')
        self.clear_button = tk.Button(self.label_frame34, text='Radera', font=('Arial', 10), command=self.clear_label34) 
        self.clear_button.pack(side='bottom')
        
        # BOX35
        self.label_frame35 = tk.LabelFrame(self.frame7, text='BOX 35', font=('Arial', 15))
        self.label_frame35.pack(side='left')
        self.label35 = tk.Label(self.label_frame35, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label35.pack(side='top')
        self.clear_button = tk.Button(self.label_frame35, text='Radera', font=('Arial', 10), command=self.clear_label35) 
        self.clear_button.pack(side='bottom')

        #Farme8
        self.frame8 = tk.Frame(self.root)
        self.frame8.pack(side='top')

        # BOX36
        self.label_frame36 = tk.LabelFrame(self.frame8, text='BOX 36', font=('Arial', 15))
        self.label_frame36.pack(side='left')
        self.label36 = tk.Label(self.label_frame36, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label36.pack(side='top')
        self.clear_button = tk.Button(self.label_frame36, text='Radera', font=('Arial', 10), command=self.clear_label36) 
        self.clear_button.pack(side='bottom')
        
        # BOX37
        self.label_frame37 = tk.LabelFrame(self.frame8, text='BOX 37', font=('Arial', 15))
        self.label_frame37.pack(side='left')
        self.label37 = tk.Label(self.label_frame37, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label37.pack(side='top')
        self.clear_button = tk.Button(self.label_frame37, text='Radera', font=('Arial', 10), command=self.clear_label37) 
        self.clear_button.pack(side='bottom')
        
        # BOX38
        self.label_frame38 = tk.LabelFrame(self.frame8, text='BOX 38', font=('Arial', 15))
        self.label_frame38.pack(side='left')
        self.label38 = tk.Label(self.label_frame38, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label38.pack(side='top')
        self.clear_button = tk.Button(self.label_frame38, text='Radera', font=('Arial', 10), command=self.clear_label38) 
        self.clear_button.pack(side='bottom')
        
        # BOX39
        self.label_frame39 = tk.LabelFrame(self.frame8, text='BOX 39', font=('Arial', 15))
        self.label_frame39.pack(side='left')
        self.label39 = tk.Label(self.label_frame39, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label39.pack(side='top')
        self.clear_button = tk.Button(self.label_frame39, text='Radera', font=('Arial', 10), command=self.clear_label39) 
        self.clear_button.pack(side='bottom')
        
        # BOX40
        self.label_frame40 = tk.LabelFrame(self.frame8, text='BOX 40', font=('Arial', 15))
        self.label_frame40.pack(side='left')
        self.label40 = tk.Label(self.label_frame40, text='', font=('Arial', 20), background='lightgreen', borderwidth=1, relief='solid')
        self.label40.pack(side='top')
        self.clear_button = tk.Button(self.label_frame40, text='Radera', font=('Arial', 10), command=self.clear_label40) 
        self.clear_button.pack(side='bottom')





        #Frame 11 start
        self.frame11 =tk.Frame(self.root)
        self.frame11.pack(side='top')

        self.entry = tk.Entry(self.frame11)
        self.entry.bind("<KeyPress>", self.shortcut)
        self.entry.pack(side='left')

        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame11, text='Stor PUO', variable=self.checkbox_var, command=self.toggle_button_command)
        self.checkbox.pack(side='right')

        self.button = tk.Button(self.frame11, text='Lägg till', command=self.add_puo)
        self.button.pack(side='right', padx=5)

        


        #Frame 12 start 
        self.frame12 = tk.Frame(self.root)
        self.frame12.pack(side='top', pady=10)

        self.entry_search = tk.Entry(self.frame12)
        self.entry_search.pack(side='left')

        self.button_search = tk.Button(self.frame12, text='Sök', font=('Arial', 10), command=self.search_puo)
        self.button_search.pack(side='right', padx=5)


        #frame13
        self.frame13 = tk.Frame(self.root)
        self.frame13.pack(side='top',pady=10)

        self.textbox = tk.Text(self.frame13, width=30, height=5)
        self.textbox.pack(side='left')


        #Varning för att stänga programmet
        self.root.protocol("WM_DELETE_WINDOW", self.close_page)
    
        self.root.mainloop()


        #Funktion för att stänga programmet
    def close_page(self):
        if messagebox.askyesno(title="Stäng programmet", message="Vill du verkligen stänga programmet?"):
            self.root.destroy()

    
    #Funktion för att klicka på enter_addera
    def shortcut(self, event):
        if event.keysym == "Return":
            self.button.invoke()   

    #Funktion för att söka efter PUO
    def search_puo(self):
        puo = self.entry_search.get()
        self.entry_search.delete(0, 'end')
        if not puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end','Sökfältet är tomt\n')

        elif self.label1.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo} finns i BOX1\n')
        elif self.label2.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX2\n')
        elif self.label3.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX3\n')
        elif self.label4.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX4\n')
        elif self.label5.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX5\n')
        elif self.label6.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX6\n')
        elif self.label7.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX7\n')
        elif self.label8.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX8\n')
        elif self.label9.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX9\n')
        elif self.label10.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX10\n')
        elif self.label11.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX11\n')
        elif self.label12.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX12\n')
        elif self.label13.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX13\n')
        elif self.label14.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX14\n')
        elif self.label15.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX15\n')
        elif self.label16.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX16\n')
        elif self.label17.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX17\n')
        elif self.label18.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX18\n')
        elif self.label19.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX19\n')
        elif self.label20.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX20\n')
        elif self.label21.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX21\n')
        elif self.label22.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX22\n')
        elif self.label23.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX23\n')
        elif self.label24.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX24\n')
        elif self.label25.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX25\n')
        elif self.label26.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX26\n')
        elif self.label27.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX27\n')
        elif self.label28.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX28\n')
        elif self.label29.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX29\n')
        elif self.label30.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX30\n')
        elif self.label31.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX31\n')
        elif self.label32.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX32\n')
        elif self.label33.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX33\n')
        elif self.label34.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX34\n')
        elif self.label35.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX35\n')
        elif self.label36.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX36\n')
        elif self.label37.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX37\n')
        elif self.label38.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX38\n')
        elif self.label39.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX39\n')
        elif self.label40.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX40\n')  
        else:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns ej :(\n')


    #Funktion för att addera PUO
    def add_puo(self):
        puo_no = self.entry.get()
        self.entry.delete(0, 'end')
        
        if not self.label1.cget('text'):
            self.label1.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i BOX 1\n')
        elif not self.label2.cget('text'):
            self.label2.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 2\n')
        elif not self.label3.cget('text'):
            self.label3.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 3\n')
        elif not self.label4.cget('text'):
            self.label4.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 4\n')
        elif not self.label5.cget('text'):
            self.label5.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 5\n')
        elif not self.label6.cget('text'):
            self.label6.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 6\n')
        elif not self.label7.cget('text'):
            self.label7.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 7\n')
        elif not self.label8.cget('text'):
            self.label8.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 8\n')
        elif not self.label9.cget('text'):
            self.label9.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 9\n')
        elif not self.label10.cget('text'):
            self.label10.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 10\n')
        elif not self.label11.cget('text'):
            self.label11.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 11\n')
        elif not self.label12.cget('text'):
            self.label12.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 12\n')
        elif not self.label13.cget('text'):
            self.label13.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 13\n')
        elif not self.label14.cget('text'):
            self.label14.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 14\n')
        elif not self.label15.cget('text'):
            self.label15.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 15\n')
        elif not self.label16.cget('text'):
            self.label16.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 16\n')
        elif not self.label17.cget('text'):
            self.label17.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 17\n')
        elif not self.label18.cget('text'):
            self.label18.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 18\n')
        elif not self.label19.cget('text'):
            self.label19.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 19\n')
        elif not self.label20.cget('text'):
            self.label20.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 20\n')      
        elif not self.label21.cget('text'):
            self.label21.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 21\n')
        elif not self.label22.cget('text'):
            self.label22.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 22\n')
        elif not self.label23.cget('text'):
            self.label23.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 23\n')
        elif not self.label24.cget('text'):
            self.label24.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 24\n')
        elif not self.label25.cget('text'):
            self.label25.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 25\n')
        elif not self.label26.cget('text'):
            self.label26.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 26\n')
        elif not self.label27.cget('text'):
            self.label27.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 27\n')
        elif not self.label28.cget('text'):
            self.label28.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 28\n')
        elif not self.label29.cget('text'):
            self.label29.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 29\n')
        elif not self.label30.cget('text'):
            self.label30.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 30\n')
        elif not self.label31.cget('text'):
            self.label31.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 31\n')
        elif not self.label32.cget('text'):
            self.label32.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 32\n')
        elif not self.label33.cget('text'):
            self.label33.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 33\n')
        elif not self.label34.cget('text'):
            self.label34.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 34\n')
        elif not self.label35.cget('text'):
            self.label35.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 35\n')
        elif not self.label36.cget('text'):
            self.label36.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 36\n')
        elif not self.label37.cget('text'):
            self.label37.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 37\n')
        elif not self.label38.cget('text'):
            self.label38.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 38\n')
        elif not self.label39.cget('text'):
            self.label39.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 39\n')
        elif not self.label40.cget('text'):
            self.label40.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 40\n')
        else:
            messagebox.showinfo('Ajdå! Ingen tom box', 'Ingen tom box kvar!! Säg till Diana :) ') 

    #Kontrollera värdet av checkbox
    def toggle_button_command(self):
        if self.checkbox_var.get():
            self.button.config(command=self.add_bigpuo)
        else:
            self.button.config(command=self.add_puo)
            
    #Adder Big_puo om checkbox har värdet ==True
    def add_bigpuo(self):
        puo_no = self.entry.get()
        self.entry.delete(0, 'end')
        
        if not self.label39.cget('text'):
            self.label39.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i BOX 39\n')
        elif not self.label40.cget('text'):
            self.label40.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i box 40\n')

    #Funktion för att radera PUO
    def clear_label1(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label1.config(text='')
    def clear_label2(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label2.config(text='')
    def clear_label3(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label3.config(text='')    
    def clear_label4(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label4.config(text='')
    def clear_label5(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label5.config(text='')         
    def clear_label6(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label6.config(text='')   
    def clear_label7(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label7.config(text='')
    def clear_label8(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label8.config(text='')
    def clear_label9(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label9.config(text='')  
    def clear_label10(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label10.config(text='')
    def clear_label11(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label11.config(text='')       
    def clear_label12(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label12.config(text='')  
    def clear_label13(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label13.config(text='')      
    def clear_label14(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label14.config(text='')
    def clear_label15(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label15.config(text='')
    def clear_label16(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label16.config(text='')
    def clear_label17(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label17.config(text='')
    def clear_label18(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label18.config(text='')
    def clear_label19(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label19.config(text='')       
    def clear_label20(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label20.config(text='')   
    def clear_label21(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label21.config(text='')
    def clear_label22(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label22.config(text='')
    def clear_label23(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label23.config(text='')
    def clear_label24(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label24.config(text='')       
    def clear_label25(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label25.config(text='')
    def clear_label26(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label26.config(text='')
    def clear_label27(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label27.config(text='')
    def clear_label28(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label28.config(text='')
    def clear_label29(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label29.config(text='')
    def clear_label30(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label30.config(text='')
    def clear_label31(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label31.config(text='')
    def clear_label32(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label32.config(text='')
    def clear_label33(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label33.config(text='')
    def clear_label34(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label34.config(text='')
    def clear_label35(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label35.config(text='')
    def clear_label36(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label36.config(text='')
    def clear_label37(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label37.config(text='')
    def clear_label38(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label38.config(text='')
    def clear_label39(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label39.config(text='')
    def clear_label40(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du vill radera?')
         self.label40.config(text='')
    

green_box()