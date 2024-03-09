import tkinter as tk

class Application(tk.Frame):
    def ＿init＿(self, master=None):
        super().＿init＿(master)

        self.pack()
# create the application

app = Application()
app.master.title("Sumator")
app.master.minsize(width=100, height=50)

# start program
app.mainloop()
def ＿init＿(self, master=None):
    super().＿init＿(master)

    self.pack()
    self.create_widgets()

def create_widgets(self):
    self.firstNumberEntry = tk.Entry()
    self.plusSign = tk.Label(text="+")
    self.secondNumberEntry = tk.Entry()
    self.equalSign = tk.Label(text="=")
    self.resultLabel = tk.Label(text="Result...", bg="green", fg="white")
    self.calculateButton = tk.Button(text="Calculate")
# place widgets
    self.firstNumberEntry.pack(side="left")
    self.plusSign.pack(side="left")
    self.secondNumberEntry.pack(side="left")
    self.equalSign.pack(side="left")
    self.resultLabel.pack(side="left")
    self.calculateButton.pack(side="left")

