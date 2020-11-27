import win32gui
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
    window_handle = win32gui.FindWindow(None, "osu!")
    if window_handle!=0 and win32gui.GetClassName(window_handle)[0:28] == "WindowsForms10.Window.2b.app":
        window_rect = win32gui.GetWindowRect(window_handle)
        print(window_handle)
    else :
        print("OSU est fermé")

