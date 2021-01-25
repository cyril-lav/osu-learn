import win32gui as wingui
import re


def getWindowPos():
    def callback(handle, data):
        if(re.match(r".*osu.*", wingui.GetWindowText(handle))):
            pos = (wingui.GetWindowRect(handle))
            tabPos.append(pos)

    tabPos = []
    wingui.EnumWindows(callback, None)
    return tabPos
