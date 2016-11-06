import os
import tkinter as tk
from tkinter import ttk

VERSION = "1.0"

class StdGUI(tk.Frame):
    """
        GUI de type notebook avec arborescence gauche
    """

    def __init__(self, master=None):

        tk.Frame.__init__(self, master, padx=10, pady=10)
        self.rootWin = master
        self.rootWin.geometry("400x300")

        self.grid()
        self.createWindow()

    def createWindow(self):

        self.rootWin.title("Standard GUI - " + VERSION)

        self.frame = tk.Frame(self.rootWin)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.pack()

        self.tree = ttk.Treeview(self.frame)
        ysb = ttk.Scrollbar(self.tree, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self.tree, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text="", anchor='w')

        abspath = os.path.abspath(".")
        root_node = self.tree.insert('', 'end', text=abspath, open=True)
        self.process_directory(root_node, abspath)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        self.grid()


    def process_directory(self, parent, path = "."):

        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = self.tree.insert(parent, 'end', text=p, open=False)
            
            if isdir:
                self.process_directory(oid, abspath)


if __name__ == "__main__":

    root = tk.Tk()
    app = StdGUI(root)
    app.mainloop()