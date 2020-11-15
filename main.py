from PythonMailHF.mypackage.Emailer import Emailer
from PythonMailHF.mypackage.jsondata import jsondata
import tkinter as tk
from tkinter import filedialog

HEIGHT = 600
WIDTH = 800


class App:
    def __init__(self, root):
        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()
        self.receiver_label = tk.Label( root, text="To: ")
        self.receiver_label.place(x=180, y=20)
        self.receiver_entry = tk.Entry(root, width=50)
        self.receiver_entry.place(x=220 + self.receiver_label.winfo_width(), y=20)
        self.subject_label = tk.Label( root, text="Subject: ")
        self.subject_label.place(x=150, y=50)
        self.subject_entry = tk.Entry( root, width=50)
        self.subject_entry.place(x=220 + self.subject_label.winfo_width(), y=50)
        self.message_label = tk.Label( root, text="Message:")
        self.message_label.place(x=160 - self.message_label.winfo_reqwidth(), y=100)
        self.message_text = tk.Text( root, height=25, width=65)
        self.message_text.place(x=160, y=100)
        self.button = tk.Button( root, text="Send", fg='black', command=self.send_click)
        self.button.place(x=WIDTH / 2 - self.button.winfo_reqwidth() / 2, y=540)
        self.run()

    def send_click(self):
        em = Emailer(self.data.data["address"], self.data.data["password"])
        em.send(self.receiver_entry.get(), self.subject_entry.get(), self.message_text.get("1.0", tk.END))
        self.clear_entries()

    def clear_entries(self):
        self.message_text.delete("1.0", tk.END)
        self.subject_entry.delete("0", tk.END)
        self.receiver_entry.delete("0", tk.END)

    def run(self):
        filename = tk.filedialog.askopenfilename(title="Select file with your email and password")
        self.data = jsondata(filename)

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()









