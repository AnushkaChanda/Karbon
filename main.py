import tkinter as tk
import threading
from ui_items.karbon_ui import KarbonUI
from preview import webview_main
import sys
import os

# Function to get the correct path for bundled data files
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

import os

# Step 1: Create autosave directory
autosave_dir = "autosave"
os.makedirs(autosave_dir, exist_ok=True)




if __name__ == "__main__":
    def start_ui():
        root = tk.Tk()
        app = KarbonUI(root)
        # --- MODIFIED: Add protocol handler to save settings on close ---
        def on_closing():
            app.save_settings()
            root.destroy()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        # --- END MODIFIED ---
        root.mainloop()

    # Run Tkinter in a separate thread
    ui_thread = threading.Thread(target=start_ui)
    ui_thread.daemon = True
    ui_thread.start()

    # Run Flask and webview in the main thread
    webview_main()
