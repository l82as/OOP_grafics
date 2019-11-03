import tkinter as tk

from tkinter.filedialog import askdirectory


class Win:
    def __init__(self, g_with, g_higth):
        self.root = tk.Tk()
        self.root.title("test programm")
        self.root.geometry(str(g_with) + 'x' + str(g_higth))
        self.var_in = tk.IntVar()
        self.var_out = tk.IntVar()
        self.var_type = tk.IntVar()
        self.creat_widgets()
        self.package_widgets()
        self.bindButton()
        self.start_loop()

    def creat_widgets(self):
        self.lab_in = tk.Label(self.root, text="select input", font="Arial 12")

        self.rb_input_h = tk.Radiobutton(self.root, text="horisontal", variable=self.var_in, value=1)
        self.rb_input_v = tk.Radiobutton(self.root, text="vertikal", variable=self.var_in, value=2)
        self.lab_out = tk.Label(self.root, text="select output", font="Arial 12")
        self.rb_out_h = tk.Radiobutton(self.root, text="horizontal", variable=self.var_out, value=1)
        self.rb_out_v = tk.Radiobutton(self.root, text="vertikal", variable=self.var_out, value=2)
        self.lab_type_file = tk.Label(self.root, text="slect type file", font="Arial 12")
        self.rb_type_py = tk.Radiobutton(self.root, text="py file", variable=self.var_type, value=1)
        self.rb_type_exe = tk.Radiobutton(self.root, text="exe file", variable=self.var_type, value=2)

        self.label_prog_dir = tk.Label(self.root, text="slect directory students")
        self.ent_prog_dir = tk.Entry(self.root)
        self.button_select_st = tk.Button(self.root, text = "select")
        self.label_test_dir = tk.Label(self.root, text="select directory with test case")
        self.ent_test_dir = tk.Entry(self.root)
        self.button_select_case = tk.Button(self.root, text="select")
        self.button_start = tk.Button(self.root, text="start")

    def package_widgets(self):
        self.lab_in.grid(column=0, row=0, padx=5, pady=10)
        self.rb_input_h.grid(column=0, row=1, sticky="w", padx=10)
        self.rb_input_v.grid(column=0, row=2, sticky="w", padx=10)
        self.lab_out.grid(column=0, row=3, sticky="w", padx=5)
        self.rb_out_h.grid(column=0, row=4, sticky="w", padx=10)
        self.rb_out_v.grid(column=0, row=5, sticky="w", padx=10)
        self.lab_type_file.grid(column=0, row=6, sticky="w", padx=10)
        self.rb_type_py.grid(column=0, row=7, sticky="w", padx=10)
        self.rb_type_exe.grid(column=0, row=8, sticky="w", padx=10)

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
    def selectDirFiles(self, event):
        os2 = askdirectory()
        self.ent_prog_dir.delete(0, tk.END)
        self.ent_prog_dir.insert(tk.END, os2)
    def selctDirTests(self, event):
        os1 = askdirectory()
        self.ent_test_dir.delete(0, tk.END)
        self.ent_test_dir.insert(tk.END, os1)

    def start_loop(self):
        self.root.mainloop()
