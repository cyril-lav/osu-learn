import win32gui
# results = []
# win32gui.EnumWindows(lambda handle, liste: liste.append(handle), results)
# get = win32gui.GetWindowText
# for handle in results:
#     print(get(handle))
while(1):
    window_handle = win32gui.FindWindow(None, "osu!")
    if window_handle!=0 :
        window_rect = win32gui.GetWindowRect(window_handle)
        print(window_rect)
    else :
        print("OSU est fermé")
