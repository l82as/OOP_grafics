import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory

class PyTest:
    def __init__(self, tab):
        self.tab = tab
        self.tab_py = ttk.Frame(self.tab)
        self.tab.add(self.tab_py, text='Python')
        self.var_in = tk.IntVar()
        self.var_in.set(0)
        self.var_out = tk.IntVar()
        self.var_out.set(0)
        self.creatViget()
        self.bindButton()
        self.gridVidgets()

    def creatViget(self):
        self.lab_in = tk.Label(self.tab_py, text="select input", font="Arial 12")

        self.rb_input_h = tk.Radiobutton(self.tab_py, text="horisontal", variable=self.var_in, value=0)
        self.rb_input_v = tk.Radiobutton(self.tab_py, text="vertikal", variable=self.var_in, value=1)
        self.lab_out = tk.Label(self.tab_py, text="select output", font="Arial 12")
        self.rb_out_h = tk.Radiobutton(self.tab_py, text="horizontal", variable=self.var_out, value=0)
        self.rb_out_v = tk.Radiobutton(self.tab_py, text="vertikal", variable=self.var_out, value=1)

        self.label_prog_dir = tk.Label(self.tab_py, text="slect directory students")
        self.ent_prog_dir = tk.Entry(self.tab_py)
        self.button_select_st = tk.Button(self.tab_py, text="select")
        self.label_test_dir = tk.Label(self.tab_py, text="select directory with test case")
        self.ent_test_dir = tk.Entry(self.tab_py)
        self.button_select_case = tk.Button(self.tab_py, text="select")
        self.button_start = tk.Button(self.tab_py, text="start")

    def gridVidgets(self):
        self.lab_in.grid(column=0, row=0, padx=5, pady=10)
        self.rb_input_h.grid(column=0, row=1, sticky="w", padx=10)
        self.rb_input_v.grid(column=0, row=2, sticky="w", padx=10)
        self.lab_out.grid(column=0, row=3, sticky="w", padx=5)
        self.rb_out_h.grid(column=0, row=4, sticky="w", padx=10)
        self.rb_out_v.grid(column=0, row=5, sticky="w", padx=10)

        self.label_prog_dir.grid(column=1, row=0)
        self.ent_prog_dir.grid(column=1, row=1)
        self.button_select_st.grid(column=2, row=1, sticky="w")
        self.label_test_dir.grid(column=1, row=2)
        self.ent_test_dir.grid(column=1, row=3)
        self.button_select_case.grid(column=2, row=3, sticky="w")
        self.button_start.grid(column=1, row=4)

    def bindButton(self):
        self.button_select_st.bind('<Button-1>', self.selectDirFiles)
        self.button_select_case.bind('<Button-1>', self.selctDirTests)
        self.button_start.bind('<Button-1>', self.printTest)

    def printTest(self, event):
        print(self.var_in.get())
        print(self.var_out.get())



    def selectDirFiles(self, event):
        os2 = askdirectory()
        self.ent_prog_dir.delete(0, tk.END)
        self.ent_prog_dir.insert(tk.END, os2)
    def selctDirTests(self, event):
        os1 = askdirectory()
        self.ent_test_dir.delete(0, tk.END)
        self.ent_test_dir.insert(tk.END, os1)

    def packTab(self):
        self.tab.pack(expand=1, fill='both')

class FileTst(PyTest):
    def __init__(self, tab):
        PyTest.__init__(self, tab)
        self.tab.add(self.tab_py, text='EXE')

