from tkinter import filedialog as tkFileDialog
import tkinter as tk


class ArduinoConfigurationWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Konfiguracja arduino przy użyciu PyFirmata")
        self.root.geometry("550x500")
        self.set_widgets()

    def set_widgets(self):
        port_name = tk.Label(self.root, text="Nazwa portu")
