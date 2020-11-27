import win32gui
import time

"""
results = []
win32gui.EnumWindows(lambda handle, liste: liste.append(handle), results)
get = win32gui.GetWindowText 
if win32gui.GetClassName
get2 = win32gui.GetClassName
for handle in results:
    if get(handle) == "osu!":
        print(get(handle))
        print(get2(handle))
"""

while(1):
    time.sleep(1)
    window_handle = win32gui.FindWindow(None, "osu!")
    if window_handle!=0 and win32gui.GetClassName(window_handle)[0:28] == "WindowsForms10.Window.2b.app":
<<<<<<< HEAD
        window_rect = win32gui.GetWindowRect(window_handle)
        print(window_handle)
=======
            window_rect = win32gui.GetWindowRect(window_handle)
            print(window_rect)
>>>>>>> 0142350a3087adb42237b6851b1768939ee9fd06
    else :
        print("OSU est fermé")

