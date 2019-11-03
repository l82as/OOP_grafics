
from win_py import PyTest

class FileTst(PyTest):
    def __init__(self, tab):
        PyTest.__init__(self, tab)
        self.tab.add(self.tab_py, text='EXE')

