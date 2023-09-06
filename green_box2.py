import tkinter as tk

class Box:
    def __init__(self, master, num):
        self.master = master
        self.num = num
        self.frame = tk.Frame(master)
        self.frame.pack(side=tk.LEFT)
        self.label = tk.Label(self.frame, text=f"Box {num}")
        self.label.pack()
        self.delete_button = tk.Button(self.frame, text="Radera", command=self.delete_number, state=tk.DISABLED)
        self.delete_button.pack()
        self.number = None
        
    def add_number(self, number):
        if self.number:
            return False
        self.number = number
        self.label.config(text=f"Box {self.num}: {self.number}")
        self.delete_button.config(state=tk.NORMAL)
        return True
        
    def delete_number(self):
        self.number = None
        self.label.config(text=f"Box {self.num}")
        self.delete_button.config(state=tk.DISABLED)
        
class App:
    def __init__(self, master):
        self.master = master
        self.boxes = [Box(master, i) for i in range(1, 21)]
        self.entry_label = tk.Label(master, text="Skriv in numret:")
        self.entry_label.pack(side=tk.LEFT)
        self.entry = tk.Entry(master, width=10)
        self.entry.pack(side=tk.LEFT)
        self.add_button = tk.Button(master, text="Lägg till", command=self.add_number)
        self.add_button.pack(side=tk.LEFT, padx=10)
        self.search_label = tk.Label(master, text="Sök nummer:")
        self.search_label.pack(side=tk.LEFT)
        self.search_entry = tk.Entry(master, width=10)
        self.search_entry.pack(side=tk.LEFT)
        self.search_button = tk.Button(master, text="Sök", command=self.search_number)
        self.search_button.pack(side=tk.LEFT)
        
    def add_number(self):
        number = self.entry.get()
        self.entry.delete(0, tk.END)
        for box in self.boxes:
            if box.add_number(number):
                return
        self.boxes[0].add_number(number)
    
    def search_number(self):
        number = self.search_entry.get()
        self.search_entry.delete(0, tk.END)
        for box in self.boxes:
            if box.number == number:
                print(f"{number} finns i box {box.num}")
                return
        print(f"Programmet hittade inte numret {number}")
        

root = tk.Tk()
app = App(root)
root.mainloop()