import tkinter as tk
from tkinter import ttk

class Win:
    def __init__(self, g_with, g_higth):
        self.root = tk.Tk()
        self.root.title("test programm")
        self.root.geometry(str(g_with) + 'x' + str(g_higth))

        self.insertVidgets()
        self.startLoop()
    def startLoop(self):
        self.root.mainloop()
    def insertVidgets(self):
        self.tab_control = ttk.Notebook(self.root)
        self.py_tab = PyTest(self.tab_control)
        self.exe_tab = FileTst(self.tab_control)
        self.py_tab.packTab()
        self.exe_tab.packTab()
class PyTest:
    def __init__(self, tab):
        self.tab = tab
        self.tab_py = ttk.Frame(self.tab)
        self.tab.add(self.tab_py, text = 'Python')
    def packTab(self):
        self.tab.pack(expand=1, fill='both')
class FileTst:
    def __init__(self, tab):
        self.tab = tab
        self.tab_py = ttk.Frame(self.tab)
        self.tab.add(self.tab_py, text='EXE')
    def packTab(self):
        self.tab.pack(expand=1, fill='both')


