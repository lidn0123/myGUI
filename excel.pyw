# _*_ coding: utf-8 _*_
__author__ = ''
__project__ = ''

# 

from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)


def excel():
    app = 'Excel'
    xl = win32.gencache.EnsureDispatch('{0}.Application'.format(app))
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.Visible = True

    sleep(1)

    sh.Cells(1, 1).Value = 'Python-to-{0} Demo'.format(app)
    sleep(1)
    for i in RANGE:
        sh.Cells(i, 1).Value = 'Line {0}'.format(i)
        sleep(1)
    sh.Cells(i + 2, 1).Value = 'Th-th-th-that\'s all folks!'

    warn(app)
    ss.Close(False)
    xl.Application.Quit()


if __name__ == '__main__':
    Tk().withdraw()
    excel()
