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
        self.frame1.pack(side='top',pady=20)

        #BOX1
        self.label_frame1 = tk.LabelFrame(self.frame1, text='BOX 1', font=('Arial',15))
        self.label_frame1.pack(side='left')
        self.label1 = tk.Label(self.label_frame1, text='', font=('Arial', 20), background='green',borderwidth=1, relief='solid')
        self.label1.pack(side='top')
        self.clear_button = tk.Button(self.label_frame1, text='Radera', font=('Arial',10), command=self.clear_label1)
        self.clear_button.pack(side='bottom')

        #BOX2
        self.label_frame2 = tk.LabelFrame(self.frame1, text='BOX 2', font=('Arial', 15))
        self.label_frame2.pack(side='left')
        self.label2 = tk.Label(self.label_frame2, text='', font=('Arial', 20), background='green',borderwidth=1, relief='solid')
        self.label2.pack(side='top')
        self.clear_button = tk.Button(self.label_frame2, text='Radera', font=('Arial', 10), command=self.clear_label2)
        self.clear_button.pack(side='bottom')


        #Frame 5 start
        self.frame5 =tk.Frame(self.root)
        self.frame5.pack(side='top')

        self.entry = tk.Entry(self.frame5)
        self.entry.bind("<KeyPress>", self.shortcut)
        self.entry.pack(side='left')

        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.frame5, text='Stor PUO', variable=self.checkbox_var, command=self.toggle_button_command)
        self.checkbox.pack(side='right')

        self.button = tk.Button(self.frame5, text='Lägg till', command=self.add_puo)
        self.button.pack(side='right', padx=5)


        #Frame 6 start 
        self.frame6 = tk.Frame(self.root)
        self.frame6.pack(side='top', pady=10)

        self.entry_search = tk.Entry(self.frame6)
        self.entry.bind("<KeyPress>2", self.shortcut2)
        self.entry_search.pack(side='left')

        self.button_search = tk.Button(self.frame6, text='Sök', font=('Arial', 10), command=self.search_puo)
        self.button_search.pack(side='right', padx=5)


        #frame7
        self.frame7 = tk.Frame(self.root)
        self.frame7.pack(side='top',pady=10)

        self.textbox = tk.Text(self.frame7, width=30, height=5)
        self.textbox.pack(side='left')

        #frame8


        

        self.root.mainloop()


    def test_button(self):
        self.textbox.delete('1.0','end')
        self.textbox.insert('end','Test test funkar\n')



    def toggle_button_command(self):
        if self.checkbox_var.get():
            self.button.config(command=self.add_bigpuo)
        else:
            self.button.config(command=self.add_puo)

       #Funktion för att klicka på enter_addera
    def shortcut(self, event):
        if event.keysym == "Return" and self.entry.get().strip():  # Kontrollera om entry-fältet har innehåll
            self.button.invoke()

    def shortcut2(self, event):
        if event.keysym == "Return" and self.entry_search.get().strip() and not self.entry.get().strip():
            self.button_search.invoke()


    
    #Funktion för att söka efter PUO
    def search_puo(self):
        puo = self.entry_search.get()
        self.entry_search.delete(0, 'end')
        if not puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end','Sökfältet är tomt\n')

        elif self.label1.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX1\n')
        elif self.label2.cget('text') == puo:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns i BOX2\n')
        else:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo} finns inte i någon av boxarna\n')
    
    # Funktion för att ändra bakgrundsfärg på label vid tillägg av PUO-nummer
    def toggle_label_bg(self, label):
        if label.cget('background') == 'green':
            self.label1.config(background='green')
            self.label2.config(background='yellow')
            label.config(background='yellow')
        else:
            label.config(background='green')



    #Funktion för att addera PUO (Tillägg: Puon ska försvinna när man klickar på knapen)
    def add_puo(self):
        puo_no = self.entry.get()
        self.entry.delete(0, 'end')
        if not self.label1.cget('text'):
            self.label1.config(text=puo_no, background='green')
            self.toggle_label_bg(self.label1)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo_no} lades till i BOX 1\n')
        elif not self.label2.cget('text'):
            self.label2.config(text=puo_no, background='green')
            self.toggle_label_bg(self.label2)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'PUO {puo_no} lades till i BOX 2\n')
        else:
            messagebox.showinfo('Ajdå! Ingen tom box', 'Säg til Leonard att fixa sitt skit proggram :)')
    
    def add_bigpuo(self):
        puo_no = self.entry.get()
        self.entry.delete(0, 'end')
        
        if not self.label2.cget('text'):
            self.label2.config(text=puo_no)
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('end', f'{puo_no} lades till i BOX 1\n')
    
    
    #Funktion för att radera PUO
    def clear_label1(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du radera?')
         self.label1.config(text='')
    def clear_label2(self):
         messagebox.askyesno('Radera PUO ur BOX', 'Är du säker på att du radera?')
         self.label2.config(text='')

green_box()