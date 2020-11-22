import win32gui
#results = []
#win32gui.EnumWindows(lambda handle, liste: liste.append(handle), results)
#get = win32gui.GetWindowText
#for handle in results:
#    print(get(handle))
while(1):
    window_handle = FindWindow(None, "osu!")
    if window_handle!=0 :
        window_rect   = GetWindowRect(window_handle)
        print(window_rect)
    else :
        print("OSu est fermé")
