# This is a sample Python script.
from pdfviewer import window
import os

#from qt import window

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} ')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ != '__main__':
    pass
# Press the green button in the gutter to run the script.
else:
    print_hi('PyCharm' + os.getcwd() + window.__class__.__name__ )
    window()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
