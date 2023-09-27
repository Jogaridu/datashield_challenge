import webview
import ctypes
import os

if __name__ == '__main__':
    

    window = webview.create_window("Datashield", 'http://127.0.0.1:5000/', height=720, width=1280, min_size=(1024, 768), confirm_close=True)
     
    # icon_path = os.path.join(os.path.dirname(__file__), 'static', 'assets', 'icon', 'favicon.ico')
    # icon = ctypes.windll.user32.LoadImageW(None, icon_path, ctypes.c_uint(1), 0, 0, ctypes.c_uint(0x00000010))

    # ctypes.windll.user32.SendMessageW(window._w, 0x80, 0, icon)
    webview.start()
